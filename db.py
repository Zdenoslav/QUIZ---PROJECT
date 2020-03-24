import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Questions1 (id INTEGER PRIMARY KEY, question text, answer text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * from Questions1")
        rows = self.cur.fetchall()
        return rows

    def insert(self, question, answer):
        self.cur.execute("INSERT INTO Questions1 VALUES (NULL, ?, ?)",(question, answer,))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM Questions1 WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, question, answer):

        self.cur.execute("UPDATE Questions1 SET question = ?, answer = ?, WHERE id = ?", (question, answer, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database('store.db')
#db.insert("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
#db.insert("Asus Mobo", "Mike Henry", "Microcenter", "360")
