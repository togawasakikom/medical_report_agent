from fastapi import FastAPI
from app.api.router import router

# 初始化 FastAPI 应用
app = FastAPI(
    title="AI体检报告解读助手 API",
    description="上传体检报告 -> 解析提取 -> RAG增强 -> LLM解读",
    version="1.0.0"
)

# 核心：将我们写好的路由注册进来，并加上统一的接口前缀 /api/v1
app.include_router(router, prefix="/api/v1", tags=["体检报告处理"])

@app.get("/")
async def root():
    return {"message": "欢迎使用 AI 体检报告解读助手 API，系统已启动！"}