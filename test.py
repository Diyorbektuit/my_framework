from urllib.parse import urlparse, parse_qs
url = 'data/?language=eng&hello=1'

parsed_url = urlparse(url)
path = parsed_url.path
query_params = parse_qs(parsed_url.query)

print(parsed_url)
print(path)
print(query_params)