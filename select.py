import psycopg2
from bd import config
conn=None
try:
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    idloca = input()
    cur.execute("select * from localització where id= "+idloca+";")

    row = cur.fetchone()
    while row is not None:
        print('\033[0;34;40m'+row[1])

        row = cur.fetchone()
    cur.close()
except(Exception, psycopg2.DatabaseError) as error:
    print(error)