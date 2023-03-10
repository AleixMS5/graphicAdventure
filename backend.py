import psycopg2
from bd import config


def menu(taula):

        if taula=="camins"  or taula=="objectes" or taula=="localitzacions" :
            print("1:Mostrar una " + taula + ".")
            print("2:Crear una " + taula + ".")
            print("3:Modificar una " + taula + ".")
            print("4:Eliminar una " + taula + ".")
            print("5:Llistar totes les " + taula + "")
        elif taula == "protagonista":
            print("1:Mostrar una " + taula + ".")
            print("2:Crear una " + taula + ".")


        if (taula=="localitzacions"):
            executarOpcioMenuLocalitzacions()
        elif(taula=="camins"):
            executarOpcioMenucamins()
        elif(taula=="objectes"):
            executarMenuObjectes();
        elif (taula == "protagonista"):
            executarMenuProtagonista();

def executarSenencies(sentencia):
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute(sentencia)
    row = cur.fetchone()
    while row is not None:
        print(row)

        row = cur.fetchone()
    cur.close()


def executarSentenciesCommit(sentencia):
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute(sentencia)
    conn.commit()
    row = cur.fetchone()
    while row is not None:
        print(row)

        row = cur.fetchone()

    cur.close()


def mostrarLcalitzacio():
    while True:
        try:
            print('digues la id per buscar')
            id = input()
            executarSenencies("select * from localitzaci√≥ where id ='" + id + "';")

            break

        except(Exception, psycopg2.DatabaseError) as error:
            print("la id no coincideix")


def eliminarlocalitzacio():
    while True:
        try:
            print('digues la id per esborrar')
            id = input()

            executarSentenciesCommit("delete from localitzaci√≥ where id=' " + id + "';")
            break
        except(Exception, psycopg2.DatabaseError) as error:
            print("les ids son camps numerics")


def crearLocalitzacio():
    while True:
        try:
            print("digues la descripci√≥")
            descripcio = input()
            print("digues el nom ")
            nom = input()
            print("descriu les sortides")
            sortides = input()
            executarSentenciesCommit(
                "insert into localitzaci√≥(descripcio,nom,sortides) values ('" + descripcio + "','" + nom + "','" + sortides + "')")
            break
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)


def modificarLocalitzacio():
    while True:
        try:
            print('digues la id per modificar')
            id = input()
            print("digues la descripci√≥")
            descripcio = input()
            print("digues el nom ")
            nom = input()
            print("descriu les sortides")
            sortides = input()
            executarSentenciesCommit(
                "UPDATE localitzaci√≥ SET descripcio='" + descripcio + "',nom='" + nom + "',sortides='" + sortides + "' WHERE id='" + id + "';")
            break
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)


def llistarTots(taula):

        try:
            executarSenencies("select * from " + taula)

        except(Exception, psycopg2.DatabaseError) as error:
            print("les ids son camps numerics")







def executarOpcioMenuLocalitzacions():
    opcioMenu = input()
    if (opcioMenu == "1"):
        # Mostrar una localitzaci√≥.
        mostrarLcalitzacio()
    elif (opcioMenu == "2"):
        # Crear una localitzaci√≥.
        crearLocalitzacio()
    elif (opcioMenu == "3"):
        # Modificar una localitzaci√≥.
        modificarLocalitzacio()

    elif (opcioMenu == "4"):
        # Eliminar una localitzaci√≥.
        eliminarlocalitzacio()

    elif (opcioMenu == "5"):
        # Llistar totes les localitzacions.

        llistarTots("localitzaci√≥")


def mostrarcamins():
    while True:
        try:
            print("1:buscar per origen")
            print("2:buscar per desti")
            obcio = input()

            if (obcio == "1"):
                print('digues la id per buscar')
                id = input()
                executarSenencies("select * from camins where idor ='" + id + "';")
            if (obcio == "2"):
                print('digues la id per buscar')
                id = input()
                executarSenencies("select * from camins where iddest ='" + id + "';")

            break
        except(Exception, psycopg2.DatabaseError) as error:
            print("les ids no coincideixen amb cap cami")

def crearcamins():
    while True:
        try:
            print("digues la id dorigen")
            id = input()
            print("digues la id de desti ")
            id2 = input()
            print("digues el nom de l'origen")
            origen = input()
            print("digues el nom del desti")
            desti = input()
            executarSentenciesCommit(
                "insert into camins (idor,iddest,nomorigen,nomdesti) values ('" + id+ "','" + id2 + "','" + origen + "','"+desti+"')")
            break
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)


def modificarcamins():
    while True:
        try:
            print('digues la id dorigen per modificar')
            id0 = input()
            print('digues la id de desti per modificar')
            id02 = input()
            print("digues la id dorigen")
            id = input()
            print("digues la id de desti ")
            id2 = input()
            print("digues el nom de l'origen")
            origen = input()
            print("digues el nom del desti")
            desti = input()
            executarSentenciesCommit(
                "update camins  SET idor='" + id + "' ,iddest ='" + id2 + "',nomorigen='" + origen + "',nomdesti='" + desti + "' where idor=' " + id0 + "' and iddest='"+id02+"';")
            break
        except(Exception, psycopg2.DatabaseError) as error:
            print("les ids son camps numerics")
def eliminarcamins():
    while True:
        try:
            print('digues la id dorigen per esborrar')
            id = input()
            print('digues la id de desti per esborrar')
            id2 = input()

            executarSentenciesCommit("delete from camins where idor=' " + id + "' and iddest='"+id2+"';")
            break
        except(Exception, psycopg2.DatabaseError) as error:
            print("les ids son camps numerics")


