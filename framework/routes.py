from framework.views import BaseView
from framework.request import Request
from framework.settings import Settings

class Router:
    routes = {}

    @classmethod
    def add_route(cls, url: str, view: BaseView):
        route = {
            url: view
        }
        cls.routes.update(route)

    @classmethod
    def dispatch(cls, url: str, method:str, query_params: dict, body:dict = None):
        middlewares = Settings.get_middlewares()
        view = cls.routes.get(url)
        if view:
            request = Request(query_params=query_params, method=method, body=body)
            for middleware in middlewares:
                middleware.process_request(request)
            response =  view.run(request)
        else:
            response =  {"status": "404 Not Found", "message": {"error": "Page not found"}}

        for middleware in reversed(middlewares):
            response = middleware.process_response(response)

        return response



