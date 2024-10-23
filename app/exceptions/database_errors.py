class DatabaseException(Exception):
    pass


class AlreadyTakenEmailException(DatabaseException):
    def __init__(self, email: str):
        self.message = f'The email "{email}" is already taken."'
        super().__init__(self.message)  # Call the base class constructor

    def __str__(self):
        return f"AlreadyTakenEmailException: {self.message}"

class UnableToFindIdException(DatabaseException):
    def __init__(self, entity_name: str, entity_id: str):
        self.message = f'{entity_name} with ID {entity_id} does not exist.'
        super().__init__(self.message)  # Initialize the base Exception with the message

    def __str__(self):
        return f"UnableToFindIdException: {self.message}"
