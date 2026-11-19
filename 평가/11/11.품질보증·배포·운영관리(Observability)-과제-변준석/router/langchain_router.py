from fastapi import APIRouter, Query
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from fastapi.responses import HTMLResponse
import markdown

from openai import OpenAI

from google import genai
from google.genai import types

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser

router = APIRouter(tags=["langchain"])
load_dotenv()

# 그냥 gpt에 말하기 - 단발성
@router.get("/langchain/gpt")
def gpt(prompt: str):
    model = ChatOpenAI(
        model='gpt-5.5',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    output = model.invoke(prompt)
    return output

# langchain 모듈 사용
# 멀티턴으로 gpt에 말하기
@router.get("/langchain/gpt/multi")
def gpt2(prompt: str):
    model = ChatOpenAI(
        model='gpt-5.6',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    messages = [
        {"role": "system", "content": "너는 친절한 조수야"},
        {"role": "user", "content": "내 이름은 00야."},
        {"role": "assistant", "content": "안녕하세요. 00님! 친절히 알려드릴께요"},
        {"role": "user", "content": prompt}
    ]

    output = model.invoke(messages)

    # 실제 대답은 output.content에 들어있음
    return output

# openai 모듈 사용
@router.get("/original/gpt")
def gpt3(prompt: str):
    # 쌩으로 openai 모듈 사용법
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    messages = [
        {"role": "system", "content": "너는 친절한 조수야"},
        {"role": "user", "content": "내 이름은 00야."},
        {"role": "assistant", "content": "안녕하세요. 00님! 친절히 알려드릴께요"},
        {"role": "user", "content": prompt}
    ]

    output = client.chat.completions.create(
        model='gpt-5.6',
        messages=messages
    )
    # 실제 대답은 output.choices[0].message.content에 들어있음
    return output

# genai 모듈 사용
@router.get("/original/gemini")
def gemini1(prompt: str):
    # 쌩으로 genai 모듈 사용법
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    # genai를 사용할 때
    # role에 system 없음
    # parts로 적어야 함
    messages = [
        {"role": "user", "parts": [{'text': "내 이름은 00야."}]},
        {"role": "model", "parts": [{'text': "안녕하세요. 00님! 친절히 알려드릴께요"}]},
        {"role": "user", "parts": [{'text': prompt}]}
    ]

    output = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction="너는 친절한 조수야",
            temperature=0.0
        )
    )

    # 실제 대답은 candidates[0].content.parts[0].text에 들어있음
    return output

# langchain 모듈 사용
@router.get("/langchain/gemini")
def gemini2(prompt: str):
    model = ChatGoogleGenerativeAI(
        model='gemini-3.8-flash',
        temperature=0,
        api_key=os.getenv("GEMINI_API_KEY")
    )

    messages = [
        {"role": "system", "content": "너는 친절한 조수야"},
        {"role": "user", "content": "내 이름은 00야."},
        {"role": "assistant", "content": "안녕하세요. 00님! 친절히 알려드릴께요"},
        {"role": "user", "content": prompt}
    ]

    output = model.invoke(messages)

    # 실제 대답은 output.content[0].text에 들어있음
    return output


# langchain의 message 모듈 사용해서 질문하기
@router.get("/langchain/gpt/message")
def gpt4(prompt: str):
    model = ChatOpenAI(
        model='gpt-5.6',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # provider에 따라 형식을 맞춰줌
    messages = [
        SystemMessage("너는 친절한 조수야"),
        HumanMessage("내 이름은 00야."),
        AIMessage("안녕하세요. 00님! 친절히 알려드릴께요"),
        HumanMessage(prompt)
    ]

    output = model.invoke(messages)

    # 실제 대답은 output.content에 들어있음
    return output

# stream으로 출력하기
@router.get("/langchain/gpt/stream")
def gpt5(prompt: str):
    model = ChatOpenAI(
        model='gpt-5.6',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # provider에 따라 형식을 맞춰줌
    messages = [
        SystemMessage("너는 친절한 조수야"),
        HumanMessage("내 이름은 00야."),
        AIMessage("안녕하세요. 00님! 친절히 알려드릴께요"),
        HumanMessage(prompt)
    ]

    for chunk in model.stream(messages):
        print(chunk.content, end='', flush=True)

@router.get("/langchain/gpt/chat_prompt_template")
def chat_prompt_template(name: str, prompt: str):
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "너는 친절한 조수야"),
        ("human", "내 이름은 {name}야."),
        ("ai", "안녕하세요. {name}님! 친절히 알려드릴께요"),
        ("human", '{prompt}') # 아직 '{prompt}'라는 글씨일 뿐
    ])

    prompt_template.invoke({
        "name": name, 
        "prompt": prompt
    })

    print(prompt_template)

@router.get("/langchain/gpt/messages_placeholder")
def messages_placeholder(name: str, prompt: str):
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "너는 친절한 조수야"),
        MessagesPlaceholder("history", optional=True),
        ("human", '{prompt}') # 아직 '{prompt}'라는 글씨일 뿐
    ])

    prompt_template.invoke({
        "history": [
            HumanMessage("내 이름은 00야."),
            AIMessage("안녕하세요. 00님! 친절히 알려드릴께요"),
        ], 
        "prompt": prompt
    })

    print(prompt_template)

class Recipe(BaseModel):
    food: list[str]
    steps: list[str]


