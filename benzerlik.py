import sqlite3


def baglan():
    return sqlite3.connect('metinler.db')


def veritabani_olustur():
    conn = baglan()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Metinler
                 (id INTEGER PRIMARY KEY, metin TEXT)''')
    conn.commit()
    conn.close()


def metin_ekle(metin):
    conn = baglan()
    c = conn.cursor()
    c.execute("INSERT INTO Metinler (metin) VALUES (?)", (metin,))
    conn.commit()
    conn.close()


def metin_sil():
    conn = baglan()
    c = conn.cursor()
    c.execute("DELETE FROM Metinler")
    conn.commit()
    conn.close()
