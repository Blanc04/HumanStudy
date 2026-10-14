from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select, text

from database import get_session
from DTO.BookmarkDTO import BookMark


router = APIRouter()
templates = Jinja2Templates(directory='templates/')


@router.get('/jobgogo/mypage/bookmarks')
def bookmark_page(
    request: Request,
    session: Session = Depends(get_session)
):
    user_id = request.session.get('user_id')

    if not user_id:
        return RedirectResponse(
            url='/jobgogo/login',
            status_code=303
        )

    sql = text('''
        SELECT
            j.recrut_pblnt_sn,
            j.recrut_pbanc_ttl,
            j.inst_nm,
            j.recrut_se_nm,
            j.work_rgn_nm_lst,
            j.pbanc_bgng_ymd,
            j.pbanc_end_ymd,
            j.src_url
        FROM bookmark b
        JOIN jobs j
          ON b.recrut_pblnt_sn = j.recrut_pblnt_sn
        WHERE b.user_id = :user_id
        ORDER BY j.pbanc_end_ymd ASC
    ''')

    result = session.exec(
        sql,
        params={
            'user_id': user_id
        }
    )

    bookmarks = result.mappings().all()

    return templates.TemplateResponse(
        request=request,
        name='bookmark.html',
        context={
            'bookmarks': bookmarks,
            'user_id': user_id,
            'user_name': request.session.get('user_name'),
            'user_status_id': request.session.get('user_status_id')
        }
    )

@router.post('/jobgogo/bookmark/{recrut_pblnt_sn}')
def toggle_bookmark(
    recrut_pblnt_sn: str,
    request: Request,
    session: Session = Depends(get_session)
):
    user_id = request.session.get('user_id')

    # 비로그인
    if not user_id:
        return JSONResponse(
            status_code=401,
            content={
                'success': False,
                'message': '로그인이 필요합니다.'
            }
        )

    try:
        # 현재 북마크 여부 확인
        statement = select(BookMark).where(
            BookMark.user_id == user_id,
            BookMark.recrut_pblnt_sn == recrut_pblnt_sn
        )

        bookmark = session.exec(statement).first()

        # 이미 찜한 공고 → 찜 해제
        if bookmark:
            session.delete(bookmark)

            # 실제 DB 반영
            session.commit()

            return {
                'success': True,
                'bookmarked': False
            }

        # 찜하지 않은 공고 → 찜 추가
        bookmark = BookMark(
            user_id=user_id,
            recrut_pblnt_sn=recrut_pblnt_sn
        )

        session.add(bookmark)

        # 실제 DB 반영
        session.commit()

        return {
            'success': True,
            'bookmarked': True
        }

    except Exception as e:
        session.rollback()

        print(
            '북마크 처리 오류:',
            repr(e)
        )

        return JSONResponse(
            status_code=500,
            content={
                'success': False,
                'message': '북마크 처리 중 오류가 발생했습니다.'
            }
        )