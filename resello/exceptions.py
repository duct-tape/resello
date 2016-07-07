class ReselloException(Exception):
    code = None
    message = ""

    def __init__(self, code, message=None):
        self.code = code
        self.message = message
