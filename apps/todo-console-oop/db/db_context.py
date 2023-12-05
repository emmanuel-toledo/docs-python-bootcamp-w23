import sqlite3

class DB_Context:

    def __init__(self):
        pass

    def open(self):
        self.connection = sqlite3.connect("./db/task.sqlite3")
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()
