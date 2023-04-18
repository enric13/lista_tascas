#!/usr/bin/python3

import sqlite3

RUTA_BD = "ima_base_de_dades.bd"
def esborra_taulas(conn):
    consulta = "DROP table if exists tasques;"
    cursor = conn.cursor()
    cursor.execute(consulta)
    conn.commit()
    cursor.close()

def crea_taulas(conn):
    consulta = """CREATE table if not exists tasques(
    title text,
    done boolean
    );"""
    cursor = conn.cursor()
    cursor.execute(consulta)
    conn.commit()
    cursor.close()

def afegir_tasca(conn, titol, done=False):
    consulta = f"INSERT INTO tasques (title, done) VALUES('{titol}', {done});"
    cursor = conn.cursor()
    cursor.execute(consulta)
    conn.commit()
    cursor.close()

def main():
    print("Obrint connexió amb base de dades")
    conn = sqlite3.connect(RUTA_BD)
    esborra_taulas(conn)
    crea_taulas(conn)
    afegir_tasca(conn, "Anar a comprar")
    conn.close()
    print("Connexió tancada")

if __name__ == "__main__":
    main()


    