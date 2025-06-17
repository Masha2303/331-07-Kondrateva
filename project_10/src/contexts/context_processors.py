from flask import current_app

def inject_app_name():
    """
    Пример context processor: добавляет имя приложения во все шаблоны.
    """
    return {'app_name': current_app.name} 