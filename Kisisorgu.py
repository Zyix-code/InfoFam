import mysql.connector
import os

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="zyix101mdata"
)

cursor = conn.cursor(dictionary=True)
os.system("cls" if os.name == "nt" else "clear")
print("""
 ________     _________   __     
 |___  /\\ \\   / /_   _\\ \\ / /    
    / /  \\ \\_/ /  | |  \\ V /     
   / /    \\   /   | |   > <      
  / /__    | |   _| |_ / . \\     
 /_____|   |_|  |_____/_/ \\_\\    
                                
Kişi Sorgu      DC: .zyix
""")

isim_input = input("İsim (ADI) girin: ")
soyisim_input = input("Soyisim (SOYADI) girin: ")

sorgu = "SELECT * FROM `101m` WHERE ADI = %s AND SOYADI = %s"
cursor.execute(sorgu, (isim_input, soyisim_input))

kisi_bilgileri = cursor.fetchall()

if kisi_bilgileri:
    dosya_adi = f"{isim_input}_{soyisim_input}_bilgi.txt"
    with open(dosya_adi, "w") as dosya:
        for i, kisi in enumerate(kisi_bilgileri, start=1):
            dosya.write(f"Kişi {i}:\n")
            dosya.write(f"İsim: {kisi['ADI']}\n")
            dosya.write(f"Soyisim: {kisi['SOYADI']}\n")
            dosya.write(f"TC: {kisi['TC']}\n")
            dosya.write(f"Doğum Tarihi: {kisi['DOGUMTARIHI']}\n")
            dosya.write(f"Nüfus İl: {kisi['NUFUSIL']}\n")
            dosya.write(f"Nüfus İlçe: {kisi['NUFUSILCE']}\n")
            dosya.write(f"Anne Adı: {kisi['ANNEADI']}\n")
            dosya.write(f"Baba Adı: {kisi['BABAADI']}\n")
            dosya.write("\n")
    print(f"{dosya_adi} dosyası oluşturuldu.")
else:
    print("Bu isimde bir kişi bulunamadı.")

cursor.close()
conn.close()
