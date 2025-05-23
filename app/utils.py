from typing import Dict, Any, List, Optional
from .data_loader import stock_data

def get_stock_by_symbol(symbol: str) -> Optional[Dict[str, Any]]:
    """Get stock data by symbol."""
    return stock_data.get(symbol.upper())

def get_stocks_by_industry(industry: str) -> List[Dict[str, Any]]:
    """Get all stocks in a specific industry."""
    return [
        stock for stock in stock_data.values() 
        if stock.get("Stock Industry") and stock["Stock Industry"].lower() == industry.lower()
    ]

def search_stocks(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    """Search stocks by symbol or company name."""
    results = []
    query = query.lower()
    
    for symbol, data in stock_data.items():
        if query in symbol.lower() or (data.get("shortName") and query in data["shortName"].lower()):
            results.append({"symbol": symbol, **data})
            if len(results) >= limit:
                break
                
    return results

def get_all_fields() -> List[str]:
    """Get all available field names from the data."""
    if not stock_data:
        return []
    
    # Get fields from the first stock
    first_stock = next(iter(stock_data.values()))
    return list(first_stock.keys())