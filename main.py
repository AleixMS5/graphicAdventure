import psycopg2
from bd import config
conn=None
esticA="1"
while (True):
    print("hola , digues mirar per veure on estas")

    pepe=input()

    if (pepe=="mirar"):
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("select descripcio from localització where id ="+esticA)

            row = cur.fetchone()
            while row is not None:
                print("'\033[0;34;40m" +str(row))

                row = cur.fetchone()
            cur.close()
            cur = conn.cursor()
            cur.execute("select nom from localització where id ="+esticA)

            row = cur.fetchone()
            while row is not None:
                print("'\033[0;34;40m" + str(row))

                row = cur.fetchone()
            cur.close()
            cur = conn.cursor()
            cur.execute("select sortides from localització where id ="+esticA)

            row = cur.fetchone()
            while row is not None:
                print("'\033[1;35m" + str(row))

                row = cur.fetchone()
            cur.close()

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    if (pepe == "anar"):

        print("hola, on vols anar?")
        esticA=input()
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select descripcio from localització where id ="+esticA)

        row = cur.fetchone()
        while row is not None:
            print("'\033[0;34;40m" + str(row))

            row = cur.fetchone()
        cur.close()
        cur = conn.cursor()
        cur.execute("select nom from localització where id ="+esticA)

        row = cur.fetchone()
        while row is not None:
            print("'\033[0;34;40m" + str(row))

            row = cur.fetchone()
        cur.close()
        cur = conn.cursor()
        cur.execute("select sortides from localització where id ="+esticA)

        row = cur.fetchone()
        while row is not None:
            print("'\033[1;35m" + str(row))

            row = cur.fetchone()
        cur.close()
