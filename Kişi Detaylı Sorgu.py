import mysql.connector
import os

try:
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
                                    
    Kişi Detaylı Sorgu      DC: .zyix
    """)

    tc_input = input("TC girin (boş bırakabilirsiniz): ").strip() or None
    isim_input = input("İsim (ADI) girin (boş bırakabilirsiniz): ").strip() or None
    soyisim_input = input("Soyisim (SOYADI) girin (boş bırakabilirsiniz): ").strip() or None
    dogum_tarihi_input = input("Doğum tarihi girin (boş bırakabilirsiniz): ").strip() or None
    nufus_il_input = input("Nüfus il girin (boş bırakabilirsiniz): ").strip() or None
    nufus_ilce_input = input("Nüfus ilçe girin (boş bırakabilirsiniz): ").strip() or None
    anne_adi_input = input("Anne adı girin (boş bırakabilirsiniz): ").strip() or None
    anne_tc_input = input("Anne TC girin (boş bırakabilirsiniz): ").strip() or None
    baba_adi_input = input("Baba adı girin (boş bırakabilirsiniz): ").strip() or None
    baba_tc_input = input("Baba TC girin (boş bırakabilirsiniz): ").strip() or None

    sorgu = "SELECT * FROM `101m` WHERE 1=1"
    sorgu_degerler = []

    if tc_input:
        sorgu += " AND TC = %s"
        sorgu_degerler.append(tc_input)
    if isim_input:
        sorgu += " AND ADI = %s"
        sorgu_degerler.append(isim_input)
    if soyisim_input:
        sorgu += " AND SOYADI = %s"
        sorgu_degerler.append(soyisim_input)
    if dogum_tarihi_input:
        sorgu += " AND DOGUMTARIHI = %s"
        sorgu_degerler.append(dogum_tarihi_input)
    if nufus_il_input:
        sorgu += " AND NUFUSIL = %s"
        sorgu_degerler.append(nufus_il_input)
    if nufus_ilce_input:
        sorgu += " AND NUFUSILCE = %s"
        sorgu_degerler.append(nufus_ilce_input)
    if anne_adi_input:
        sorgu += " AND ANNEADI = %s"
        sorgu_degerler.append(anne_adi_input)
    if anne_tc_input:
        sorgu += " AND ANNETC = %s"
        sorgu_degerler.append(anne_tc_input)
    if baba_adi_input:
        sorgu += " AND BABAADI = %s"
        sorgu_degerler.append(baba_adi_input)
    if baba_tc_input:
        sorgu += " AND BABATC = %s"
        sorgu_degerler.append(baba_tc_input)

    cursor.execute(sorgu, tuple(sorgu_degerler))
    kisi_bilgileri = cursor.fetchall()

    if kisi_bilgileri:
        dosya_adi = f"sonuc_bilgileri.txt"
        with open(dosya_adi, "w") as dosya:
            for i, kisi in enumerate(kisi_bilgileri, start=1):
                dosya.write(f"Kişi {i}:\n")
                dosya.write(f"TC: {kisi.get('TC', '')}\n")
                dosya.write(f"İsim: {kisi.get('ADI', '')}\n")
                dosya.write(f"Soyisim: {kisi.get('SOYADI', '')}\n")
                dosya.write(f"Doğum Tarihi: {kisi.get('DOGUMTARIHI', '')}\n")
                dosya.write(f"Nüfus İl: {kisi.get('NUFUSIL', '')}\n")
                dosya.write(f"Nüfus İlçe: {kisi.get('NUFUSILCE', '')}\n")
                dosya.write(f"Anne Adı: {kisi.get('ANNEADI', '')}\n")
                dosya.write(f"Anne TC: {kisi.get('ANNETC', '')}\n")
                dosya.write(f"Baba Adı: {kisi.get('BABAADI', '')}\n")
                dosya.write(f"Baba TC: {kisi.get('BABATC', '')}\n")
                dosya.write("\n")
        print(f"{dosya_adi} dosyası oluşturuldu.")
    else:
        print("Bu kriterlerde bir kişi bulunamadı.")

except mysql.connector.Error as err:
    print(f"Bir hata oluştu: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
