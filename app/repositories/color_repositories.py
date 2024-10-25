# External Library imports
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import Optional, List, cast

# Internal library imports
from app.models.color import Color
from app.resources.color_resource import ColorReturnResource, ColorCreateResource


class ColorRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[ColorReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, color_id: str) -> Optional[ColorReturnResource]:
        pass

    @abstractmethod
    def create(self, color_create_data: ColorCreateResource) -> ColorReturnResource:
        pass

    @abstractmethod
    def is_name_taken(self, name: str) -> bool:
        pass

class MySQLColorRepository(ColorRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[ColorReturnResource]:
        colors: List[Color] = cast(List[Color], self.session.query(Color).all())
        return [color.as_resource() for color in colors]

    def get_by_id(self, color_id: str) -> Optional[ColorReturnResource]:
        color: Optional[Color] = self.session.query(Color).get(color_id)
        if color is not None:
            return color.as_resource()
        return None

    def create(self, color_create_data: ColorCreateResource) -> ColorReturnResource:
        new_color = Color(
            name=color_create_data.name,
            price=color_create_data.price,
            red_value=color_create_data.red_value,
            green_value=color_create_data.green_value,
            blue_value=color_create_data.blue_value,
        )
        self.session.add(new_color)
        self.session.commit()
        self.session.refresh(new_color)

        return new_color.as_resource()

    def is_name_taken(self, name: str) -> bool:
        return self.session.query(Color).filter_by(name=name).first() is not None

# Placeholder for future repositories
# class OtherDBColorRepository(ColorRepository):
#     ...