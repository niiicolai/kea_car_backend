from api import get_data_from_api
from fastapi import FastAPI, Depends, HTTPException
from db import Session
from db import get_db as get_db_session
from sqlalchemy import text
from app.controllers.controller_colors import colors_router
from app.controllers.controller_accessories import accessories_router
from app.controllers.controller_brands import brands_router
from app.controllers.controller_customers import customers_router
from app.controllers.controller_insurances import insurances_router
from app.controllers.controller_sales_people import sales_people_router
from app.controllers.controller_models import models_router

app = FastAPI()

app.include_router(colors_router, tags=["Colors"])
app.include_router(accessories_router, tags=["Accessories"])
app.include_router(brands_router, tags=["Brands"])
app.include_router(customers_router, tags=["Customers"])
app.include_router(insurances_router, tags=["Insurances"])
app.include_router(sales_people_router, tags=["Sales People"])
app.include_router(models_router, tags=["Models"])

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