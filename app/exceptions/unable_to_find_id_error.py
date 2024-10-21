class UnableToFindIdError(Exception):
    def __init__(self, entity_name: str, entity_id: str):
        self.message = f'{entity_name} with ID {entity_id} does not exist.'
        super().__init__(self.message)  # Initialize the base Exception with the message

    def __str__(self):
        return self.message
