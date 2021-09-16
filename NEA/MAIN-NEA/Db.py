from os import curdir
import sqlite3
import sqlite3
conn = sqlite3.connect("Customer.db")
C = conn.cursor()

C.execute("""CREATE TABLE Customer(
            CustomerID TEXT,
            Name TEXT,
            Age INTERGER
            )""")
    
conn.commit()
conn.close()

ha = sqlite3.connect("Hairdresser.db")
h = conn.cursor()

h.execute("""CREATE TABLE Hairdresser(
            HairdresserID TEXT,
            Name TEXT,
            HairType TEXT,
            Nam TEXT,
            HairTyp TEXT,
            Na TEXT,
            HairTy TEXT,
            )""")
ha.commit()
ha.close()       