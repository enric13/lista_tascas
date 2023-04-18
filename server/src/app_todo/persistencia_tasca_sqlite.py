#!/usr/bin/python3
import sqlite3
import tasca
class Persistencia_tasca_sqlite():
    def __init__(self, ruta):
        self._ruta = ruta
        self._conn = sqlite3.connect(self._ruta)


    def desa(self, tasca):
        titol = tasca.titol
        done = tasca.done
        resultat = None
        consulta = "INSERT INTO tasques " \
            + "(titol, done) " \
            + f"VALUES('{titol}', {done});"
                                                   
        cursor = self._conn.cursor()
        try:
            cursor.execute(consulta)
            tasca.id = cursor.lastrowid
            resultat = tasca
        except sqlite3.IntegrityError:
            print("[X]IntegrityError: possiblement aqesta tasque ya esta registrada")
        self._conn.commit()  
        cursor.close()
        return resultat

    def get_list(self):
        consulta = "SELECT rowid, titol, done, * FROM tasques;"
        cursor = self._conn.cursor()
        cursor.execute(consulta)
        llista = cursor.fetchall() 
        resultat = []
        for registre in llista:
            tarea = tasca.Tasca(self, registre[1], registre[2], registre[0])
            resultat.append(tarea)

        return resultat


def main():
    
    persistencia = Persistencia_tasca_sqlite("del
import persistencia_tasca_sqliteeteme.bd")
    una_tasca = tasca.Tasca(persistencia, "Treure a passejar al gat")
    print (persistencia.desa(una_tasca))
    tasques = persistencia.get_list()
    print("--- llista de tasques: ---")
    for taska in tasques:
        print(taska)

if __name__ =="__main__":
    main()
           