from fastapi import FastAPI

from eb_server.database.database import engine
from eb_server.database import models
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

from eb_server.domain.auth.register.sources import register_routers
from eb_server.domain.auth.login.sources import login_router
app.include_router(register_routers.router)
app.include_router(login_router.router)

@app.get("/")
def read_root():
    return 'Hellow World!'


# import traceback

# ...

# async def catch_exceptions_middleware(request: Request, call_next):
#     try:
#         return await call_next(request)
#     except Exception as e:
#         print(traceback.format_exc())
#         raise e


# app.middleware('http')(catch_exceptions_middleware)