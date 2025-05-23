from typing import Optional, Dict, Any, List, Union
from pydantic import BaseModel

class StockBase(BaseModel):
    Stock_Symbol: str
    Volatility: Optional[float]
    Beta: Optional[float]
    Return_on_Investment: Optional[float]
    CAGR: Optional[float]
    Debt_to_Equity_Ratio: Optional[float]
    Latest_Close_Price: Optional[float]
    PE_Ratio: Optional[float]
    PB_Ratio: Optional[float]
    EPS: Optional[float]
    Dividend_Yield: Optional[float]
    Market_Cap: Optional[float]
    Fifty_MA: Optional[float]
    Two_Hundred_MA: Optional[float]
    RSI: Optional[float]
    MACD: Optional[float]
    Bollinger_Band: Optional[str]
    Current_Price: Optional[float]
    Percentage_Difference: Optional[float]
    Correlation_with_event: Optional[float]
    Category: Optional[str]
    Total_Score: Optional[float]
    Stock_Industry: Optional[str]
    # Add all other fields from your Excel here

class StockResponse(StockBase):
    pass

class IndustryResponse(BaseModel):
    industry: str
    stocks: List[StockResponse]
    count: int

class SearchResponse(BaseModel):
    results: List[StockResponse]
    count: int

class FieldListResponse(BaseModel):
    fields: List[str]
    count: int