from datetime import date
from app.resources.car_resource import CarReturnResource, ModelReturnResource, ColorReturnResource

class DatabaseError(Exception):
    pass


class AlreadyTakenFieldValueError(DatabaseError):
    def __init__(self, entity_name: str, field: str, value: str):
        self.message = f'{entity_name} with {field}: {value} is already taken.'
        super().__init__(self.message)  # Call the base class constructor

    def __str__(self):
        return f"{self.message}"

class UnableToFindIdError(DatabaseError):
    def __init__(self, entity_name: str, entity_id: str):
        self.message = f'{entity_name} with ID: {entity_id} does not exist.'
        super().__init__(self.message)  # Initialize the base Exception with the message

    def __str__(self):
        return f"{self.message}"

class PurchaseDeadlineHasPastError(DatabaseError):
    def __init__(self, car_resource: CarReturnResource, date_of_purchase: date):
        self.message = f'Car with ID: {car_resource.id} has a Purchase Deadline: {car_resource.purchase_deadline.strftime("%d-%m-%Y")} that has past the date of purchase: {date_of_purchase.strftime("%d-%m-%Y")}.'
        super().__init__(self.message)  # Initialize the base Exception with the message

    def __str__(self):
        return f"{self.message}"

class UnableToFindEntityError(DatabaseError):
    def __init__(self, entity_name: str, field: str, value: str):
        self.message = f'{entity_name} with {field}: {value} does not exist.'
        super().__init__(self.message)  # Call the base class constructor

    def __str__(self):
        return f"{self.message}"

class TheColorIsNotAvailableInModelToGiveToCarError(DatabaseError):
    def __init__(self, model_resource: ModelReturnResource, color_resource: ColorReturnResource):
        self.message = f'The model: {model_resource.name} with colors: {[color.name for color in model_resource.colors]} does not have the color: {color_resource.name} to be given to a car.'
        super().__init__(self.message)  # Call the base class constructor

    def __str__(self):
        return f"{self.message}"

class UnableToDeleteCarWithoutDeletingPurchaseTooError(DatabaseError):
    def __init__(self, car_resource: CarReturnResource):
        self.message = f"The car with ID: '{car_resource.id}' must delete its purchase too."
        super().__init__(self.message)  # Call the base class constructor

    def __str__(self):
        return f"{self.message}"
