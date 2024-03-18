from typing import Optional
from fastapi import FastAPI

from router import auth_router

from database.database import engine
from database import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router.app)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id,
        "q": q,
    }
