from flask import Flask
from .services.models import db, PartnerType
from .components.routes import bp
from flask_sqlalchemy import SQLAlchemy
from .contexts import register_contexts
from .hooks import register_hooks

# Инициализация Flask-приложения и базы данных
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///partners.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your-secret-key-here'

db.init_app(app)

# Регистрация Blueprint
app.register_blueprint(bp)

# Инициализация БД начальными типами партнёров
@app.before_first_request
def init_db():
    db.create_all()
    if PartnerType.query.count() == 0:
        types = [
            PartnerType(name='Розничный магазин'),
            PartnerType(name='Оптовый поставщик'),
            PartnerType(name='Строительная компания'),
            PartnerType(name='Дизайн-студия')
        ]
        db.session.add_all(types)
        db.session.commit()

register_contexts(app)
register_hooks(app)
