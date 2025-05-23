from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List, Dict, Any
from .models import StockResponse, IndustryResponse, SearchResponse, FieldListResponse
from .utils import (
    get_stock_by_symbol, 
    get_stocks_by_industry, 
    search_stocks,
    get_all_fields
)

app = FastAPI(
    title="Stock Data API",
    description="API for accessing stock market data",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "email": "your.email@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

# CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to the Stock Data API",
        "endpoints": {
            "get_stock": "/stocks/{symbol}",
            "get_industry": "/industries/{industry}",
            "search_stocks": "/search",
            "list_fields": "/fields"
        }
    }

@app.get("/stocks/{symbol}", response_model=StockResponse, tags=["Stocks"])
async def get_stock(symbol: str):
    """Get stock data by symbol"""
    stock = get_stock_by_symbol(symbol)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock

@app.get("/industries/{industry}", response_model=IndustryResponse, tags=["Industries"])
async def get_industry(industry: str):
    """Get all stocks in a specific industry"""
    stocks = get_stocks_by_industry(industry)
    if not stocks:
        raise HTTPException(status_code=404, detail="No stocks found in this industry")
    return {
        "industry": industry,
        "stocks": stocks,
        "count": len(stocks)
    }

@app.get("/search", response_model=SearchResponse, tags=["Search"])
async def search(
    query: str = Query(..., min_length=1, description="Search term for stock symbol or name"),
    limit: int = Query(10, gt=0, le=100, description="Maximum number of results to return")
):
    """Search stocks by symbol or company name"""
    results = search_stocks(query, limit)
    return {
        "results": results,
        "count": len(results)
    }

@app.get("/fields", response_model=FieldListResponse, tags=["Metadata"])
async def list_fields():
    """List all available data fields"""
    fields = get_all_fields()
    return {
        "fields": fields,
        "count": len(fields)
    }