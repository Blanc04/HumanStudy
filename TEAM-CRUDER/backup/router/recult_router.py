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


##########################################################
# 메인 페이지 접속 라우팅
########################################################## 

@router.get('/jobgogo/recult')
def recult(
    request: Request,
    keyword : str = "" ,
    session: Session = Depends(get_session)
):
    print('채용 공고 페이지 접속 성공!') 
    print('키워드 나오니!',keyword)
    
    search_keyword = f'%{keyword}%' 
    
    # 채용 공고를 가져오는 부분
    # 채용공고를 가져오기 위한 SQL문
    try:
           sql_jobs_notice = text('''
               SELECT *
               FROM jobs
               WHERE ongoing_yn = 'Y'
               and(
                   recrut_pbanc_ttl like :keyword 
                   or inst_nm like :keyword 
                   or work_rgn_nm_lst like :keyword 
               )
               ORDER BY pbanc_bgng_ymd DESC
               limit 9
           ''')
   
           # 채용공고 가져오기
           result=session.exec(sql_jobs_notice,params={'keyword':search_keyword})
           jobs=result.mappings().fetchall()

           user_id = request.session.get("user_id")

           bookmarked_job_ids = set()

           if user_id:
            bookmark_result = session.exec(
                select(BookMark.recrut_pblnt_sn).where(
                    BookMark.user_id == user_id
                )
            )

            bookmarked_job_ids = set(bookmark_result.all())
           
           return templates.TemplateResponse(
               request=request,
               name='recult.html',
               context={
                   "jobs": jobs,
                   "keyword" : search_keyword,

                   "bookmarked_job_ids": bookmarked_job_ids,
   
                   # 로그인 세션
                   "user_id": request.session.get("user_id"),
                   "user_name": request.session.get("user_name"),
                   "user_status_id": request.session.get("user_status_id")
               }
           )
    except Exception as e:
           print('에러에러', e)    
       