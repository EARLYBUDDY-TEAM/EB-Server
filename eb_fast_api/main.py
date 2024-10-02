import time
from fastapi import FastAPI, Request, Response


app = FastAPI()


from eb_fast_api.domain.auth.register.sources import register_routers
from eb_fast_api.domain.auth.login.sources import login_router
from eb_fast_api.domain.map.place.sources import place_router
from eb_fast_api.domain.map.route.sources import route_router
from eb_fast_api.domain.schedule.sources import schedule_router
from eb_fast_api.domain.token.sources import token_router
from eb_fast_api.domain.home.sources import home_router


app.include_router(register_routers.router)
app.include_router(login_router.router)
app.include_router(place_router.router)
app.include_router(route_router.router)
app.include_router(schedule_router.router)
app.include_router(token_router.router)
app.include_router(home_router.router)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    request_body = await request.body()
    print(f"REQUEST_URL : {request.url}")
    print(f"REQUEST_BODY : {request_body}")

    response = await call_next(request)

    process_time = time.time() - start_time
    print(f"PROCESS_TIME : {process_time}")
    response_body = b""
    async for chunk in response.body_iterator:
        response_body += chunk
    print(f"RESPONSE_BODY : {response_body.decode()}")
    return Response(
        content=response_body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type,
    )


@app.get("/")
def read_root():
    return "Hello EarlyBuddy Fast API !!!"


if __name__ == "__main__":
    import uvicorn
    from eb_fast_api.database.sources.database import EBDataBase

    EBDataBase.initialize()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
