from fastapi import FastAPI

from eb_server.database.database import engine
from eb_server.database import models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

from eb_server.domain.register.sources import register_routers
app.include_router(register_routers.router)

@app.get("/")
def read_root():
    return 'Hellow World!'