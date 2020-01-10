from Sql import Sql
from Utils import Utils

Utils.header()

sql = Sql()
while (q := int(input("# "))) != 99:
    if q == 0:
        cmd = input("$# ")
        ret = sql.select(cmd)
        print(ret)
        continue
    if q == 1:
        cmd = input("@# ")
        sql.query(cmd)
        continue
    if q == 2:
        Utils.header()
        continue


