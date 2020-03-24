import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Questions2 (id INTEGER PRIMARY KEY, question text, answerA text, answerB text, answerC text, answerD text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * from Questions2")
        rows = self.cur.fetchall()
        return rows

    def insert(self, question, answerA, answerB, answerC, answerD):
        self.cur.execute("INSERT INTO Questions2 VALUES (NULL, ?, ?, ?, ?, ?)",(question, answerA, answerB, answerC, answerD))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM Questions2 WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, question, answerA, answerB, answerC, answerD):
        self.cur.execute("UPDATE Questions2 SET question = ?, answerA = ?, answerB = ?, answerC = ?, answerD = ? WHERE id = ?", (question, answerA, answerB, answerC, answerD, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
