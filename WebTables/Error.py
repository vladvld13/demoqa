class InputNotSavedError(Exception):
    def __init__(self, name):
        self.name = name

class InvalidCommand(Exception):
    def __init__(self, name):
        self.name = name

class RowNotDeleted(Exception):
    def __init__(self, name):
        self.name = name