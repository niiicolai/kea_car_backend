from api import get_data_from_api
from fastapi import FastAPI, Depends, HTTPException
from db import Session, get_db as get_db_session
from sqlalchemy import text

app = FastAPI()

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