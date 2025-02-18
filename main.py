from volcenginesdkarkruntime import Ark
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from typing import List, Dict, Any

app = FastAPI(
    title="Stock Analysis API",
    description="API for analyzing stock data using AI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# 初始化客户端
client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)

class NewsItem(BaseModel):
    date: str
    title: str

class StockData(BaseModel):
    """
    股票数据模型，允许任意字段
    """
    class Config:
        extra = "allow"  # 允许任意额外字段

class StockDataList(BaseModel):
    """
    股票数据列表
    """
    stocks: List[Dict[str, Any]]  # 使用Dict[str, Any]来允许任意key-value结构

def get_stock_analysis(content: str) -> str:
    """
    获取股票分析结果
    Args:
        content: 需要分析的股票数据内容
    Returns:
        生成的分析结果
    """
    response_text = ""
    stream = client.chat.completions.create(
        model="ep-20250218214527-wcwtg",
        messages=[
            {"role": "system", "content": "你是一个量化股票数据分析师，我会给你一些json数据，你从这个数据中帮我分析当前股票的利好利空情况, 如果利空到利好是0-10分，请你基于数据的分析给我一个客观分数,结果请用中文来回答我"},
            {"role": "user", "content": content}
        ],
        stream=True
    )
    for chunk in stream:
        if not chunk.choices:
            continue
        delta_content = chunk.choices[0].delta.content
        if delta_content:
            response_text += delta_content
    return response_text

@app.post("/analyze")
async def analyze_stock(stock_data_list: StockDataList):
    """
    分析股票数据的API端点
    """
    try:
        # 将Pydantic模型转换为JSON字符串
        content = stock_data_list.model_dump_json()
        result = get_stock_analysis(content)
        return {"analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    """
    API根路径
    """
    return {
        "status": "ok",
        "message": "Stock Analysis API is running",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=7777
    )
