# pip install psycopg2-binary

import psycopg2


class Sql:

    DBNAME = 'python'
    HOSTNAME = '127.0.0.1'
    USERNAME = 'geek'
    PASSWORD = 'toor'

    def __init__(self):
        try:
            self.__conn = psycopg2.connect(
                database=Sql.DBNAME,
                host=Sql.HOSTNAME,
                user=Sql.USERNAME,
                password=Sql.PASSWORD
            )
        except psycopg2.Error as e:
            print(f"Erro na conexao ao PostgreSQL Server: {e}")

    @property
    def conn(self):
        return self.__conn

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def select(self, stmt):
        cur = self.conn.cursor()
        cur.execute(stmt)
        self.commit()
        return cur.fetchall()

    def query(self, stmt):
        cur = self.conn.cursor()
        cur.execute(stmt)
        self.commit()

    def commit(self):
        self.conn.commit()

    @classmethod
    def change_conn(cls, hostname, username, password, dbname):
        cls.HOSTNAME = hostname
        cls.USERNAME = username
        cls.PASSWORD = password
        cls.DBNAME = dbname






