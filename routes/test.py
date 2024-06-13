from fastapi import APIRouter, Request, Depends, HTTPException, Response
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
    data = "Okay"
    return Response(content=data, media_type="text/plain")

@router.post("/post_test")
async def post_test(request: Request, db: Session = Depends(get_session)):
    client_host = request.client.host
    body = await request.body()
    create_log(db=db, ip_address=client_host, data=body)
    data = "Okay"
    return Response(content=data, media_type="text/plain")
