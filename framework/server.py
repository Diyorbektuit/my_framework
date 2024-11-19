from wsgiref.simple_server import make_server
import json
from framework.routes import Router
from .utils import get_query_params


def sample_app(environ, start_response):
    # PATH_INFO orqali URL path olamiz
    path = environ.get('PATH_INFO', '/')
    method = environ.get('REQUEST_METHOD', 'GET').upper()
    # QUERY_STRING orqali query parametrlarni olamiz
    query_string = environ.get('QUERY_STRING', '')
    query_params = get_query_params(query_string)

    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError, TypeError):
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size) if request_body_size > 0 else b''
    body = json.loads(request_body) if request_body else {}

    data = Router.dispatch(path, method, query_params, body)

    # HTTP status va headerlarni aniqlash
    status = data.get('status')
    headers = [("Content-type", "application/json")]
    start_response(status, headers)

    # Ma'lumotlarni JSON formatiga o‘tkazamiz
    response = json.dumps(data.get('message')).encode("utf-8")
    print(response)
    return [response]


# Serverni ishga tushiramiz
server = make_server("localhost", 8080, sample_app)
print("Serving on http://localhost:8080")
server.serve_forever()
