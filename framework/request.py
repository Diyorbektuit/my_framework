class Request:
    def __init__(self, query_params: dict, method: str = "GET", body: dict = None):
        self.query_params = query_params
        self.method = method
        self.body = body or {}
