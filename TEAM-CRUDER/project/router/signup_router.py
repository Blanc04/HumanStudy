from fastapi import Request, Form
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from passlib.context import CryptContext
from pw_utils import hash_password

from sqlmodel import Session
from database import get_session
from DTO.UserDTO import User

router = APIRouter()
templates = Jinja2Templates(directory='templates/')


# =========================================================
# static 폴더 연결
# =========================================================

router.mount(
    "/assets",
    StaticFiles(directory="assets"),
    name="assets"
)


##########################################################
# 회원가임 페이지 접속 라우팅
########################################################## 

pw = CryptContext(
    schemes=['argon2'],
    deprecated='auto'
)

@router.get('/jobgogo/signup')
def jobgogo(
    request: Request
):
    return templates.TemplateResponse(
        request,
        'signup.html'
    )

@router.post('/signup/idcheck')
async def signupIDChk(
    request: Request,
    session: Session = Depends(get_session)
):
    data = await request.json()
    request.session.pop(
        'signup_checked_id',
        None
    )
    signupUserId = data.get(
        'signupUserId',
        ''
    ).strip()
    if (
        signupUserId == ''
        or len(signupUserId) > 12
        or not signupUserId.isalnum()
    ):
        return {
            'result': '아이디 형식을 확인해 주세요.',
            'check': 'failed'
        }
    sql_idcheck = text('''
        select user_id
        from user
        where user_id = :user_id
    ''')
    result_idcheck = session.execute(
        sql_idcheck,
        {
            'user_id': signupUserId
        }
    )
    idcheck = (
        result_idcheck
        .mappings()
        .fetchone()
    )
    if idcheck is None:
        request.session[
            'signup_checked_id'
        ] = signupUserId
        return {
            'result': '사용 가능한 아이디입니다.',
            'check': 'success'
        }
    return {
        'result': '이미 사용 중인 아이디입니다.',
        'check': 'failed'
    }

@router.post('/signup')
def signupData(
    request: Request,
    user_id: str = Form(),
    user_pw: str = Form(),
    user_pw_confirm: str = Form(),
    user_name: str = Form(),
    user_home: str = Form(),
    user_email: str = Form(),
    user_phone: str = Form(),
    session: Session = Depends(get_session)
):
    print('''
    ========================================
    /signup : 회원가입 실행
    ========================================
    ''')
    user_id = user_id.strip()
    user_name = user_name.strip()
    user_home = user_home.strip()
    user_email = user_email.strip()
    user_phone = user_phone.strip()
    # 휴대폰 번호에서 하이픈 제거
    user_phone = user_phone.replace('-', '')
    # 010으로 시작하는 숫자 11자리 검사
    if (
        not user_phone.isdigit()
        or len(user_phone) != 11
        or not user_phone.startswith('010')
    ):
        return RedirectResponse(
            url='/signup',
            status_code=303
        )
    # 필수 입력값 검사
    if (
        user_id == ''
        or user_pw == ''
        or user_name == ''
        or user_home == ''
        or user_email == ''
        or user_phone == ''
    ):
        return RedirectResponse(
            url='/signup',
            status_code=303
        )
    # 비밀번호 확인
    if user_pw != user_pw_confirm:
        return RedirectResponse(
            url='/signup',
            status_code=303
        )
    
    # 중복확인을 받은 아이디와 제출한 아이디 비교
    checked_user_id = request.session.get(
        'signup_checked_id'
    )

    if checked_user_id != user_id:
        return RedirectResponse(
            url='/signup',
            status_code=303
        )
    
    # 회원가입 직전 아이디 중복 재검사
    sql_idcheck = text('''
        select user_id
        from user
        where user_id = :user_id
    ''')

    result_idcheck = session.execute(sql_idcheck, {
        'user_id': user_id
    })

    idcheck = result_idcheck.mappings().fetchone()
    if idcheck is not None:
        request.session.pop('signup_checked_id', None)
        return RedirectResponse(
            url='/signup',
            status_code=303
        )
    
    sql_signup = text('''
        insert into user (
            user_id,
            user_pw,
            user_name,
            user_email,
            user_phone,
            user_home
        )
        values (
            :user_id,
            :user_pw,
            :user_name,
            :user_email,
            :user_phone,
            :user_home
        )
    ''')
    session.execute(sql_signup, {
        'user_id': user_id,
        'user_pw': hash_password(user_pw),
        'user_name': user_name,
        'user_email': user_email,
        'user_phone': user_phone,
        'user_home': user_home
    })

    session.commit()
    # 회원가입 완료 후 중복확인 기록 제거
    request.session.pop('signup_checked_id', None)
    return RedirectResponse(
        url='/login',
        status_code=303
    )