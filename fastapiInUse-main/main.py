from pydantic import BaseModel
from concurrent.futures.process import _python_exit
from unicodedata import name
from fastapi.responses import FileResponse
from fastapi import FastAPI
app = FastAPI()


class Model(BaseModel):
    name: str
    phone: int


@app.get | ("/")
async def 작명():
    return FileResponse('index.html')


@app.post("/send")
def 작명(data: Model):
    print(data)
    return '전송완료'
