from framework.middleware import LoggerMiddleware, Middleware, RequestBodyMiddleware

class Settings:
    middlewares = []

    @classmethod
    def add_middleware(cls, middleware: Middleware):
        cls.middlewares.append(middleware)

    @classmethod
    def get_middlewares(cls):
        return cls.middlewares

base_middleware = LoggerMiddleware()
request_middleware = RequestBodyMiddleware()

# Settings.add_middleware(middleware=base_middleware)
Settings.add_middleware(middleware=request_middleware)


