from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db import Session
from db import get_db as get_db_session
from sqlalchemy import text
from app.controllers import (
    controller_brands,
    controller_colors,
    controller_models,
    controller_customers,
    controller_insurances,
    controller_accessories,
    controller_sales_people,
    controller_purchases,
    controller_cars
)

app = FastAPI()


CORS_SETTINGS = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"]
}

app.add_middleware(CORSMiddleware, **CORS_SETTINGS)

app.include_router(controller_brands.router, prefix="/mysql", tags=["MySQL - Brands"])
app.include_router(controller_colors.router, prefix="/mysql", tags=["MySQL - Colors"])
app.include_router(controller_models.router, prefix="/mysql", tags=["MySQL - Models"])
app.include_router(controller_customers.router, prefix="/mysql", tags=["MySQL - Customers"])
app.include_router(controller_insurances.router, prefix="/mysql", tags=["MySQL - Insurances"])
app.include_router(controller_accessories.router, prefix="/mysql", tags=["MySQL - Accessories"])
app.include_router(controller_sales_people.router, prefix="/mysql", tags=["MySQL - Sales People"])
app.include_router(controller_purchases.router, prefix="/mysql", tags=["MySQL - Purchases"])
app.include_router(controller_cars.router, prefix="/mysql", tags=["MySQL - Cars"])

def get_db():
    with get_db_session() as session:
        yield session

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test-db")
async def get_db_connection(db: Session = Depends(get_db)):
    """
    Endpoint to test the database connection by returning the current database name.
    """
    try:
        # Use text() to create a text-based SQL expression
        result = db.execute(text("SELECT DATABASE();"))
        # Fetch the result
        database_name = result.scalar()

        return {"message": "Connected to database", "database_name": database_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to database: {e}")