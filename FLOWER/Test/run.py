from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from router.api_router import router as api_router
from config import SESSION_SECRET_KEY

BASE_DIR = Path(__file__).resolve().parent

router = FastAPI()

router.include_router(api_router)


router.add_middleware(
    SessionMiddleware,
    secret_key=SESSION_SECRET_KEY,
    same_site="lax",
    https_only=False
)

router.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://127.0.0.1:5500'
    ],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# 정적 파일
# router.mount(
#     "/assets",
#     StaticFiles(directory=str(BASE_DIR / "assets")),
#     name="assets"
# )

# router.mount(
#     "/static",
#     StaticFiles(directory=str(BASE_DIR / "static")),
#     name="static"
# )

@router.get('/')
def home():
    return "welcome!"

if __name__ == "__main__" :
    import uvicorn
    uvicorn.run('run:router', port=8000, reload=True, host='0.0.0.0')