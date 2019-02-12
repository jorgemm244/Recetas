import sqlite3


class Base_de_Datos:
    def __init__(self):
        self.bd = sqlite3.connect("recetas.db")
        self.c = self.bd.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS materia_prima ("
                       "ID INTEGER PRYMARY KEY AUTOINCREMENT, "
                       "ingrediente TEXT")
        self.crear_tabla()