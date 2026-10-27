from fastapi import APIRouter, Query
import traceback
import util
import pandas as pd
from typing import Any

import os

from elasticsearch import helpers

from collections import Counter
import math

router = APIRouter(tags=["엘라스틱서치"])

@router.get("/read/head")
# def read(fileName) :
def read(fileName : Literal['movies.csv', 'tags.csv', 'ratings.csv'] = 'movies.csv') :
    print('fileName :', fileName)
    frame = util.load_csv(fileName)
    if frame is None :
        return {'ERROR': "파일을 불러오지 못했습니다"}

    '''
        head : 상위 몇 개의 데이터만 추출 (기본값 : 5)
        astype : 형변환, 기본값:NumPy.int64
        to_dict : dict로 변환
        orient='records' : 컬럼명:값 형태 
                           기본값=dict : 인덱스가 키가 된다
    '''
    preview = frame.head().astype(object).to_dict(orient='records')
    return preview

@router.get('/read/valid')
def valid():
    df_movies = util.load_csv('movies.csv')
    df_tags = util.load_csv('tags.csv')
    df_ratings = util.load_csv('ratings.csv')

    # dropna : N/A 즉 결측치 즉 없는 것 제외
    notnull = df_movies['movieId'].dropna()

    # set 타입의 속성을 이용해서 id 중복 제거
    movie_ids = set(notnull)
    tag_ids = set(df_tags['movieId'].dropna())
    rating_ids = set(df_ratings['movieId'].dropna())

    result = {}
    result['no_id'] = {}
    result['no_id']['tags'] = len(tag_ids - movie_ids)
    result['no_id']['ratings'] = len(rating_ids - movie_ids)

    result['rating range'] = {}
    result['rating range']['min'] = float(df_ratings['rating'].min())
    result['rating range']['max'] = float(df_ratings['rating'].max())

    return result

# 제목+장르들+태그들 을 한 문장으로 만들기
def makeContent() :
    df_movies = util.load_csv('movies.csv')
    df_tags = util.load_csv('tags.csv')

    # pandas
    # 데이터 프레임 : 2차원 배열
    # 시리즈 : 1차원 값
    result = pd.DataFrame()
    result['movieId'] = df_movies['movieId']
    # pandas 타입을 string 타입으로 변경 후 앞뒤공백 제거
    result['title'] = df_movies['title'].astype(str).str.strip()

    # 장르는 a|b|c 형식으로 되어있다
    # 그래서 list로 바꾸겠다
    def parse_genre(genres):
        result = []
        if str(genres).strip() == '' or str(genres).strip() == '(no genres listed)' :
            return result

        list_genre = str(genres).split('|')
        for genre in list_genre :
            # strip : 앞뒤공백 제거
            # lower : 소문자로
            result.append(genre.strip().lower())

        return result

    # 장르의 리스트가 쌓인다
    result['list_genre'] = df_movies['genres'].map(parse_genre)


    # copy() : 원본을 보존하고 사본을 가져온다
    tags = df_tags[ ['movieId', 'tag'] ].copy()

    # 공백제거 후 소문자로 변환
    tags['tag'] = tags['tag'].astype(str).str.strip().str.lower()

    # group by 처럼 중복 제거
    tags = tags.drop_duplicates(['movieId', 'tag'])

    # # pandas의 data frame 특성인데 컬림이 아니라 True인 것만 반복 시킨다
    # tags = tags[tags['tag'] != ''].drop_duplicates(['movieId', 'tag'])

    # print(tags.head())

    movie_tags = {}
    for info in tags.to_dict(orient="records") :
        id = info['movieId']
        tag = info['tag']

        # 딕셔너리의 key 중에서 id가 없으면
        if id not in movie_tags :
            # movie_tags[id] : key를 id로 만들고
            # 그 값을 리스트로 초기화
            movie_tags[id] = []
        movie_tags[id].append(tag)

    # 위 코드를 한줄로 줄이면
    # tags.groupby('movieId') : data frame인 tags를 movieId로 group by 해서
    # ['tag'] : group by 한 것에서 tag 항목을 꺼내고
    # agg(list) : 결과를 list로 만들어서
    '''
        to_dict() 까지 한 결과
        {
            movieId1 : [tag1, tag2],
            movieId2 : [tag11, tag12]
        }
    '''
    movie_tags = tags.groupby('movieId')['tag'].agg(list).to_dict()


    result['list_tag'] = df_movies['movieId'].map(lambda id : movie_tags.get(id, []))

    # 파이썬의 리스트는 + 제공
    # [1,2] + [3,4] == [1,2,3,4]

    # map : 한 컬럼을 대상으로 반복
    # apply : 모든 컬럼을 대상으로 반복
    # axis : 기본값 0
    #           0 : 위에서 아래로 읽기
    #           1 : 왼쪽에서 오른쪽으로
    result['content_text'] = result.apply(
        lambda info : " ".join( [ info['title'] ] + info['list_genre'] + info['list_tag']  ).strip(),
        axis=1
    )

    # # * : 언팩킹, js의 ...과 같음
    # # 배열을 하나씩 분리해 주는것
    # # *[1,2,3] => 1,2,3
    # result['content_text'] = result.apply(
    #     lambda info : " ".join( info['title'] , *info['list_genre'] , *info['list_tag']  ).strip(),
    #     axis=1
    # )


    # reset_index : pandas 내부 index를 재정리
    # drop=True 를 안하면 새로 추가되버린다 그래서 엉망인건 버려라
    return result.reset_index(drop=True)


