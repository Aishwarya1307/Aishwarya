from loguru import logger as logging
from src.db.alchemy import SessionLocal, engine
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
import psycopg2.extras


class Message(BaseModel):
    status_code: int
    detail: str


def get_db():
    '''
    does
    :return:
    '''
    db = SessionLocal()
    # logging.info("get_db")
    try:
        # logging.debug("yeilding db")
        yield db
    finally:
        # logging.debug("closing db")
        db.close()


def get_raw_db():
    '''
    does
    :return:
    '''
    db = engine.raw_connection()


    # logging.info("get_db")
    try:
        # logging.debug("yeilding db")
        yield db
    finally:
        # logging.debug("closing db")
        db.close()

