import pymysql
from sqlalchemy import create_engine


def db_conn(host,port,user,password,db_name):
    try:
        conn=pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=db_name,
            charset='utf8',
        )
        print('Database connection succeeded！')
        return conn

    except pymysql.Error as e:
        print('Database connection failed! ')
        print('mysql.Error: ',e.args[0],e.args[1])

def db_cur(conn):
    cur=conn.cursor()
    return cur

def db_close(cur,conn):
    cur.close()

    conn.commit()

    conn.close()

def db_insert_datas(sql, cur, list_datas):
    try:
        result=cur.executemany(sql,list_datas)
        print('Batch insert affected rows：', result)
    except Exception as e:
        print('db_insert_datas error: ', e.args)


def db_delete_datas(sql,cur,list_datas):
    try:
        result=cur.executemany(sql,list_datas)
        print('Batch insert affected rows：',result)
    except Exception as e:
        print('db_delete_datas error: ',e.args)

def db_query_datas(sql):
    cur.execute(sql)
    res1 = cur.fetchall()
    return res1

host = 'localhost'
port = 3306
user = 'root'
password = '971005'
db = 'wifi'

conn = db_conn(host, port, user, password, db)
cur=db_cur(conn)

'''
cur.execute("create table wifi_distance1(name varchar(50), distance varchar(50))character set utf8;")
cur.execute("create table wifi_distance2(name varchar(50), distance varchar(50))character set utf8;")
cur.execute("create table wifi_distance3(name varchar(50), distance varchar(50))character set utf8;")
cur.execute("create table wifi_distance4(name varchar(50), distance varchar(50))character set utf8;")
cur.execute("create table wifi_locate(x varchar(50), y varchar(50), z varchar(50))character set utf8;")
'''

# insert
'''insert_datas_sql = "insert into wifi_distance2 values(%s,%s);"
from run import dist1
db_insert_datas(insert_datas_sql,cur,dist1)
conn.commit()'''

# query
'''sql="select * from wifi_distance;"
cur.execute(sql)
res3=cur.fetchall()
print(res3)'''



