# /docs: /docs접속시 API 문서 자동 생성
# redocs: 문서 변경

from fastapi import FastAPI
app = FastAPI()

from fastapi.responses import FileResponse 

# 페이지 접속시 메시지 출력
@app.get("/")
def print_message():
    return FileResponse('index.html')

@app.get("/data")
def print_message():
    return {'hello':1234} 

# 유저에게 데이터 수신
from pydantic import BaseModel
class your_info(BaseModel):
    name : str
    phone : str

@app.post("/send")
def info(data : your_info):
    print(data)
    return '입력이 완료되었습니다.'