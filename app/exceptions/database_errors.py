from datetime import date
from app.resources.car_resource import CarReturnResource

class DatabaseError(Exception):
    pass


class AlreadyTakenFieldValueError(DatabaseError):
    def __init__(self, entity_name: str, field: str, value: str):
        self.message = f'{entity_name} with {field}: {value} is already taken.'
        super().__init__(self.message)  # Call the base class constructor

    def __str__(self):
        return f"AlreadyTakenFieldValueException: {self.message}"

class UnableToFindIdError(DatabaseError):
    def __init__(self, entity_name: str, entity_id: str):
        self.message = f'{entity_name} with ID: {entity_id} does not exist.'
        super().__init__(self.message)  # Initialize the base Exception with the message

    def __str__(self):
        return f"UnableToFindIdException: {self.message}"

class PurchaseDeadlineHasPastError(DatabaseError):
    def __init__(self, car_resource: CarReturnResource):
        self.message = f'Car with ID: {car_resource.id} has a Purchase Deadline: {car_resource.purchase_deadline} has past the current date: {date.today()}.'
        super().__init__(self.message)  # Initialize the base Exception with the message

    def __str__(self):
        return f"PurchaseDeadlineHasPastException: {self.message}"

class UnableToFindEntityError(DatabaseError):
    def __init__(self, entity_name: str, field: str, value: str):
        self.message = f'{entity_name} with {field}: {value} does not exist.'
        super().__init__(self.message)  # Call the base class constructor

    def __str__(self):
        return f"UnableToFindEntityException: {self.message}"

class UnableToGiveEntityWithValueFromOtherEntityError(DatabaseError):
    def __init__(self, entity_name: str, field: str, value: str, other_entity_name: str):
        self.message = f'{entity_name} can not have {field}: {value} set from {other_entity_name}.'
        super().__init__(self.message)  # Call the base class constructor

    def __str__(self):
        return f"UnableToGiveEntityWithValueFromOtherEntityException: {self.message}"