@router.get('/make/content')
def content():
    dataFrame = makeContent()
    return dataFrame.head(10).to_dict(orient="records")

# 한줄로 만들어진 content_text를 적당히 쪼개고 겹쳐서 chunk로 만들기
def makeChunk() :
    size_chunk = 50
    overlap:int = 15
    # chunks = []
    # 자료형을 미리 지정하기
    # Any : 아무형태나
    chunks : list[dict[str, Any]] = []

    dataFrame = makeContent()
    content = dataFrame.to_dict(orient="records")

    step = size_chunk - overlap
    for idx_content, info in enumerate(content) :
        text = info.get('content_text', '').strip()
        if not text :
            continue

        # for idx_start in range(0, len(text), step):
        for idx, idx_start in enumerate( range(0, len(text), step) ):
            chunk = text[idx_start : idx_start+size_chunk]
            if chunk :
                chunks.append({
                    'index': idx_content,
                    'movieId': int(info['movieId']),
                    'title': str(info['title']),
                    'genres': list(info['list_genre']),
                    'tags': list(info['list_tag']),
                    'content': chunk,
                    'chunk_index': idx,
                })

    return chunks

@router.get("/make/chunk")
def chunk():
    # dict 중에서 앞에 10개만
    return makeChunk()[0:10]


@router.get("/make/embedding/gemini")
def embedding():
    target = makeChunk()[0:10]
    actions = util.embedding_with_gemini(target)

    return actions
@router.get("/make/embedding/openai")
def embedding():
    target = makeChunk()[:10]
    print(len(target))
    actions = util.embedding_with_openai(target)

    return actions

@router.get('/es/health')
def health():
    return {'msg': util.es.ping()}

@router.post('/es/bulk')
def bulk():
    # target = makeChunk()[0:10]
    target = makeChunk()
    # actions = util.embedding_with_gemini(target)
    actions = util.embedding_with_openai(target)

    # 1. 만약에 엘라스틱서치에 인덱스가 없다면 새로 만들기
    # 있으면 삭제하기
    if util.es.indices.exists(index=os.getenv('ES_INDEX')) :
        util.es.indices.delete(index=os.getenv('ES_INDEX'))

    # 없으면 create table
    if not util.es.indices.exists(index=os.getenv('ES_INDEX')) :
        '''
        # 기본 chunk 구조
        {
            'index': idx_content,
            'movieId': int(info['movieId']),
            'title': str(info['title']),
            'genres': list(info['list_genre']),
            'tags': list(info['list_tag']),
            'content': chunk,
            'chunk_index': idx,

            # util에서 추가
            'embedding' : content의 벡터
        }
        
        '''
        mappings = {
            'properties': {
                'index': {'type': 'integer'},
                'movieId': {'type': 'integer'},
                'title': {'type': 'text'}, # keyword: 완벽히 같은 단어 검색 용
                'genres': {'type': 'keyword'},
                'tags': {'type': 'text'},
                'content': {'type': 'text'}, # text: 형태소를 이용한 유연한 검색 용
                'chunk_index': {'type': 'integer'},
                'embedding': {
                    'type': 'dense_vector',
                    'dims': 768
                },
            }
        }

        util.es.indices.create(
            index=os.getenv('ES_INDEX'),
            mappings=mappings
        )

    # 2. bulk로 넣기
    success, errors = helpers.bulk(
        util.es,
        actions,
        stats_only=False # 성공, 실패 숫자와 메세지
    )
    return {
        'msg':{
            'succ': success,
            'errors': errors
        }
    }

