from functools import wraps


def make_html(element):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            result = f'<{element}>{result}</{element}>'
            return result
        return wrapper
    return decorator