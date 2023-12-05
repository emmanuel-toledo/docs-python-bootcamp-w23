from db.db_context import DB_Context as _DB_Context
from models.task import Task as _Task

class Task_Context:

    def __init__(self):
        self.db = _DB_Context()
        self._initialize_table()
        pass

    def _initialize_table(self):
        self.db.open()
        self.db.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS task (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                status INTEGER DEFAULT 1,
                created_on TEXT,
                completed_on TEXT
            )
            """)
        self.db.connection.commit()
        self.db.close()

    def get_all(self):
        self.db.open()
        self.db.cursor.execute("SELECT id, name, description, status, created_on, completed_on FROM task")
        data = self.db.cursor.fetchall()
        self.db.close()
        return data
        
    def get(self, task: _Task):
        self.db.open()
        self.db.cursor.execute(
            """SELECT 
                id, 
                name, 
                description, 
                status, 
                created_on, 
                completed_on
                FROM task WHERE id = ?""", (task.get_id(),))
        data = self.db.cursor.fetchone()
        self.db.close()
        return data

    def add(self, task: _Task):
        self.db.open()
        self.db.cursor.execute(
            """INSERT INTO task 
            (name, description, created_on) VALUES 
            (?, ?, ?)""", (task.get_name(), task.get_description(), task.get_created_on()))
        self.db.connection.commit()
        id = self.db.cursor.lastrowid
        self.db.close()
        return id
    
    def delete(self, task: _Task):
        self.db.open()
        self.db.cursor.execute("DELETE FROM task WHERE id = ?", (task.get_id(),))
        self.db.connection.commit()
        self.db.close()

    def update(self, task: _Task):
        self.db.open()
        self.db.cursor.execute(
            """UPDATE task 
            SET name = ?, 
            description = ?, 
            status = ?,
            completed_on = ?
            WHERE id = ?""", (task.get_name(), task.get_description(), task.get_status(), task.get_completed_on(), task.get_id()))
        self.db.connection.commit()
        self.db.close()