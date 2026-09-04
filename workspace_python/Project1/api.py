from fastapi import FastAPI, Cookie, Request, Response
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

@app.get('/main')
async def main(
    request: Request,
    response: Response,
):
    print('no')




if __name__=="__main__":
    import uvicorn
    uvicorn.run('api:app', port=8000, reload=True, host="0.0.0.0")