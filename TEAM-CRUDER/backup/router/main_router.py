from fastapi import Request, Form
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

from sqlmodel import Session, text, select
from DTO.BookmarkDTO import BookMark

from database import get_session


router = APIRouter()
templates = Jinja2Templates(directory='templates/')


# =========================================================
# assets 폴더 연결
# =========================================================

router.mount(
    "/assets",
    StaticFiles(directory="assets"),
    name="assets"
)

# =========================================================
# static 폴더 연결
# =========================================================

router.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


##########################################################
# 메인 페이지 접속 라우팅
########################################################## 

@router.get('/jobgogo')
def jobgogo(
    request: Request,
    selectNum: str = '0',
    keyword: str = "",
    session: Session = Depends(get_session)
):
    print('메인 페이지 접속 성공!')
    print('키워드 나오냐?', keyword)
    print('셀렉트 나오냐?', selectNum)

    search_keyword = f'%{keyword}%'

    try:
        # 1. 채용공고를 가져오기 위한 SQL문
        sql_jobs_notice = text('''
            SELECT *
            FROM jobs
            WHERE ongoing_yn = 'Y'
            AND (
                recrut_pbanc_ttl LIKE :keyword
                OR inst_nm LIKE :keyword
                OR work_rgn_nm_lst LIKE :keyword
            )
            ORDER BY pbanc_bgng_ymd DESC
            LIMIT :selectNum
        ''')

        # 2. 채용공고 가져오기
        result = session.exec(
            sql_jobs_notice,
            params={
                'keyword': search_keyword,
                'selectNum': int(selectNum)
            }
        )

        jobs = result.mappings().fetchall()

        # 3. 현재 로그인한 회원 ID 가져오기
        user_id = request.session.get("user_id")

        # 4. 북마크 목록 초기화
        bookmarked_job_ids = set()

        # 5. 로그인한 회원만 북마크 조회
        if user_id:
            bookmark_result = session.exec(
                select(BookMark.recrut_pblnt_sn).where(
                    BookMark.user_id == user_id
                )
            )

            bookmarked_job_ids = set(bookmark_result.all())

        # 6. HTML 렌더링
        return templates.TemplateResponse(
            request=request,
            name='main.html',
            context={
                "jobs": jobs,
                "keyword": keyword,

                # 북마크 데이터
                "bookmarked_job_ids": bookmarked_job_ids,

                # 로그인 세션
                "user_id": user_id,
                "user_name": request.session.get("user_name"),
                "user_status_id": request.session.get("user_status_id")
            }
        )

    except Exception as e:
        print('에러에러', e)
        raise   
    
    
