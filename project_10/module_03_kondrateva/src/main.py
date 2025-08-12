# Корневой компонент приложения (шаблон модуля 03)
import tkinter as tk
from tkinter import ttk, messagebox

class MainModule:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Модуль 03 - Управление партнёрами")
        self.root.geometry("800x600")
        
    def run(self):
        """Запуск главного окна приложения"""
        self.setup_ui()
        self.root.mainloop()
        
    def setup_ui(self):
        """Настройка пользовательского интерфейса"""
        # Создание меню
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Меню партнёров
        partners_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Партнёры", menu=partners_menu)
        partners_menu.add_command(label="Добавить", command=self.add_partner)
        partners_menu.add_command(label="Список", command=self.show_partners)
        
        # Главная область
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Заголовок
        title_label = ttk.Label(main_frame, text="Система управления партнёрами", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Кнопки действий
        ttk.Button(main_frame, text="Добавить партнёра", 
                  command=self.add_partner).grid(row=1, column=0, pady=10, padx=5)
        ttk.Button(main_frame, text="Просмотр партнёров", 
                  command=self.show_partners).grid(row=1, column=1, pady=10, padx=5)
        
    def add_partner(self):
        """Открытие формы добавления партнёра"""
        messagebox.showinfo("Информация", "Форма добавления партнёра")
        
    def show_partners(self):
        """Отображение списка партнёров"""
        messagebox.showinfo("Информация", "Список партнёров")

if __name__ == "__main__":
    app = MainModule()
    app.run()
