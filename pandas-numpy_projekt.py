#%% direkt

import pandas
import numpy
import random

id = []
produkt = []
preis = []
brutto = []
for i in range(100):
    id.append(i+1)
    produkt.append(random.choice(["Brot", "Käse", "Honig"]))
    preis.append(random.uniform(1, 4))
    brutto.append(preis[i]*1.07)
rechnung = (pandas.DataFrame({"id": id, "produktname": produkt, "preis": numpy.array(preis).round(2), "brutto 7%": numpy.array(brutto).round(2)}))
rechnung.set_index("id", inplace=True)
rechnung.to_csv(".\\rechnung.csv", ":")
print(rechnung)

#%% mit Funktionen

import pandas
import numpy
import random

def vorbereitung():
    id = []
    produkt = []
    preis = []
    brutto = []
    for i in range(100):
        id.append(i+1)
        produkt.append(random.choice(["Brot", "Käse", "Honig"]))
        preis.append(random.uniform(1, 4))
        brutto.append(preis[i]*1.07)
    return id, produkt, preis, brutto
def rechnung_erstellen(id, produkt, preis, brutto):
    rechnung = (pandas.DataFrame({"id": id, "produktname": produkt, "preis": numpy.array(preis).round(2), "brutto 7%": numpy.array(brutto).round(2)}))
    rechnung.set_index("id", inplace=True)
    rechnung.to_csv(".\\rechnung_funktion.csv", ";")
    return rechnung
def main():
    id, produkt, preis, brutto = vorbereitung()
    rechnung = rechnung_erstellen(id, produkt, preis, brutto)
    print(rechnung)
if __name__ == "__main__":
    main()

#%% mit Klassen und Methoden

import pandas
import numpy
import random

class Rechnung:
    def __init__(self, id, produkt, preis, brutto):
        self.__datenframe = (pandas.DataFrame({"id": id, "produktname": produkt, "preis": numpy.array(preis).round(2), "brutto 7%": numpy.array(brutto).round(2)}))
        self.__datenframe.set_index("id", inplace=True)
    def get_datenframe(self):
        return self.__datenframe
    def csv_erstellen(self):
        self.__datenframe.to_csv(".\\rechnung_klasse.csv", "|")
def vorbereitung():
    id = []
    produkt = []
    preis = []
    brutto = []
    for i in range(100):
        id.append(i + 1)
        produkt.append(random.choice(["Brot", "Käse", "Honig"]))
        preis.append(random.uniform(1, 4))
        brutto.append(preis[i] * 1.07)
    return id, produkt, preis, brutto
def main():
    id, produkt, preis, brutto = vorbereitung()
    rechnung = Rechnung(id.copy(), produkt.copy(), preis.copy(), brutto.copy())
    rechnung.csv_erstellen()
    print(rechnung.get_datenframe())
if __name__ == "__main__":
    main()

#%% SQLite Datenbank

import pandas
import numpy
import random
import sqlite3

def vorbereitung():
    id = []
    produkt = []
    preis = []
    brutto = []
    for i in range(100):
        id.append(i+1)
        produkt.append(random.choice(["Brot", "Käse", "Honig"]))
        preis.append(random.uniform(1, 4))
        brutto.append(preis[i]*1.07)
    return id, produkt, preis, brutto
def rechnung_erstellen(id, produkt, preis, brutto):
    rechnung = (pandas.DataFrame({"id": id, "produktname": produkt, "preis": numpy.array(preis).round(2), "brutto 7%": numpy.array(brutto).round(2)}))
    return rechnung
def sqlite_datenbank_erstellen():
    conn = sqlite3.connect('Pandas.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rechnung(id INTEGER,
    produkt TEXT, preis FLOAT, brutto FLOAT)''')
    conn.commit()
    conn.close()
def sqlite_datenbank_füllen(rechnung):
    conn = sqlite3.connect('Pandas.db')
    c = conn.cursor()
    sql = '''INSERT INTO rechnung (id, produkt, preis, brutto) VALUES (?, ?, ?, ?)'''
    for i in rechnung["id"]:
        params = (i, rechnung["produktname"][i-1], rechnung["preis"][i-1], rechnung["brutto 7%"][i-1])
        c.execute(sql, params)
        conn.commit()
    conn.close()
def main():
    id, produkt, preis, brutto = vorbereitung()
    rechnung = rechnung_erstellen(id, produkt, preis, brutto)
    sqlite_datenbank_erstellen()
    sqlite_datenbank_füllen(rechnung)
    rechnung.set_index("id", inplace=True)
    print(rechnung)
if __name__ == "__main__":
    main()