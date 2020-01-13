import _sqlite3


class Sql:

    DBNAME = 'SqlLiteTeste.db'

    def __init__(self):
        self.__conn = _sqlite3.connect(Sql.DBNAME)

    @property
    def conn(self):
        return self.__conn

    def disconnect(self):
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
