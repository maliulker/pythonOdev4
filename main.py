import sqlite3
from benzerlik import veritabani_olustur, metin_ekle, metin_sil


def jaccard_benzerlik(metin1, metin2):
    kume1 = set(metin1.split())
    kume2 = set(metin2.split())
    benzer_kelimeler = kume1.intersection(kume2)
    farkli_kelimeler = kume1.union(kume2)
    return len(benzer_kelimeler) / len(farkli_kelimeler)


metin1 = input("Lütfen birinci metni girin: ")
metin2 = input("Lütfen ikinci metni girin: ")

conn = sqlite3.connect('metinler.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Metinler
             (id INTEGER PRIMARY KEY, metin TEXT)''')
c.execute("INSERT INTO Metinler (metin) VALUES (?)", (metin1,))
c.execute("INSERT INTO Metinler (metin) VALUES (?)", (metin2,))
conn.commit()
conn.close()

conn = sqlite3.connect('metinler.db')
c = conn.cursor()
c.execute("SELECT metin FROM Metinler")
metinler = c.fetchall()
conn.close()

jaccard_sonucu = jaccard_benzerlik(metinler[0][0], metinler[1][0])

print("Metinler arasındaki Jaccard benzerlik katsayısı:", jaccard_sonucu)

with open("benzerlik_durumu.txt", "w") as dosya:
    dosya.write("Metinler arasındaki Jaccard benzerlik katsayısı: " + str(jaccard_sonucu))

metin_sil()