def search_movies(keyword: str, size: int = 10) :
    response = util.es.search(
        index=os.getenv('ES_INDEX'),
        query={
            'multi_match':{
                'query': keyword,
                'type':'best_fields',
                # 'fields': ['title', 'genres', 'tags', 'content'], # ^2 가중치
                'fields': ['title^5', 'genres^2', 'tags^2', 'content'], # ^2 가중치
            }
        },
        size=size
    )

    return response

@router.get('/es/select/multi_match')
def multi_match(keyword, size=10):
    response = search_movies(keyword, size)

    return {
        'msg': util.formatter(response)
    }


def term_movieId(ids: list) :
    # term : 키워드     where id = 1
    # terms : 리스트    where id in (1,2,3)
    response = util.es.search(
        index=os.getenv('ES_INDEX'),
        query={
            'terms':{
                'movieId': ids,
            }
        },
        size=len(ids)*5
    )

    return response

@router.get('/es/select/terms')
def terms(ids:list = Query(...)):
    response = term_movieId(ids)
    return {
        'msg': util.formatter(response)
    }

#####################################
# 추천 시스템
#####################################

@router.get('/recommand/test/counter')
def test_counter():
    str = 'hello world'
    print(Counter(str))

    list_counter = ['hi', 'hey', 'hi', 'hello', 'hi', 'aloha', 'hey']
    print(Counter(list_counter))

    food_counter = Counter()
    list_food = ['김밥', '달빵', '마라탕', '김밥', '김밥', '달빵']
    for food in list_food:
        food_counter.update(food)
    print(1, food_counter)

    food_counter2 = Counter()
    for food in [list_food]:
        food_counter.update(food)
    print(2, food_counter)

    favorite_foods = [
        ['밥', '치킨'],
        ['산낙지', '육회', '광어회'],
        ['밥', '라면', '짜장면'],
        ['햄버거', '라면', '밥']
    ]

    food_counter3 = Counter()
    for foods in favorite_foods:
        food_counter3.update(foods)
    print(food_counter3)

# CBF 콘텐츠 기반 필터링 Content-Based Filtering
# "내가 뭘 좋아했지?"
def content_based_filtering(list_movieId: list):
    selected = term_movieId(list_movieId)

    # return selected

    genre_counter = Counter()
    tag_counter = Counter()
    for hit in selected['hits']['hits']:
        source = hit['_source']
        print(source)
        genre_counter.update(source.get('genres', []))
        tag_counter.update(source.get('tags', []))

    print('genre_counter', genre_counter)
    print('tag_counter', tag_counter)

    max = 5

    # 장르와 태그를 각각 집계한 뒤 : Counter
    # 빈도가 높은 특성부터 검색어에 반영
    # most_common : 기본값 None, 모두 다
    # most_common의 리턴은 내용과 숫자가 나옴
    # 사용하지 않는 변수는 보통 _로만 표시
    terms_genre = [term for term, count in genre_counter.most_common(max)]

    # terms_genre = []
    # for term, count in genre_counter.most_common(max):
    #     term.append(term)

    terms_tag = [term for term, count in tag_counter.most_common(max)]

    # 리스트는 +로 합칠 수 있는데 하나씩 더해 나갈 때 마다 메모리를 차지
    terms = terms_genre + terms_tag

    terms = []
    terms.extend(terms_genre)
    terms.extend(terms_tag)

    # 단점
    # 중복 데이터가 있을 수 있음
    # " ".join(terms)
    # 그래서 set에 넣어보자
    # 그런데 순서를 보장하지 않음
    # " ".join(set(terms))
    # 나는 순서를 유지하면서 중복을 제거하고 싶음
    # dict.fromkeys()를 사용하면 됨
    # [a,b,a] >>>> {a: None, b: None}
    # 이걸 join하면 key만 빼올 수 있음
    query = ' '.join(dict.fromkeys(terms))
    response = search_movies(query)

    return response

