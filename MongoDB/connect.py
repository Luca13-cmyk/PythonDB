from MongoDB.Db import Db

mongo = Db()

db = mongo.conn.python

print(list(db.usuarios.find({})))

print(mongo.__repr__())

print(mongo.help())
