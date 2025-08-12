# Утилиты для валидации данных
import re
from typing import Dict, List, Tuple

class Validator:
    """Класс для валидации данных партнёров"""
    
    @staticmethod
    def validate_partner_data(data: Dict) -> Tuple[bool, List[str]]:
        """Валидация данных партнёра"""
        errors = []
        
        # Проверка наименования
        if not data.get('name') or not data['name'].strip():
            errors.append("Наименование обязательно для заполнения")
        
        # Проверка типа партнёра
        if not data.get('partner_type') or not data['partner_type'].strip():
            errors.append("Тип партнёра обязателен для заполнения")
        
        # Проверка рейтинга
        rating = data.get('rating', 0)
        if not isinstance(rating, int) or rating < 0:
            errors.append("Рейтинг должен быть целым неотрицательным числом")
        
        # Проверка телефона
        phone = data.get('phone', '').strip()
        if phone and not Validator.validate_phone(phone):
            errors.append("Неверный формат телефона. Используйте: +7XXXXXXXXXX или 7XXXXXXXXXX")
        
        # Проверка email
        email = data.get('email', '').strip()
        if email and not Validator.validate_email(email):
            errors.append("Неверный формат email")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Валидация номера телефона"""
        # Паттерн для российских номеров: +7XXXXXXXXXX или 7XXXXXXXXXX
        pattern = r'^\+?7?\d{10}$'
        return bool(re.match(pattern, phone))
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Валидация email адреса"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_rating(rating: int) -> bool:
        """Валидация рейтинга"""
        return isinstance(rating, int) and 0 <= rating <= 1000
    
    @staticmethod
    def sanitize_input(text: str) -> str:
        """Очистка введённого текста от лишних символов"""
        if not text:
            return ""
        return text.strip()
    
    @staticmethod
    def format_phone(phone: str) -> str:
        """Форматирование номера телефона"""
        # Убираем все нецифровые символы
        digits = re.sub(r'\D', '', phone)
        
        # Если номер начинается с 8, заменяем на 7
        if digits.startswith('8') and len(digits) == 11:
            digits = '7' + digits[1:]
        
        # Добавляем +7 если номер из 10 цифр
        if len(digits) == 10:
            digits = '7' + digits
        
        # Добавляем + если его нет
        if not digits.startswith('+'):
            digits = '+' + digits
            
        return digits