@router.get("/langchain/output_parser")
def output_parser(dish:str):
    
    output_parser = PydanticOutputParser(pydantic_object=Recipe)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                'system',

                '사용자가 입력한 요리의 레시피를 생각해 주세요.'
                '{format_instructions}'
            ),
            ('human', '{dish}')
        ]
    )

    prompt2 = prompt.partial(
        format_instructions = output_parser.get_format_instructions()
    )

    prompt_value = prompt2.invoke({
        'dish': dish
    })

    print(prompt_value)

    model = ChatOpenAI(
        model='gpt-5.6',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    ai_msg = model.invoke(prompt_value)

    print(ai_msg)

    result = output_parser.invoke(ai_msg)

    return result

@router.get("/langchain/str_output_parser")
def str_output_parser(dish:str):

    model = ChatOpenAI(
        model='gpt-5.6',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    ai_msg = model.invoke(f'{dish}의 레시피를 간략히 알려줘')

    # result = StrOutputParser().parse(ai_msg) # 전문 모두 나옴
    result = StrOutputParser().invoke(ai_msg) # content만 나옴

    return result

@router.get("/langchain/chain")
def chain(dish:str, name:str):
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "당신은 절대적으로 친절한 조수입니다."),
        ("human", "내 이름은 {name}야."),
        ("ai", "안녕하세요. {name}님! 친절히 알려드릴께요."),
        ("human", '{prompt}') # 아직 '{prompt}'라는 글씨일 뿐
    ])

    model = ChatOpenAI(
        model='gpt-5.6',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    chain = prompt_template | model | StrOutputParser()

    result = chain.invoke({
        'name': name,
        'prompt': f'{dish}의 레시피를 간략히 알려줘.'
    })

    return result

@router.get("/langchain/chain/pydantic")
def chain_pydantic(dish:str):

    output_parser = PydanticOutputParser(pydantic_object=Recipe)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "너는 미슐렝 쉐프야. 나는 요리 초보고 자취생이라 기구가 거의 없어."
                "네가 쉽고 빠르게 만들 수 있는 레시피를 알려줘."
                '{format_instructions}'
            ),
            ("human", '{dish}')
        ]
    ).partial(
        format_instructions = output_parser.get_format_instructions()
    )

    model = ChatOpenAI(
        model='gpt-5.6',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    ).bind(
        # 출력 양식을 json으로 함
        # 이것 만으로는 Recipe의 변수와 매칭되리라는 보장이 없음
        response_format={
            'type': 'jaon_object'
        }
    )

    chain = prompt | model | output_parser

    result = chain.invoke({
        'dish': dish
    })

    return result

@router.get("/langchain/chain/with_structured_output")
def chain_with_structured_output(dish:str):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "너는 미슐렝 쉐프야. 나는 요리 초보고 자취생이라 기구가 거의 없어."
                "네가 쉽고 빠르게 만들 수 있는 레시피를 알려줘. 계량도 내 것만으로 할 수 있게"
            ),
            ("human", '{dish}')
        ]
    )

    model = ChatOpenAI(
        model='gpt-5.6',
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    chain = prompt | model.with_structured_output(Recipe)

    return chain.invoke({
        'dish': dish
    })

from elasticsearch import Elasticsearch
from router import es_router

@router.get("/langchain/recommend/hybrid")
def recommend_hybrid(
    userId: int,                # CF에서 사용할 사용자 ID
    provider: Literal['GPT', 'Gemini'] = 'GPT',
    top_k: int = 10,            # 결과 개수
    candidate_size: int = 50,    # 각각의 추천의 후보 수
    list_movieId: list[int] = Query(...)    # CBF에서 사용할 영화 목록
):
    # 예전에 만들어 뒀던 hybrid 추천 결과를 그대로 가져와서
    # langchain으로
    # LLM에게 이쁘게 포장해달라고 해서 그 결과를 출력
    # 단, 사용자가 GPT랑 Gemini를 선택할 수 있게 하기
    hybrid = es_router.hybrid(userId, top_k, candidate_size, list_movieId)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                '너는 영화 추천 서비스의 설명 도우미야.'
                '필요하면 인터넷 검색을 해서 알아봐.'
                '입력 받은 추천 결과만 사용해서 설명해.'
                '결과는 구조적인 json으로 알려줘.'
            ),
            (
                "human", 
                'cbf, cf의 하이브리드 추천 결과물: {hybrid}'
                '제목을 한국 제목으로 변경해서 알려줘. 단 제목을 추측하지 마.'
                '영화 줄거리도 알려줘. 단 추측하지 마.'
                '순위를 보고 3개 정도면 정리해주면 되.'
            )
        ]
    )

    if provider == 'GPT':
        # ChatOpenAI 객체 생성
        model = ChatOpenAI(
            model='gpt-5.6',
            temperature=0,
            api_key=os.getenv("OPENAI_API_KEY")
        )

    elif provider == 'Gemini':
        # ChatGoogleGenerativeAI 객체 생성
        model = ChatGoogleGenerativeAI(
            model='gemini-3.8-flash',
            temperature=0,
            api_key=os.getenv("GEMINI_API_KEY")
        )

    chain = prompt | model | StrOutputParser()

    return chain.invoke({
        'hybrid': hybrid
    })

    # result = chain.invoke({
    #     'hybrid': hybrid
    # })

    # html = markdown.markdown(result)

    # return HTMLResponse(content=html)