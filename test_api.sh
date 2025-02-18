#!/bin/bash
curl -X POST http://localhost:8000/analyze \
-H "Content-Type: application/json" \
-d '{
    "stocks": [
        {
            "stock_code": "600519",
            "stock_name": "贵州茅台",
            "current_price": 1789.98,
            "change_percent": 2.35,
            "trading_volume": 892365,
            "trading_amount": 159623.45,
            "market_indicators": {
                "pe_ratio": 28.5,
                "pb_ratio": 9.8,
                "revenue_growth": 15.6,
                "profit_margin": 45.2
            },
            "recent_news": [
                {"date": "2024-02-18", "title": "公司发布新产品战略"},
                {"date": "2024-02-17", "title": "季度营收超出市场预期"}
            ]
        },
        {
            "stock_code": "000858",
            "stock_name": "五粮液",
            "current_price": 189.45,
            "change_percent": 1.25,
            "trading_volume": 456789,
            "trading_amount": 86543.21,
            "market_indicators": {
                "pe_ratio": 25.6,
                "pb_ratio": 8.2,
                "revenue_growth": 12.8,
                "profit_margin": 38.5
            },
            "recent_news": [
                {"date": "2024-02-18", "title": "五粮液扩大产能"},
                {"date": "2024-02-17", "title": "新市场开拓计划公布"}
            ]
        }
    ]
}'
