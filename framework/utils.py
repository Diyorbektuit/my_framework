from urllib.parse import parse_qs

def get_query_params(query_string):
    parsed_params = parse_qs(query_string)
    return {k: v[0] if isinstance(v, list) and len(v) > 0 else None for k, v in parsed_params.items()}