from fastapi import APIRouter, Request, Depends, HTTPException, Response, Form
from sqlalchemy.orm import Session
from database.db import get_session
from database.model import create_log

router = APIRouter(
    prefix="/v1/test",
    tags=["v1_test"]
)

@router.get("/get_test")
async def get_test(request: Request, db: Session = Depends(get_session)):
    client_host = request.client.host
    create_log(db=db, ip_address=client_host)
    data = "R311100010000010030911202405181612098"
    return Response(content=data, media_type="text/plain")

@router.post("/post_test")
async def post_test(request: Request, db: Session = Depends(get_session)):
    client_host = request.client.host
    body = await request.body()
    create_log(db=db, ip_address=client_host, data=body)
    # data = "R311100010000010030911202405181612098"
    data = "R31110001000001003091120240518161209819383728463728818643875"
    return Response(content=data, media_type="text/plain")

@router.post("/form_test")
async def form_test(request: Request, db: Session = Depends(get_session), body: str = Form()):
    client_host = request.client.host
    create_log(db=db, ip_address=client_host, data=body)
    # data = "R311100010000010030911202405181612098"
    # data = "R31110001000001003091120240518161209819383728463728818643875"
    data = "C311100010000010030900202405181612001"
    str_len = len(data)
    fin_len = 60 - str_len
    data = data.ljust(fin_len, '0')
    return Response(content=data, media_type="text/plain")
