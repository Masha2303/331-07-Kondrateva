# Точка входа в приложение (шаблон модуля 03)
import sys
import os

# Добавляем путь к модулям
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import MainModule
from services.partners_service import PartnersService
from utils.validators import Validator

class Index:
    @staticmethod
    def initialize():
        """Инициализация приложения"""
        print("Инициализация модуля 03...")
        
        # Инициализация сервисов
        partners_service = PartnersService()
        
        # Инициализация утилит
        validator = Validator()
        
        print("Модуль 03 инициализирован успешно!")
        return partners_service, validator
    
    @staticmethod
    def run():
        """Запуск приложения"""
        try:
            # Инициализация
            partners_service, validator = Index.initialize()
            
            # Запуск главного окна
            app = MainModule()
            app.run()
            
        except Exception as e:
            print(f"Ошибка запуска приложения: {e}")
            sys.exit(1)

if __name__ == "__main__":
    Index.run()
