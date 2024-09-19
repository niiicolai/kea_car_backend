from fastapi import APIRouter, Depends, HTTPException
from db import Session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from main import get_db
from services import service_color

router: APIRouter = APIRouter()

@router.get("/colors")
async def get_colors(session: Session = Depends(get_db)):
    try:
        colors = service_color.get_all(session)
        return {"data": colors}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(f"SQL Error caught. Failed to retrieve colors: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Exception caught. Failed to retrieve colors: {e}"))
