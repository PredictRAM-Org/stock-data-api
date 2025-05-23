import pandas as pd
from pathlib import Path
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

def load_stock_data() -> Dict[str, Dict[str, Any]]:
    """Load stock data from Excel file and return as dictionary."""
    try:
        data_path = Path(__file__).parent.parent / "data" / "merged_stock_data.xlsx"
        df = pd.read_excel(data_path)
        
        # Check for duplicate symbols
        duplicates = df["Stock Symbol"].duplicated()
        if duplicates.any():
            duplicate_symbols = df[duplicates]["Stock Symbol"].unique()
            logger.warning(f"Found duplicate stock symbols: {duplicate_symbols}")
            # Keep the first occurrence of each duplicate
            df = df.drop_duplicates(subset=["Stock Symbol"], keep='first')

        # Convert NaN values to None for JSON compatibility
        df = df.where(pd.notnull(df), None)
        
        # Convert DataFrame to dictionary with stock symbol as key
        stock_data = df.set_index("Stock Symbol").to_dict(orient="index")
        
        logger.info(f"Successfully loaded data for {len(stock_data)} stocks")
        return stock_data
        
    except Exception as e:
        logger.error(f"Error loading stock data: {str(e)}")
        raise
