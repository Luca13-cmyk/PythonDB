# pip install redis

import redis


class Db:

    HOSTNAME = "127.0.0.1"
    PORT = 6379

    def __init__(self):
        self.__conn = redis.Redis(
            host=Db.HOSTNAME,
            port=Db.PORT
        )

    @property
    def conn(self):
        return self.__conn

    def get_hash(self, stmt, generator=False):
        ret = self.conn.keys(pattern=stmt)
        if generator:
            ret = (self.conn.hgetall(k) for k in ret)
            return ret
        ret = [self.conn.hgetall(k) for k in ret]
        return ret

    def set_hash(self, name, key, value):
        self.conn.hset(name, key, value)

    def set_hash_m(self, name, items):
        self.conn.hmset(name, items)

    def del_key(self, name):
        self.conn.delete(name)

    def del_hash(self, name, key):
        self.conn.hdel(name, key)

    def disconnect(self):
        self.conn.connection_pool.disconnect()

    @staticmethod
    def help():
        return """
        db = Db()

        # fazendo a conexao
        print(db.conn)
        
        # pegando os dados HGET - hash
        ret = db.get_hash('usuarios:*')
        
        # mostrando os dados
        print(ret)
        print(str(ret[0][b'name'], 'utf-8', 'ignore'))
        
        # setando com HASH
        db.set_hash("nomes:1", "nome", "Jade Picon")
        
        # setando com HMSET
        #db.set_hash_m("nomes:2", {"nome": "Sabrina Torres", "idade": 18})
        
        # Mostrando dados com HMSET
        ret = db.get_hash('nomes:2')
        print(str(ret[0][b'nome'], 'utf-8', 'ignore'))
        
        # Deletando KEY
        db.del_key("peso")
        
        # Deletando hash
        db.del_hash("gatas2:", "nome")
        
        # Buscando com generator
        ret = db.get_hash("carros:1", generator=True)
        print(ret)
        """
