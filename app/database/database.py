import MySQLdb
from typing import Dict, List, Optional, Union
import os
import sys
from PyQt6.QtWidgets import QMessageBox


class Database:
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(
                host='localhost',
                user='root',
                password='',
                database='diplom_gushub',
                charset='utf8mb4'
            )
            # Устанавливаем курсор, который возвращает словари
            self.conn.cursorclass = MySQLdb.cursors.DictCursor
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Could not connect to database: {e}")
            sys.exit(1)

    # --- Курсы ---
    def add_course(self, github_path: str, title: str, description: str | None = None,
                   site_id: int | None = None) -> int:
        """Добавление курса в базу данных"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO courses (github_path, title, description, site_id)
                    VALUES (%s, %s, %s, %s)
                ''', (github_path, title, description, site_id))
                self.conn.commit()
                return cursor.lastrowid
        except MySQLdb.Error as e:
            self.conn.rollback()
            QMessageBox.critical(None, "Database Error", f"Error adding course: {e}")
            return -1

    def get_course(self, course_id: int) -> Optional[Dict[str, object]]:
        """Получение курса по его id"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    SELECT * FROM courses WHERE id = %s
                ''', (course_id,))
                return cursor.fetchone()
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error getting course: {e}")
            return None

    def get_courses(self) -> List[Dict[str, object]]:
        """Получение всех курсов"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    SELECT * FROM courses ORDER BY title
                ''')
                return cursor.fetchall()
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error getting courses: {e}")
            return []

    def delete_course(self, course_id: int) -> bool:
        """Удаление курса из базы данных"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    DELETE FROM courses WHERE id = %s
                ''', (course_id,))
                self.conn.commit()
                return cursor.rowcount > 0
        except MySQLdb.Error as e:
            self.conn.rollback()
            QMessageBox.critical(None, "Database Error", f"Error deleting course: {e}")
            return False

    # --- Модули ---
    def add_module(self, course_id: int, github_path: str, title: str, description: str | None = None,
                   site_id: int | None = None) -> int:
        """Добавление модуля в базу данных"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO modules (course_id, github_path, title, description, site_id)
                    VALUES (%s, %s, %s, %s, %s)
                ''', (course_id, github_path, title, description, site_id))
                self.conn.commit()
                return cursor.lastrowid
        except MySQLdb.Error as e:
            self.conn.rollback()
            QMessageBox.critical(None, "Database Error", f"Error adding module: {e}")
            return -1

    def get_module(self, module_id: int) -> Optional[Dict[str, object]]:
        """Получение модуля по его id"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    SELECT * FROM modules WHERE id = %s
                ''', (module_id,))
                return cursor.fetchone()
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error getting module: {e}")
            return None

    def get_modules(self) -> List[Dict[str, object]]:
        """Получение всех модулей"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    SELECT * FROM modules ORDER BY title
                ''')
                return cursor.fetchall()
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error getting modules: {e}")
            return []

    def get_modules_by_course(self, course_id: int) -> List[Dict[str, object]]:
        """Получение всех модулей по курсу"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    SELECT * FROM modules WHERE course_id = %s ORDER BY id
                ''', (course_id,))
                return cursor.fetchall()
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error getting modules by course: {e}")
            return []

    def delete_module(self, module_id: int) -> bool:
        """Удаление модуля из базы данных"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    DELETE FROM modules WHERE id = %s
                ''', (module_id,))
                self.conn.commit()
                return cursor.rowcount > 0
        except MySQLdb.Error as e:
            self.conn.rollback()
            QMessageBox.critical(None, "Database Error", f"Error deleting module: {e}")
            return False

    # --- Уроки ---
    def add_lesson(self, module_id: int, github_path: str, title: str, raw_url: str, site_id: int | None = None) -> int:
        """Добавление урока в базу данных"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO lessons (module_id, github_path, title, raw_url, site_id)
                    VALUES (%s, %s, %s, %s, %s)
                ''', (module_id, github_path, title, raw_url, site_id))
                self.conn.commit()
                return cursor.lastrowid
        except MySQLdb.Error as e:
            self.conn.rollback()
            QMessageBox.critical(None, "Database Error", f"Error adding lesson: {e}")
            return -1

    def get_lesson(self, lesson_id: int) -> Optional[Dict[str, object]]:
        """Получение урока по его id"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    SELECT * FROM lessons WHERE id = %s
                ''', (lesson_id,))
                return cursor.fetchone()
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error getting lesson: {e}")
            return None

    def get_lessons(self) -> List[Dict[str, object]]:
        """Получение всех уроков"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    SELECT * FROM lessons ORDER BY title
                ''')
                return cursor.fetchall()
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error getting lessons: {e}")
            return []

    def get_lessons_by_module(self, module_id: int) -> List[Dict[str, object]]:
        """Получение уроков по модулю"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    SELECT * FROM lessons WHERE module_id = %s ORDER BY id
                ''', (module_id,))
                return cursor.fetchall()
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error getting lessons by module: {e}")
            return []

    def delete_lesson(self, lesson_id: int) -> bool:
        """Удаление урока из базы данных"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    DELETE FROM lessons WHERE id = %s
                ''', (lesson_id,))
                self.conn.commit()
                return cursor.rowcount > 0
        except MySQLdb.Error as e:
            self.conn.rollback()
            QMessageBox.critical(None, "Database Error", f"Error deleting lesson: {e}")
            return False

    # --- Задачи ---
    def add_task(self, lesson_id: int, github_path: str, title: str, raw_url: str, site_id: int | None = None) -> int:
        """Добавление задачи в базу данных"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO tasks (lesson_id, github_path, title, raw_url, site_id)
                    VALUES (%s, %s, %s, %s, %s)
                ''', (lesson_id, github_path, title, raw_url, site_id))
                self.conn.commit()
                return cursor.lastrowid
        except MySQLdb.Error as e:
            self.conn.rollback()
            QMessageBox.critical(None, "Database Error", f"Error adding task: {e}")
            return -1

    def get_task(self, task_id: int) -> Optional[Dict[str, object]]:
        """Получение задачи по его id"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    SELECT * FROM tasks WHERE id = %s
                ''', (task_id,))
                return cursor.fetchone()
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error getting task: {e}")
            return None

    def get_tasks(self) -> List[Dict[str, object]]:
        """Получение всех задач"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    SELECT * FROM tasks ORDER BY title
                ''')
                return cursor.fetchall()
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error getting tasks: {e}")
            return []

    def get_tasks_by_lesson(self, lesson_id: int) -> List[Dict[str, object]]:
        """Получение всех задач по уроку"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    SELECT * FROM tasks WHERE lesson_id = %s ORDER BY id
                ''', (lesson_id,))
                return cursor.fetchall()
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error getting tasks by lesson: {e}")
            return []

    def delete_task(self, task_id: int) -> bool:
        """Удаление задачи из базы данных"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('''
                    DELETE FROM tasks WHERE id = %s
                ''', (task_id,))
                self.conn.commit()
                return cursor.rowcount > 0
        except MySQLdb.Error as e:
            self.conn.rollback()
            QMessageBox.critical(None, "Database Error", f"Error deleting task: {e}")
            return False

    def get_tasks_by_module(self, module_id: int) -> List[Dict[str, object]]:
        """Получение всех задач в модуле"""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                    SELECT t.id, t.title, t.github_path, t.raw_url
                    FROM tasks t
                    JOIN lessons l ON t.lesson_id = l.id
                    WHERE l.module_id = %s
                    ORDER BY t.id
                """, (module_id,))
                return cursor.fetchall()
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error getting tasks by module: {e}")
            return []

    def close(self) -> None:
        """Закрытие соединения с базой данных"""
        try:
            if hasattr(self, 'conn') and self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            QMessageBox.critical(None, "Database Error", f"Error closing connection: {e}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()