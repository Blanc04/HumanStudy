from elasticsearch import Elasticsearch, helpers
import requests
from fastapi import APIRouter
from dotenv import load_dotenv

load_dotenv()
from config import ALIO_API_KEY, ELASTIC_ENDPOINT

router = APIRouter()

es = Elasticsearch(
    ELASTIC_ENDPOINT
)

# print('ALIO_API_KEY 존재:', ALIO_API_KEY is not None)
# print('ALIO_API_KEY 길이:', len(ALIO_API_KEY) if ALIO_API_KEY else 0)

# GET /jobs?keyword=검색어
# 형태로 요청할 수 있는 API
@router.get('/jobs')
def get_jobs(keyword: str):

    # 청년 일자리 채용정보 목록 Open API 주소
    url = 'https://opendata.alio.go.kr/new/v1/recruit/list.do'

    # ALIO API에 전달할 Query Parameter
    params = {
        # 발급받은 인증키
        'serviceKey': ALIO_API_KEY,
        # 응답 형식을 JSON으로 요청
        'resultType': 'json',
        # 조회할 페이지 번호
        'pageNo': 1,
        # 한 번에 가져올 데이터 개수
        'numOfRows': 500
    }

    # HTTP 요청에 같이 전달할 Header
    headers = {
        # JSON 형태의 응답을 원한다고 서버에 알람
        'accept': 'application/json',
        # ALIO Swagger에서 사용하는 헤더
        'swaggerType': 'Y'
    }

    # HTTP 요청에 같이 전달할 Header
    response = requests.post(
        url,
        params=params,
        headers=headers
    )

    # HTTP 요청 자체가 실패한 경우 예외 발생
    response.raise_for_status()

    # ALIO가 반환한 JSON 데이터를
    # Python 딕셔너리로 변환
    data = response.json()

    jobs = data.get('result', [])

    # 엘라스틱서치 저장
    actions = []

    # ALIO에서 받아온 채용공고를 하나씩 처리
    for job in jobs:
        # Elasticsearch bulk 저장 형식으로 변환
        actions.append({
            # 저장할 Elasticsearch 인덱스 이름
            '_index': 'alio_jobs',

             # 채용공고 고유번호를 Elasticsearch 문서 ID로 사용
            '_id': job['recrutPblntSn'],

            # 실제로 Elasticsearch에 저장할 내용
            '_source': job
        })

    # 저장할 데이터가 하나 이상 있을 때만 실행
    if actions:
        # actions에 담긴 모든 채용공고를
        # Elasticsearch에 한 번에 저장
        helpers.bulk(es, actions)

    # 검색
    keyword = keyword.strip().lower()

    filtered_jobs = []

    # 가져온 채용공고를 하나씩 검사
    for job in jobs:

        # 채용공고 제목
        title = job.get('recrutPbancTtl', '')

        # 기관명
        inst_name = job.get('instNm', '')

        # NCS 직무분야 이름
        ncs_name = job.get('ncsCdNmLst', '')

        # 제목에서 기관명 제거
        search_title = title.replace(inst_name, '')

        if (
            keyword in search_title.lower()
            or keyword in ncs_name.lower()
        ):
            filtered_jobs.append(job)

    return {
        'keyword': keyword,
        'count': len(filtered_jobs),
        'result': filtered_jobs
    }