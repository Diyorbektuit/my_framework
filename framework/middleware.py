from framework.request import Request
from framework.response import Response
import json
from framework import status

class Middleware:
    def process_request(self, request: Request):
        pass

    def process_response(self, response: Response):
        pass


class LoggerMiddleware(Middleware):
    def process_request(self, request: Request):
        print(f"[LOG] Method: {request.method}, Path: {request.query_params}")

    def process_response(self, response: Response):
        if response is None:
            response = Response(data={"msg": "Response was not generated."}, status=status.status_500)
        print(f"[LOG] Status: {response.status}")
        return response

class RequestBodyMiddleware(Middleware):
    def process_request(self, request: Request):
        if request.method in ["POST", "PUT", "PATCH"]:
            # Agar body mavjud bo'lsa, uni o'qish va JSON formatiga o'tkazish
            if isinstance(request.body, str):  # Agar body string bo'lsa
                try:
                    request.body = json.loads(request.body)  # JSON ni dictionary ga o'zgartirish
                except json.JSONDecodeError:
                    # Agar JSON formatda bo'lmasa, xatolik qaytarish
                    return Response(
                        data={"msg": "Bad Request: Invalid JSON format"},
                        status=status.status_400
                    )

            # Agar body bo'sh bo'lsa, uni bo'sh dictionary qilib o'zgartirish
        if not request.body:
            request.body = {}

        return None