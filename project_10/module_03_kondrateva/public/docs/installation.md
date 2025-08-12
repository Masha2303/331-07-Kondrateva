# Инструкция по установке - Модуль 03

## Требования

- Python 3.8 или выше
- Tkinter (обычно входит в стандартную установку Python)

## Установка

### 1. Клонирование репозитория
```bash
git clone <repository-url>
cd project_10/module_03_kondrateva
```

### 2. Проверка Python
```bash
python --version
# Должно быть 3.8 или выше
```

### 3. Проверка Tkinter
```bash
python -c "import tkinter; print('Tkinter доступен')"
```

## Запуск

### Основной запуск
```bash
python src/index.py
```

### Прямой запуск главного окна
```bash
python src/main.py
```

### Через конфигурацию
```bash
python package.py
```

## Структура файлов

```
module_03_kondrateva/
├── src/
│   ├── main.py              # Главное окно
│   ├── index.py             # Точка входа
│   ├── components/          # UI компоненты
│   ├── services/            # Сервисы
│   └── utils/               # Утилиты
├── public/                  # Публичные ресурсы
└── package.py               # Конфигурация
```

## Устранение неполадок

### Ошибка "No module named tkinter"
Установите Tkinter для вашей системы:
- Ubuntu/Debian: `sudo apt-get install python3-tk`
- CentOS/RHEL: `sudo yum install tkinter`
- Windows: Обычно включен в Python

### Ошибка базы данных
База данных SQLite создается автоматически при первом запуске.
