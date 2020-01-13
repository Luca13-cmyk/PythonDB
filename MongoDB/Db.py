# pip3 install pymongo

from pymongo import MongoClient, errors
from bson.objectid import ObjectId


class Db:

    HOSTNAME = "127.0.0.1"
    PORT = 27017

    def __init__(self):
        self.__conn = MongoClient(Db.HOSTNAME, Db.PORT)

    @property
    def conn(self):
        return self.__conn

    def disconnect(self):
        if self.conn:
            self.conn.close()

    @staticmethod
    def object_id(obj_id):
        return ObjectId(obj_id)

    def __repr__(self):
        return self.__dict__

    @staticmethod
    def help():
        return """
    
    # Criando instancia da classe Db Mongo
    mongo = Db()

    # Fazendo a conexao no database python
    python = mongo.conn.python

    # Buscando dados
    print(list(python.usuarios.find({})))

    # Inserindo dados
    # python.usuarios.insert_one({"name": "Joaozinho da Silva"})

    # Atualizando dados
    python.usuarios.update_one(
        {"_id": mongo.object_id("5e1cc7c893192bc4de61c645")},
        {
            "$set": {
                "name": "Hotel Barato"
            }
        })

    # Deletando dados
    python.usuarios.delete_one({
        "_id": mongo.object_id("5e1cc7c893192bc4de61c645")
    })
    
    # metodos/atributos da instacia db.usuarios
    print(dir(db.usuarios))
        """

