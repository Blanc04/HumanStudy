from elasticsearch import Elasticsearch, helpers
import requests
from fastapi import APIRouter
from sqlalchemy import text
from datetime import datetime,date
from config import APIS_API_KEY, ELASTIC_ENDPOINT
from sqlalchemy import text
from fastapi import FastAPI, Depends
from sqlmodel import Session


# 여행정보 관련 API를 모아두는 라우터
router = APIRouter(tags=['여행정보 관련 라우터'])
session = requests.Session()

def fetch_trip():
    url = 'https://apis.data.go.kr/B551011/KorService2'

    # APIS API에 전달할 Query Parameter
    params = {
        # 발급받은 인증키
        'serviceKey': APIS_API_KEY,
        # 필수: IOS, AND, WIN, ETC 중 선택
        "MobileOS": "ETC",
        # 필수: 서비스명(영문 권장)
        "MobileApp": "FLOWER",
        # 응답 형식을 JSON으로 요청
        '_type': 'json',
        # 조회할 페이지 번호
        'pageNo': 1,
        # 한 번에 가져올 데이터 개수
        'numOfRows': 1000
    }

    # HTTP 요청에 같이 전달할 Header
    headers = {
        # JSON 형태의 응답을 원한다고 서버에 알림
        'accept': 'application/json',
        # APIS Swagger에서 사용하는 헤더
        'swaggerType': 'Y'
    }

    # APIS Open API에 POST 방식으로 채용정보 요청
    response = requests.post(
        url,
        params=params,
        headers=headers
    )

    # HTTP 요청 자체가 실패한 경우 예외 발생
    response.raise_for_status()

    # APIS가 반환한 JSON 데이터를
    # Python 딕셔너리로 변환
    data = response.json()

    # result가 없을 경우 빈 리스트 반환
    return data.get('result', [])

@router.get("/trip")
def get_trip():
    return fetch_trip()

@router.post("/trip")
def post_trip():
    return fetch_trip()