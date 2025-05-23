from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging
from .utils import get_stock_by_symbol
from .models import StockResponse

logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/stocks/{symbol}", response_model=StockResponse)
async def get_stock(symbol: str):
    try:
        logger.info(f"Fetching stock data for: {symbol}")
        stock = get_stock_by_symbol(symbol)
        if not stock:
            logger.warning(f"Stock not found: {symbol}")
            raise HTTPException(status_code=404, detail="Stock not found")
        return stock
    except Exception as e:
        logger.error(f"Error fetching stock {symbol}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
