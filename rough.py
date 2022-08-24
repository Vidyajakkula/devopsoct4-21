import psycopg2
base = psycopg2.connect(  # the database is assigned by dbase
    host='localhost',
    dbname='sample',
    user='postgres',
    password='Vidya_98',
    port=5432)

cursor=base.cursor()
cursor.execute("select * from asset where reserved=%s or reserved=%s",[False,'null'])
res=cursor.fetchall()
print(res)