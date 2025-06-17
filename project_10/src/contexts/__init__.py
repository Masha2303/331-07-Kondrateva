from .context_processors import inject_app_name

def register_contexts(app):
    """
    Регистрирует все context processors для Flask-приложения.
    """
    app.context_processor(inject_app_name) 