from flask import request

def before_request_hook():
    """
    Пример before_request hook: логирует каждый запрос.
    """
    print(f"[HOOK] Before request: {request.method} {request.path}")

def teardown_request_hook(exception=None):
    """
    Пример teardown_request hook: логирует завершение запроса.
    """
    print(f"[HOOK] Teardown request: {request.method} {request.path}") 