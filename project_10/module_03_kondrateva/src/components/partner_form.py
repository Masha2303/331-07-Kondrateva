# Компонент формы партнёра
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, Optional, Callable

class PartnerForm:
    def __init__(self, parent, partner_data: Optional[Dict] = None, 
                 on_save: Optional[Callable] = None):
        """Инициализация формы партнёра"""
        self.parent = parent
        self.partner_data = partner_data
        self.on_save = on_save
        
        # Создание окна
        self.window = tk.Toplevel(parent)
        self.window.title("Добавление партнёра" if not partner_data else "Редактирование партнёра")
        self.window.geometry("500x400")
        self.window.resizable(False, False)
        
        # Центрирование окна
        self.window.transient(parent)
        self.window.grab_set()
        
        self.setup_ui()
        self.load_data()
    
    def setup_ui(self):
        """Настройка пользовательского интерфейса"""
        # Основной фрейм
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Заголовок
        title = "Добавление партнёра" if not self.partner_data else "Редактирование партнёра"
        title_label = ttk.Label(main_frame, text=title, font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Поля формы
        row = 1
        
        # Наименование
        ttk.Label(main_frame, text="Наименование *:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(main_frame, textvariable=self.name_var, width=30)
        self.name_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        row += 1
        
        # Тип партнёра
        ttk.Label(main_frame, text="Тип партнёра *:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.type_var = tk.StringVar()
        self.type_combo = ttk.Combobox(main_frame, textvariable=self.type_var, 
                                      values=["Поставщик", "Клиент", "Партнёр", "Дистрибьютор"],
                                      state="readonly", width=27)
        self.type_combo.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        row += 1
        
        # Рейтинг
        ttk.Label(main_frame, text="Рейтинг:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.rating_var = tk.IntVar(value=0)
        self.rating_spinbox = ttk.Spinbox(main_frame, from_=0, to=1000, 
                                         textvariable=self.rating_var, width=27)
        self.rating_spinbox.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        row += 1
        
        # Адрес
        ttk.Label(main_frame, text="Адрес:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.address_var = tk.StringVar()
        self.address_entry = ttk.Entry(main_frame, textvariable=self.address_var, width=30)
        self.address_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        row += 1
        
        # ФИО директора
        ttk.Label(main_frame, text="ФИО директора:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.director_var = tk.StringVar()
        self.director_entry = ttk.Entry(main_frame, textvariable=self.director_var, width=30)
        self.director_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        row += 1
        
        # Телефон
        ttk.Label(main_frame, text="Телефон:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.phone_var = tk.StringVar()
        self.phone_entry = ttk.Entry(main_frame, textvariable=self.phone_var, width=30)
        self.phone_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        row += 1
        
        # Email
        ttk.Label(main_frame, text="Email:").grid(row=row, column=0, sticky=tk.W, pady=5)
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(main_frame, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        row += 1
        
        # Кнопки
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=row, column=0, columnspan=2, pady=20)
        
        ttk.Button(button_frame, text="Сохранить", command=self.save_partner).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Отмена", command=self.cancel).pack(side=tk.LEFT, padx=5)
        
        # Настройка весов для растягивания
        main_frame.columnconfigure(1, weight=1)
    
    def load_data(self):
        """Загрузка данных для редактирования"""
        if self.partner_data:
            self.name_var.set(self.partner_data.get('name', ''))
            self.type_var.set(self.partner_data.get('partner_type', ''))
            self.rating_var.set(self.partner_data.get('rating', 0))
            self.address_var.set(self.partner_data.get('address', ''))
            self.director_var.set(self.partner_data.get('director', ''))
            self.phone_var.set(self.partner_data.get('phone', ''))
            self.email_var.set(self.partner_data.get('email', ''))
    
    def get_form_data(self) -> Dict:
        """Получение данных из формы"""
        return {
            'name': self.name_var.get().strip(),
            'partner_type': self.type_var.get(),
            'rating': self.rating_var.get(),
            'address': self.address_var.get().strip(),
            'director': self.director_var.get().strip(),
            'phone': self.phone_var.get().strip(),
            'email': self.email_var.get().strip()
        }
    
    def save_partner(self):
        """Сохранение партнёра"""
        if self.on_save:
            data = self.get_form_data()
            if self.on_save(data):
                self.window.destroy()
    
    def cancel(self):
        """Отмена операции"""
        self.window.destroy()