def executarOpcioMenucamins():
    opcioMenu = input()
    if (opcioMenu == "1"):
        # Mostrar una localitzaci√≥.
        mostrarcamins()
    elif (opcioMenu == "2"):
        # Crear una localitzaci√≥.
        crearcamins()
    elif (opcioMenu == "3"):
        # Modificar una localitzaci√≥.
        modificarcamins()

    elif (opcioMenu == "4"):
        # Eliminar una localitzaci√≥.
        eliminarcamins()

    elif (opcioMenu == "5"):
        # Llistar totes les localitzacions.

        llistarTots("camins")


# menu("localitzaci√≥")
class  objecte:
    def __init__(self, pes,nom,descripcio,idLocalitzacio):
        self.pes = pes
        self.nom = nom
        self.descripcio = descripcio
        self.idLocalitzacio = idLocalitzacio

def mostrarObjectes():
    while True:
        try:




            print('digues la id per buscar')
            id = input()
            executarSenencies("select * from objectes where id ='" + id + "';")

            break

        except(Exception, psycopg2.DatabaseError) as error:
            print("la id no coincideix"
                  "")

def crearObjectes():
    while True:
        try:
            print("digues la id ")
            id = input()
            print("digues el pes ")
            pes = input()
            print("digues el nom de l'objecte")
            nom = input()
            print("digues la descripci√≥ del objecte")
            descripcio = input()
            print("digues la id de l'origen")
            idOrigen = input()
            executarSentenciesCommit(
                "insert into objectes VALUES  ('" +id+ "',('" + pes + "','" + nom + "','"+descripcio+"'),"+idOrigen+")")
            break
        except(Exception, psycopg2.DatabaseError) as error:
            print("les ids i el pes son camp numerics")


def modificarObjectes():
    while True:
        try:
            print("digues la id d'jecte per modificar")
            id0 = input()
            print("digues el pes de l'objecte")
            pes = input()
            print("digues el nom de l'objecte")
            nom = input()
            print("digues la descripci√≥ del objecte")
            descripcio = input()
            print("digues la id de l'origen")
            idOrigen = input()

            executarSentenciesCommit(
                "update objectes  SET  objecte.pes='"+pes+"', objecte.nom='"+nom+"', objecte.descripcio='"+descripcio+"', idlocalitzacio='"+idOrigen+"' where id='" + id0 + "' ;")
            break
        except(Exception, psycopg2.DatabaseError) as error:
            print("les ids i el pes son camp numerics")
def eliminarObjectes():
    while True:
        try:
            print('digues la id dorigen per esborrar')
            id = input()


            executarSentenciesCommit("delete from objectes where id=" + id + ";")
            break
        except(Exception, psycopg2.DatabaseError) as error:
            print("la id no existeix")



def executarMenuObjectes():
    opcioMenu = input()
    if (opcioMenu == "1"):
        # Mostrar una localitzaci√≥.
        mostrarObjectes()
    elif (opcioMenu == "2"):
        # Crear una localitzaci√≥.
        crearObjectes()
    elif (opcioMenu == "3"):
        # Modificar una localitzaci√≥.
        modificarObjectes()

    elif (opcioMenu == "4"):
        # Eliminar una localitzaci√≥.
        eliminarObjectes()

    elif (opcioMenu == "5"):
        # Llistar totes les localitzacions.

        llistarTots("objectes")

def mostrarProtagonista():

        try:

            executarSenencies("select * from protagonista ;")



        except(Exception, psycopg2.DatabaseError) as error:
            print("no hi ha protagonista")

def crearProtagonista():
    try:
        executarSentenciesCommit("delete  from protagonista;")
    except(Exception, psycopg2.DatabaseError) as error:
        print("primer protagonista")
    try:
        print("digues el nom ")
        name = input()
        print("digues la descripcio ")
        descripcio = input()

        while (True):
            print("digues el sexe ‚Äômascul√≠‚Äô, ‚Äėfemen√≠‚Äô, ‚Äėaltres‚Äô")
            sexe = input()
            if sexe=="mascul√≠"or sexe=="femen√≠" or sexe=="altres":
                break

        while (True):
            print("digues la edat")
            edat = input()
            if int(edat) > 18 and int(edat) < 99:
                break
        print("digues la altura")
        altura = input()
        print("digues el pes")
        pes = input()

        while (True):
            print("digues la for√ßa")
            for√ß = input()
            if int(for√ß) > 1 and int(for√ß) < 20:
                break

        while (True):
            print("digues la destresa")
            des = input()
            if int(des) > 1 and int(des) < 20:
                break

        while (True):
            print("digues la resistencia")
            res = input()
            if int(res)>1 and int(res)<20:
                break

        sal = res*2
        executarSentenciesCommit(
            "insert into protagonista (name,descripcio,sexe,edat,altura,pes,FORs,DESs,RESs,salut)  VALUES  ('" +name+ "','" + descripcio + "','" + sexe + "','"+edat+"','"+altura+"','"+pes+"','"+for√ß+"','"+des+"','"+res+"','"+sal+"')")

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)






def executarMenuProtagonista():
    opcioMenu = input()
    if (opcioMenu == "1"):

        mostrarProtagonista()
    elif (opcioMenu == "2"):

        crearProtagonista()




while True:
    print("digues si vols editar 'camins', 'localitzacions' o 'objectes' o 'protagonista'")
    pepe=input()
    if pepe == "camins" or pepe == "objectes" or pepe == "localitzacions" or pepe == "protagonista":
        break;
menu(pepe)

#pepe