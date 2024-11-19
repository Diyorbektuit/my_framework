from framework import status
from framework.request import Request
from framework.response import Response


class BaseView:

    def get(self, request: Request) -> Response:
        return Response(data={"error": "GET method not allowed"}, status="405 Method Not Allowed")

    def post(self, request: Request) -> Response:
        return Response(data={"error": "POST method not allowed"}, status="405 Method Not Allowed")

    def put(self, request: Request) -> Response:
        return Response(data={"error": "PUT method not allowed"}, status="405 Method Not Allowed")

    def patch(self, request: Request) -> Response:
        return Response(data={"error": "PATCH method not allowed"}, status="405 Method Not Allowed")

    def delete(self, request: Request) -> Response:
        return Response(data={"error": "DELETE method not allowed"}, status="405 Method Not Allowed")

    def run(self, request: Request) -> dict:
        # So'rov turiga qarab tegishli metodni chaqirish
        method = request.method.lower()
        if hasattr(self, method):
            response = getattr(self, method)(request)
        else:
            response = Response(data={"error": f"{request.method} method not allowed"}, status="405 Method Not Allowed")

        return {
            "message": response.data,
            "status": response.status,
        }

    @classmethod
    def as_view(cls):
        return cls()



class ListApiView(BaseView):
    queryset = None
    fields = []

    def get(self, request: Request) -> Response:
        count = len(list(self.queryset))

        query_data = []
        for query in self.queryset:
            data = {}
            for field in self.fields:
                response = getattr(query, field, None)
                data.update({
                    field: response if str(type(response)) == "<class 'int'>" else str(response),
                })
            query_data.append(data)

        data = {
            'count': count,
            'data': query_data
        }

        return Response(data=data, status=status.status_200)

