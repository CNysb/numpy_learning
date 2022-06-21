import pymysql
import random


n = 1
db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='test'
)

while n < 1000:
    n += 1

    cursor = db.cursor()

    sql = 'insert into tasks (price, name) values(%s, %s)'

    t_id = n
    name = f'username{t_id}'

    cursor.execute(sql, (t_id, name))

    db.commit()

    cursor.close()

db.close()



