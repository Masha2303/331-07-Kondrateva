from .lifecycle_hooks import before_request_hook, teardown_request_hook

def register_hooks(app):
    """
    Регистрирует before_request и teardown_request хуки для Flask-приложения.
    """
    app.before_request(before_request_hook)
    app.teardown_request(teardown_request_hook) 