@router.get('/recommand/cbf')
def cbf(list_movieId: list[int] = Query(...)):
    response = content_based_filtering(list_movieId)

    return response['hits']['hits']

test_indices = []

def split_train_test(test_size: float = 0.2):
    '''
        과거 평점을 학습시키고 미래 평점으로 평가하자
        test_size: 미래 평점의 비율(정답 데이터의 비율)
    
        사용자 별로
        최신 평점은 평가용
        과거 평점은 학습용

        평점이 한 건 뿐인 사용자는 학습 데이터에만 둠
        만약에 timestamp가 같으면 원본 행 순서로 정렬
    '''

    # 평점 파일 읽기
    frame_ratings = util.load_csv('ratings.csv')

    # 원본 유지를 위해
    data = frame_ratings.copy()

    # 원본의 순서대로 줄 번호 먹이기
    data['original_order'] = range(len(data))

    # timestamp를 숫자 타입으로 변경
    # errors='coerce': 변경이 안 되는 건 NaN으로 강제로 변경
    # errors='ignire': 변경 실패 시 원본 유지
    # errors='raise': ValueError 발생하고 즉시 중단
    valid_data = pd.to_numeric( data['timestamp'], errors='coerce' )

    # N/A가 아닌 것만 뽑아줌
    # data[ True/False ] >>>> 참인 행(row 또는 document)만 변환
    valid_data = data[data['timestamp'].notna()].copy()

    # 시간이 N/A 즉 비어있는 것만 뽑아줌
    no_time = data[data['timestamp'].isna()].copy()

    # userId가 같은 데이터끼리 group by
    # sort에 기본값은 True >> userId로 정렬하지 않고 원래 등장 순서를 유지
    # 원래 id, value 반환인데 id는 안 쓸 거라서
    for _, group in valid_data.groupby('userId', sort=False):

        # 평점을 하나만 준 사용자는 건너뛰기
        # 지금은 학습과 정답 데이터를 나누는 거라
        if len(group) <=1 :
            continue

        # 과거와 미래를 나누기 위해
        # timestamp 기준으로 정렬
        # 같은 게 있다면 original_order 기준으로 정렬해라
        # kind stable: 그래도 같은 게 있다면 정렬 전 순서 유지
        # kind에 사용할 수 있는 것
        # quicksort(기본값), mergesort, heapsort, stable
        # 오름차순
        ordered = group.sort_values(['timestamp', 'original_order'], kind='stable')

        # 전체 데이터 중 test_size 비율로 뽑았음
        # 0.4 등의 결과를 1로 만듬
        test_count = math.ceil(len(ordered) * test_size)
        if test_count < 1:
            test_count - 1

        if test_count > len(ordered) - 1:
            test_count = len(ordered) -1

        # max: 둘 중에 큰 값을 돌려줌
        # 최소 값을 지정할 때 사용
        max(1, test_count)

        # min : 둘 중에 작은 값을 돌려줌
        # 최대 값을 지정할 때 사용
        min(test_count, 3)

        test_count = min(len(ordered) -1, max(1, math.ceil(len(ordered) * test_size)))

        # tail : 끝에서 몇 개
        # 미리 시간 오름차순으로 정렬 해 두어서 최신 데이터는 끝에 있음
        # index만 모음 - 나중에 학습 데이터 분리할 때 사용하려고
        test_indices.extend(ordered.tail(test_count).index.tolist())

    # 테스트 할 데이터의 index는 모아둔 상태
    # 실제 테스트 데이터 추출
    # 학습 데이터 추출