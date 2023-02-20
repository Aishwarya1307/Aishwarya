# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware

from src.routes.all_routes import router as all_routes

app = FastAPI(
    title="tagsmart APIV2",

)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.include_router(all_routes)

if __name__ == '__main__':
    run("main:app", host="0.0.0.0", port=5017, reload=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
