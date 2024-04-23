from typing import Optional
from fastapi import FastAPI

# from database.database import engine
# from database import models
# models.Base.metadata.create_all(bind=engine)

# Path
from sys import path as sys_path
from pathlib import Path
sys_path.append(Path(__file__))
from database.database import engine
from database import models

app = FastAPI()

# from domain.user import user_routers
# app.include_router(user_routers.router)

hello_world = 'Hellow World!'

@app.get("/")
def read_root():
    return hello_world

# if __name__ != '__main__':
#     hello_world = __name__

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {
#         "item_id": item_id,
#         "q": q,
#     }
