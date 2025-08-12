# Сервис для работы с партнёрами
import sqlite3
import json
from typing import List, Dict, Optional

class PartnersService:
    def __init__(self, db_path: str = "partners.db"):
        """Инициализация сервиса партнёров"""
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Инициализация базы данных"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS partners (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        partner_type TEXT NOT NULL,
                        rating INTEGER DEFAULT 0,
                        address TEXT,
                        director TEXT,
                        phone TEXT,
                        email TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                conn.commit()
        except Exception as e:
            print(f"Ошибка инициализации БД: {e}")
    
    def add_partner(self, partner_data: Dict) -> bool:
        """Добавление нового партнёра"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO partners (name, partner_type, rating, address, director, phone, email)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    partner_data['name'],
                    partner_data['partner_type'],
                    partner_data['rating'],
                    partner_data.get('address', ''),
                    partner_data.get('director', ''),
                    partner_data.get('phone', ''),
                    partner_data.get('email', '')
                ))
                conn.commit()
                return True
        except Exception as e:
            print(f"Ошибка добавления партнёра: {e}")
            return False
    
    def get_all_partners(self) -> List[Dict]:
        """Получение всех партнёров"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM partners ORDER BY name')
                columns = [description[0] for description in cursor.description]
                return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Ошибка получения партнёров: {e}")
            return []
    
    def get_partner_by_id(self, partner_id: int) -> Optional[Dict]:
        """Получение партнёра по ID"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM partners WHERE id = ?', (partner_id,))
                row = cursor.fetchone()
                if row:
                    columns = [description[0] for description in cursor.description]
                    return dict(zip(columns, row))
                return None
        except Exception as e:
            print(f"Ошибка получения партнёра: {e}")
            return None
    
    def update_partner(self, partner_id: int, partner_data: Dict) -> bool:
        """Обновление партнёра"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE partners 
                    SET name=?, partner_type=?, rating=?, address=?, director=?, phone=?, email=?
                    WHERE id=?
                ''', (
                    partner_data['name'],
                    partner_data['partner_type'],
                    partner_data['rating'],
                    partner_data.get('address', ''),
                    partner_data.get('director', ''),
                    partner_data.get('phone', ''),
                    partner_data.get('email', ''),
                    partner_id
                ))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Ошибка обновления партнёра: {e}")
            return False
    
    def delete_partner(self, partner_id: int) -> bool:
        """Удаление партнёра"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM partners WHERE id = ?', (partner_id,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Ошибка удаления партнёра: {e}")
            return False
    
    def get_partner_types(self) -> List[str]:
        """Получение списка типов партнёров"""
        return ["Поставщик", "Клиент", "Партнёр", "Дистрибьютор"]
