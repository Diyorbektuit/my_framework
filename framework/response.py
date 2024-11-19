class Response:

    def __init__(self, data: dict or list, status: str):
        self.data = data
        self.status = status