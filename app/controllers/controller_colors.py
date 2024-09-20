from fastapi import APIRouter, Depends, HTTPException
from db import Session
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from db import get_db as get_db_session
from app.services import service_colors
from app.resources.color_resource import ColorCreateResource

router: APIRouter = APIRouter()

def get_db():
    with get_db_session() as session:
        yield session

@router.get("/colors")
async def get_colors(session: Session = Depends(get_db)):
    try:
        colors = service_colors.get_all(session)
        return {"data": colors}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(f"SQL Error caught. Failed to retrieve colors: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"Exception caught. Failed to retrieve colors: {e}"))

@router.get("/color/{color_id}")
async def get_color(color_id: int, session: Session = Depends(get_db)):
    try:
        color = service_colors.get_by_id(session, color_id)
        return {"data": color}
    except ValueError as e: 
        raise HTTPException(status_code=404, detail=str(f"Value error failed to retrieve color: {e}"))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(f"SQL Error caught. Failed to retrieve color: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"unknown error chaught. Failed to create color: {e}"))


@router.post("/color")
async def create_color(color_create_data: ColorCreateResource, session: Session = Depends(get_db)):
    try:
        new_color = service_colors.create(session, color_create_data)
        return {"data": new_color}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(f"SQL Error caught. Failed to create color: {e}"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(f"unknown error chaught. Failed to create color: {e}"))
