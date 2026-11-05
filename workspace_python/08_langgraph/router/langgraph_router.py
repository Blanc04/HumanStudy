from fastapi import APIRouter, Query
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from fastapi.responses import HTMLResponse
from openai import OpenAI

from google import genai
from google.genai import types

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser

from langgraph.graph import StateGraph, START, END
from typing import Literal, Optional

from elasticsearch import Elasticsearch
# from router import es_router
from router.es_router import (
    content_based_filtering, 
    collaborative_filtering, 
    search_movies,
    term_movieId
)

router = APIRouter(tags=["langgraph"])
load_dotenv()

'''
    * list_movieId, userId와 질문을 입력
    * 추천 방식을 분석하고 선정
    * 선정된 방식으로 추천
    * 결과를 이쁘게 포장해서 출력
'''

# 상태 클래스 : langGraph에서 공유할 객체
class State(BaseModel):
    list_movieId: Optional[list[int]] = None                    # CBF에서 사용할 영화 Id 목록
    userId: Optional[int] = None                                # CF에서 사용할 사용자 Id
    top_k: int = 10                                             # 결과물 개수

    question: str                                               # 사용자 질문

    recommend_type: Optional[str] = None                        # 사용할 추천 방식
    recommend_type_reason: Optional[str] = None                 # 추천 타입 선정의 이유

    recommends: Optional[list[dict]] = None                     # 추천 목록들

    explain: Optional[str] = 'LLM 응답 없음'                     # 최종 답변

    error: Optional[str] = None                                 # 에러 메시지



class RecommendType(BaseModel):
    recommend_type: Literal['CBF', 'CF', 'BM25'] = 'CBF'        # 사용할 추천 방식
    recommend_type_reason: str                                  # 추천 타입 선정의 이유


# 질문을 기반으로 추천 방식을 선택
def recommend_select(state: State):
    question = state.question

    # 프롬프트 준비
    prompt = ChatPromptTemplate.from_messages([
        ('system', 
            '''
                당신은 영화 추천 시스템의 추천 방식을 선택하는 역할
                사용자의 질문의 의도를 파악해서 세 가지 중 하나만 선택

                1. [CBF]
                    - 특정 영화와 비슷한 영화를 찾는 경우
                    - 장르와 사용자들의 태그 기반으로 추천하는 경우
                2. [CF]
                    - 사용자의 취향과 비슷한 다른 사용자들의 평점 패턴 분석 기반으로 추천하는 경우
                3. [BA25]
                    - 제목, 장크, 태그 등의 키워드로 검색하는 경우
            '''
        ),
        ('human', '*** 사용자 질문: {question}')
    ])

    # 모델 준비
    model = ChatOpenAI(
        model='gpt-5.6',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # chain
    chain = prompt | model.with_structured_output(RecommendType)

    # chain 실행 결과를 State의 필드에 저장하게 return
    result = chain.invoke({
        'question': state.question
    })
    print('recommend_select >> result: ', result)

    return {
        'recommend_type': result.recommend_type,
        'recommend_type_reason': result.recommend_type_reason
    }

def normalize(response, top_k):
    movieIds = set()
    recommends = []

    for hit in response['hits']['hits']:
        source = hit['_source']

        movieId = source.get('movieId')
        if movieId not in movieIds :
            movieIds.add(movieId)

            recommends.append({
                'movieId': movieId,
                'title': source.get('title', ''),
                'genres': source.get('genres', []),
                'tags': source.get('tags', []),
                'score': hit.get('_score', -1),
            })

    # top-k개가 지나면 break로 끝내고 되겠음
    return recommends[:top_k]
    

def cbf(state: State):
    response = content_based_filtering(state.list_movieId)

    recommends = normalize(response, state['top_k'])

    return {
        'recommends': recommends
    }


def cf(state: State):
    '''
        [{
            'movieId': movieId,
            'score': score
        }]
    '''
    result = collaborative_filtering(state.userId)
    movieIds = set()
    for info in result:
        movieIds.add(info.get('movieId', 0))

    response = term_movieId(movieIds)

    recommends = normalize(response, state['top_k'])

    return {
        'recommends': recommends
    }

def bm25(state: State):
    response = search_movies(state.question)

    recommends = normalize(response, state['top_k'])

    return {
        'recommends': recommends
    }

def explain(state:State):
    # 프롬프트 준비
    prompt = ChatPromptTemplate.from_messages([
        ('system', 
            '''
                당신은 영화 추천 시스템의 추천 방식을 선택하는 역할
                설명을 섹시하게 해서 꼭 볼 수 밖에 없는 설득력을 가짐
                간략하게 중요 내용만 설명

                [주의사항]
                    - 결과에 없는 영화를 추천하지 않습니다.
                    - 제목을 한국 것으로 검색해서 원제와 함께 알려줍니다.
            '''
        ),
        ('human', 
         '''
            [사용자 질문]: {question}
            [검색 방식]: {recommend_type}
            [검색 결과]
            {recommends}
            [할 일]: 위 정보로 사용자에게 잘 설명하시오.
         '''
         )
    ])

    # 모델 준비
    model = ChatOpenAI(
        model='gpt-5.6',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # chain
    chain = prompt | model | StrOutputParser()

    result = chain.invoke({
        'question': state.question,
        'recommend_type': state.recommend_type,
        'recommends': state.recommends,
    })

    return {
        'explain': result
    }

def validator(state: State):
    type = state.recommend_type
    if type == 'CBF':
        if state.list_movieId is None :
            return 'ERROR'

    elif type == 'CF':
        if state.userId is None :
            return 'ERROR'
    
    return type

def makeErrorMessage(state: State):

    error = None

    type = state.recommend_type
    if type == 'CBF':
        error = 'list_movieId는 필수입니다'
    elif type == 'CF':
        error = 'userId는 필수입니다'

@router.post('/langgraph/recommend')
def recommend(param: State):
    print(param)
    # question = param.question

    # 랭그래프 생성
    graph = StateGraph(State)

    # 노드 등록
    graph.add_node('select', recommend_select)
    graph.add_node('CBF', cbf)
    graph.add_node('CF', cf)
    graph.add_node('BM25', bm25)
    graph.add_node('explain', explain)

    graph.add_node('validator', validator)
    graph.add_node('makeErrorMessage', makeErrorMessage)

    # 노드 간의 엣지 설정
    graph.add_edge(START, 'select')

    graph.add_conditional_edges(
        'select',
        # lambda s : s.recommend_type,
        'validator',
        {
            'CBF': 'CBF',
            'CF': 'CF',
            'BM25': 'BM25',
            'ERROR': 'makeErrorMessage'
        }
    )

    graph.add_edge('CBF', 'explain')
    graph.add_edge('CF', 'explain')
    graph.add_edge('BM25', 'explain')

    graph.add_edge('explain', END)
    graph.add_edge('makeErrorMessage', END)

    # 실행 가능한 랭그래프 객체로 만들기
    recommend_graph = graph.compile()
    result = recommend_graph.invoke({
        'list_movieId': param.list_movieId,
        'userId': param.userId,
        'top_k': param.top_k,
        'question': param.question,
        'recommends': [],
    })

    return result


    


