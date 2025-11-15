import psycopg2

class Database:

    def __init__(self):
        self.conn = psycopg2.connect( # This is sample data, please do not share it on GitHub!
            database="endstone",
            user="postgres",
            password="1234",
            host="172.17.0.3",
            port=5432
        )

    def getMoneyByUser(self, nametag):

        cur = self.conn.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s', (nametag,))
        rows = cur.fetchall()
        cur.close()
        if(len(rows) == 0):
            return 0
        return rows[0][2]

    def close(self):
        self.conn.close()