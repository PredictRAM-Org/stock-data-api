import pandas as pd
from pathlib import Path
from typing import Dict, Any

def load_stock_data() -> Dict[str, Dict[str, Any]]:
    """Load stock data from Excel file and return as dictionary."""
    data_path = Path(__file__).parent.parent / "data" / "merged_stock_data.xlsx"
    df = pd.read_excel(data_path)
    
    # Convert NaN values to None for JSON compatibility
    df = df.where(pd.notnull(df), None)
    
    # Convert DataFrame to dictionary with stock symbol as key
    stock_data = df.set_index("Stock Symbol").to_dict(orient="index")
    
    return stock_data

# Preload the data when module is imported
stock_data = load_stock_data()