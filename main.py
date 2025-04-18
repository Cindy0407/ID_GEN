from fastapi import FastAPI
from app.api.project.controller.route import router as project_router
import redis
import os

app = FastAPI()

# 應用程式啟動時初始化
@app.on_event("startup")
def startup():
    app.state.redis_client = redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        decode_responses=True  # 建議設 True，回傳 string 而不是 bytes
    )

@app.on_event("shutdown")
def shutdown():
    app.state.redis_client.close()

app.include_router(project_router)
