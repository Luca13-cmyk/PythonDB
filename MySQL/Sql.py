# apt install python3-dev default-libmysqlclient-dev
# pip install mysqlclient

import MySQLdb


class Sql:

    HOSTNAME = "127.0.0.1"
    USERNAME = "luca13-cmyk"
    PASSWORD = "toor"
    DBNAME = "python"

    def __init__(self):
        try:
            self.__conn = MySQLdb.connect(
                db=Sql.DBNAME,
                host=Sql.HOSTNAME,
                user=Sql.USERNAME,
                passwd=Sql.PASSWORD
            )
        except MySQLdb.Error as e:
            print(f"Error na conexao ao MySQL Server: {e}")

    @property
    def conn(self):
        return self.__conn

    def disconnect(self):
        if self.conn:
            return self.conn.close()

    def query(self, stmt):
        cur = self.conn.cursor()
        cur.execute(stmt)
        self.commit()

    def select(self, stmt):
        cur = self.conn.cursor()
        cur.execute(stmt)
        self.commit()
        return cur.fetchall()

    def commit(self):
        self.conn.commit()

    @classmethod
    def change_conn(cls, hostname, username, password, dbname):
        cls.HOSTNAME = hostname
        cls.USERNAME = username
        cls.PASSWORD = password
        cls.DBNAME = dbname





