from fastapi import FastAPI
from app.api import users, files

app = FastAPI()

# 注册路由
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(files.router, prefix="/files", tags=["files"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Poetry!"}
