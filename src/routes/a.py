from http.client import HTTPException

from fastapi import FastAPI, Depends
from typing import Optional
from fastapi import APIRouter
from loguru import logger
from sqlalchemy.orm import Session
from pydantic import BaseModel
from src.routes import get_db

router = APIRouter()
Json_ = {
    1: {
        "name": "john",
        "age ": "52",
        "city": "Pune",
        "numbers ": "58"
    }
}


class data(BaseModel):
    name: str
    age: int
    city: str
    numbers: int


@router.post('/login', tags=["Login / User Management"], )
def login_user(

        db: Session = Depends(get_db)
):
    try:

        return Json_
    except HTTPException as e:
        logger.error(f'{e}')
        raise e
    except Exception as e:
        logger.error(f'{e}')
        raise HTTPException(status_code=500, detail=f'{e}')


@router.post('/login/signup', tags=["Login / User Management"], )
def login_user(

        db: Session = Depends(get_db)
):
    try:

        return {"name": "tom"}
    except HTTPException as e:
        logger.error(f'{e}')
        raise e
    except Exception as e:
        logger.error(f'{e}')
        raise HTTPException(status_code=500, detail=f'{e}')


@router.get('/access_data', tags=["Login / User Management"], )
def login_user(

        db: Session = Depends(get_db)
):
    try:

        return {"user_name": "tom", "password": "1234"}
    except HTTPException as e:
        logger.error(f'{e}')
        raise e
    except Exception as e:
        logger.error(f'{e}')
        raise HTTPException(status_code=500, detail=f'{e}')


@router.get("/local")
def read_item(*, name: Optional[str] = None, test: int):
    #  when optional is used then that position is last in the parameters otherwise use * at the starting
    if Json_[name] not in Json_:
        raise HTTPException(status_code=404, detail="Item not found")
    return Json_


@router.post("/storedata")
def post_method(json_id: int, std: data):
    if json_id in Json_:
        return {"msg": "id is already exists"}
    Json_[json_id] = std
    return Json_[json_id]


@router.put("/update_data/")
def update_data(id_: int, json_cls: data):
    if id_ not in Json_:
        return {"Error": "id is not exists for update"}

    Json_[id_] = json_cls
    return Json_[id_]
