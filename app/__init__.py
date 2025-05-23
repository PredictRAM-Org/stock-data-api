"""
Stock Data API Package

This package contains the FastAPI application for serving stock market data.
The main application is defined in app/main.py.

Modules:
    - main: Contains the FastAPI application and routes
    - data_loader: Handles loading and accessing the stock data
    - models: Defines Pydantic models for API responses
    - utils: Utility functions for data access
"""

__version__ = "1.0.0"
__all__ = ["main", "data_loader", "models", "utils"]

# Initialize package-level variables
# This can be used to store shared state if needed
app = None

def get_app():
    """Get the FastAPI application instance."""
    from .main import app as fastapi_app
    return fastapi_app

# Optional: Initialize the app when the package is imported
# Uncomment if you want the app to be created immediately
# app = get_app()