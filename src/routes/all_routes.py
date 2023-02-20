
from fastapi import APIRouter
from src.routes.a import router as ggggggg

router = APIRouter()

router.include_router(ggggggg)
