import psycopg2
from bd import config
conn=None
try:

    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    pepe=input()
    cur.execute("select * from localització where id="+pepe)
    row = cur.fetchone()
    while row is not None:
        print(row[3])

        row = cur.fetchone()
    cur.close()
except(Exception, psycopg2.DatabaseError) as error:
    print(error)