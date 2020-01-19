# pip install pyrebase
import pyrebase


class Db:

    CONFIG = {
        "apiKey": "AIzaSyDf-W4NgZtVQVwQ5JRqcI2jAAZZ3TI5bqc",
        "authDomain": "https://python-teste-b3ea8.firebaseio.com/",
        "databaseURL": "https://python-teste-b3ea8.firebaseio.com/",
        "storageBucket": "python-teste-b3ea8.appspot.com/",
        "projectId": "python-teste-b3ea8"
    }

    def __init__(self):
        self.__conn = pyrebase.initialize_app(Db.CONFIG)
        self.__db = self.__conn.database()

    @property
    def conn(self):
        return self.__conn

    @property
    def db(self):
        return self.__db

    def insert(self, collection, stmt):
        self.db.child(collection).push(stmt)

    def select(self, child):
        data = self.db.child(child).get()
        if data.val():
            return data.val()

    def update(self, collection, id_target, stmt):
        data = self.db.child(collection).child(id_target).get()
        if data.val():
            self.db.child(collection).child(id_target).update(stmt)

    def delete(self, collection, id_target):
        data = self.db.child(collection).child(id_target).get()
        if data.val():
            self.db.child(collection).child(id_target).remove()

    @classmethod
    def change_config(cls, stmt):
        cls.CONFIG = stmt





