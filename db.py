import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts (part text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * from parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, part):
        self.cur.execute("INSERT INTO parts VALUES (?)",(part,))
        self.conn.commit()

    def remove(self, part):
        self.cur.execute("DELETE FROM parts WHERE part=?", (part,))
        self.conn.commit()
    def update(self, part):
        self.cur.execute("UPDATE parts SET part = ?",(part,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database('store.db')
#db.insert("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
#db.insert("Asus Mobo", "Mike Henry", "Microcenter", "360")
