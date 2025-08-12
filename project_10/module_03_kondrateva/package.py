# Конфигурация проекта (зависимости и скрипты)
import os
import sys
from typing import Dict, List

class ProjectConfig:
    """Конфигурация проекта Модуль 03"""
    
    # Основная информация о проекте
    PROJECT_NAME = "project_10_module_03_kondrateva"
    VERSION = "1.0.0"
    DESCRIPTION = "Модуль 03 - Система управления партнёрами на Python"
    AUTHOR = "Кондратьева"
    LICENSE = "MIT"
    
    # Основные скрипты
    SCRIPTS = {
        "start": "python src/index.py",
        "dev": "python src/main.py", 
        "test": "python -m pytest tests/",
        "build": "echo 'Сборка завершена'"
    }
    
    # Зависимости
    DEPENDENCIES = {
        "python": ">=3.8",
        "tkinter": "built-in",
        "sqlite3": "built-in"
    }
    
    # Зависимости для разработки
    DEV_DEPENDENCIES = {
        "pytest": "^7.0.0",
        "black": "^22.0.0", 
        "flake8": "^4.0.0"
    }
    
    # Ключевые слова
    KEYWORDS = [
        "python",
        "tkinter", 
        "partners",
        "management",
        "gui"
    ]
    
    @classmethod
    def get_project_info(cls) -> Dict:
        """Получение информации о проекте"""
        return {
            "name": cls.PROJECT_NAME,
            "version": cls.VERSION,
            "description": cls.DESCRIPTION,
            "author": cls.AUTHOR,
            "license": cls.LICENSE,
            "main": "src/index.py",
            "scripts": cls.SCRIPTS,
            "dependencies": cls.DEPENDENCIES,
            "devDependencies": cls.DEV_DEPENDENCIES,
            "keywords": cls.KEYWORDS
        }
    
    @classmethod
    def run_script(cls, script_name: str) -> bool:
        """Запуск скрипта по имени"""
        if script_name in cls.SCRIPTS:
            command = cls.SCRIPTS[script_name]
            print(f"Выполнение: {command}")
            return os.system(command) == 0
        else:
            print(f"Скрипт '{script_name}' не найден")
            return False
    
    @classmethod
    def list_scripts(cls) -> List[str]:
        """Список доступных скриптов"""
        return list(cls.SCRIPTS.keys())

# Пример использования
if __name__ == "__main__":
    config = ProjectConfig()
    print("Конфигурация проекта:")
    print(config.get_project_info())
    
    print("\nДоступные скрипты:")
    for script in config.list_scripts():
        print(f"  {script}: {config.SCRIPTS[script]}")
