# API Документация - Модуль 03

## PartnersService

### Методы

- `add_partner(data)` - добавление партнёра
- `get_all_partners()` - получение всех партнёров  
- `update_partner(id, data)` - обновление партнёра
- `delete_partner(id)` - удаление партнёра

## Validator

### Методы

- `validate_partner_data(data)` - валидация данных
- `validate_phone(phone)` - валидация телефона
- `validate_email(email)` - валидация email

## Структура данных

```python
{
    'name': str,            # Наименование
    'partner_type': str,    # Тип партнёра
    'rating': int,          # Рейтинг (0-1000)
    'address': str,         # Адрес
    'director': str,        # ФИО директора
    'phone': str,           # Телефон
    'email': str            # Email
}
```
