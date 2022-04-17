import sqlite3

class botDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def add_message(self, user_id, message):
        self.cursor.execute("INSERT INTO 'messages' ('user_id', 'message', 'status') VALUES (?, ?, ?)", (user_id, message, 'на проверке'))
        self.conn.commit()

    def change_status(self, id, new_status):
        self.cursor.execute("UPDATE 'messages' SET status=? WHERE id=?", (new_status, id))


    def close(self):
        self.conn.close()