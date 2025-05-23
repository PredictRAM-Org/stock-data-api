import pandas as pd
from pathlib import Path
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

def load_stock_data() -> Dict[str, Dict[str, Any]]:
    """Load stock data from Excel file and return as dictionary."""
    try:
        data_path = Path(__file__).parent.parent / "data" / "merged_stock_data.xlsx"
        logger.info(f"Loading data from: {data_path}")
        
        if not data_path.exists():
            raise FileNotFoundError(f"Data file not found at {data_path}")
            
        df = pd.read_excel(data_path)
        
        # Validate required columns
        if "Stock Symbol" not in df.columns:
            raise ValueError("Excel file must contain 'Stock Symbol' column")
            
        # Handle missing/empty symbols
        df = df[df["Stock Symbol"].notna()]
        
        # Check for duplicate symbols
        duplicates = df["Stock Symbol"].duplicated()
        if duplicates.any():
            duplicate_symbols = df[duplicates]["Stock Symbol"].unique()
            logger.warning(f"Found duplicate stock symbols: {duplicate_symbols}")
            df = df.drop_duplicates(subset=["Stock Symbol"], keep='first')

        # Convert all data to JSON-serializable types
        df = df.where(pd.notnull(df), None)
        
        # Convert to dictionary
        stock_data = df.set_index("Stock Symbol").to_dict(orient="index")
        
        logger.info(f"Loaded {len(stock_data)} stocks successfully")
        return stock_data
        
    except Exception as e:
        logger.error(f"Critical error loading stock data: {str(e)}")
        # Return empty dict to prevent app crash
        return {}

# Initialize data
stock_data = load_stock_data()
