from fastapi import APIRouter

app = APIRouter(
    prefix="/auth",
)

@app.get("/login")
async def login_test():
    return "login test"