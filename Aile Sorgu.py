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
      / /__    \\ |   _| |_ / . \\     
     /_____|   |_|  |_____/_/ \\_\\    
                                    
    Detaylı Aile Sorgu     DC: .zyix
    """)

    # Kullanıcı girişlerini alıyoruz
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

    # Sorguyu oluşturuyoruz
    sorgu = "SELECT * FROM `101m` WHERE 1=1"
    sorgu_degerler = []

    if not any([tc_input, isim_input, soyisim_input, dogum_tarihi_input, nufus_il_input, nufus_ilce_input, anne_adi_input, anne_tc_input, baba_adi_input, baba_tc_input]):
        print("Hata: En az bir kriter girmelisiniz!")
    else:
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
        kisi_bilgisi = cursor.fetchone()

        if kisi_bilgisi:
            print(f"Kişi bulundu: {kisi_bilgisi['ADI']} {kisi_bilgisi['SOYADI']}")

            anne_tc = kisi_bilgisi.get("ANNETC")
            baba_tc = kisi_bilgisi.get("BABATC")

            dosya_adi = f"{kisi_bilgisi['ADI']}_{kisi_bilgisi['SOYADI']}_aile_bilgileri.txt"
            with open(dosya_adi, "w") as dosya:

                dosya.write(f"Kişi: {kisi_bilgisi['ADI']} {kisi_bilgisi['SOYADI']}\n")
                dosya.write(f"TC: {kisi_bilgisi['TC']}\n")
                
                # Anne bilgisi
                dosya.write("\nAile Bilgisi:\n")
                if anne_tc:
                    cursor.execute("SELECT * FROM `101m` WHERE TC = %s", (anne_tc,))
                    anne_bilgisi = cursor.fetchone()
                    if anne_bilgisi:
                        dosya.write(f"Anne: {anne_bilgisi['ADI']} {anne_bilgisi['SOYADI']}, TC: {anne_bilgisi['TC']}\n")
                    else:
                        dosya.write("Anne bilgisi bulunamadı.\n")
                else:
                    dosya.write("Anne bilgisi yok.\n")
                
                # Baba bilgisi
                if baba_tc:
                    cursor.execute("SELECT * FROM `101m` WHERE TC = %s", (baba_tc,))
                    baba_bilgisi = cursor.fetchone()
                    if baba_bilgisi:
                        dosya.write(f"Baba: {baba_bilgisi['ADI']} {baba_bilgisi['SOYADI']}, TC: {baba_bilgisi['TC']}\n")
                    else:
                        dosya.write("Baba bilgisi bulunamadı.\n")
                else:
                    dosya.write("Baba bilgisi yok.\n")

                # Kardeş bilgisi
                dosya.write("\nKARDEŞ BİLGİLERİ\n")
                if anne_tc and baba_tc:
                    cursor.execute("SELECT * FROM `101m` WHERE ANNETC = %s AND BABATC = %s AND TC != %s", (anne_tc, baba_tc, kisi_bilgisi['TC']))
                    kardesler = cursor.fetchall()
                    if kardesler:
                        for kardes in kardesler:
                            dosya.write(f"Kardeş: {kardes['ADI']} {kardes['SOYADI']}, TC: {kardes['TC']}\n")
                    else:
                        dosya.write("Kardeşi yok.\n")
                else:
                    dosya.write("Kardeş bilgisi yok.\n")

                # Çocuk bilgisi
                dosya.write("\nÇocuk Bilgileri:\n")
                cursor.execute("SELECT * FROM `101m` WHERE ANNETC = %s OR BABATC = %s", (kisi_bilgisi['TC'], kisi_bilgisi['TC']))
                cocuklar = cursor.fetchall()
                if cocuklar:
                    for cocuk in cocuklar:
                        dosya.write(f"Çocuk: {cocuk['ADI']} {cocuk['SOYADI']}, TC: {cocuk['TC']}\n")
                else:
                    dosya.write("Çocuk bilgisi yok.\n")

                # Babaannesi ve Dedesi (Baba Tarafı)
                dosya.write("\nBaba Tarafı Büyük Ebeveynler:\n")
                if baba_tc:
                    cursor.execute("SELECT * FROM `101m` WHERE TC = %s", (baba_tc,))
                    baba_bilgisi = cursor.fetchone()
                    if baba_bilgisi:
                        # Babaannesi
                        if baba_bilgisi.get('ANNETC'):
                            cursor.execute("SELECT * FROM `101m` WHERE TC = %s", (baba_bilgisi['ANNETC'],))
                            babaanne_bilgisi = cursor.fetchone()
                            if babaanne_bilgisi:
                                dosya.write(f"Babaannesi: {babaanne_bilgisi['ADI']} {babaanne_bilgisi['SOYADI']}, TC: {babaanne_bilgisi['TC']}\n")
                            else:
                                dosya.write("Babaannesi bilgisi bulunamadı.\n")
                        # Dedesi
                        if baba_bilgisi.get('BABATC'):
                            cursor.execute("SELECT * FROM `101m` WHERE TC = %s", (baba_bilgisi['BABATC'],))
                            dede_bilgisi = cursor.fetchone()
                            if dede_bilgisi:
                                dosya.write(f"Dedesi: {dede_bilgisi['ADI']} {dede_bilgisi['SOYADI']}, TC: {dede_bilgisi['TC']}\n")
                            else:
                                dosya.write("Dedesi bilgisi bulunamadı.\n")

                # Anneannesi ve Dedesi (Anne Tarafı)
                dosya.write("\nAnne Tarafı Büyük Ebeveynler:\n")
                if anne_tc:
                    cursor.execute("SELECT * FROM `101m` WHERE TC = %s", (anne_tc,))
                    anne_bilgisi = cursor.fetchone()
                    if anne_bilgisi:
                        # Anneannesi
                        if anne_bilgisi.get('ANNETC'):
                            cursor.execute("SELECT * FROM `101m` WHERE TC = %s", (anne_bilgisi['ANNETC'],))
                            anneanne_bilgisi = cursor.fetchone()
                            if anneanne_bilgisi:
                                dosya.write(f"Anneannesi: {anneanne_bilgisi['ADI']} {anneanne_bilgisi['SOYADI']}, TC: {anneanne_bilgisi['TC']}\n")
                            else:
                                dosya.write("Anneannesi bilgisi bulunamadı.\n")
                        # Dedesi
                        if anne_bilgisi.get('BABATC'):
                            cursor.execute("SELECT * FROM `101m` WHERE TC = %s", (anne_bilgisi['BABATC'],))
                            anne_dede_bilgisi = cursor.fetchone()
                            if anne_dede_bilgisi:
                                dosya.write(f"Dedesi: {anne_dede_bilgisi['ADI']} {anne_dede_bilgisi['SOYADI']}, TC: {anne_dede_bilgisi['TC']}\n")
                            else:
                                dosya.write("Dedesi bilgisi bulunamadı.\n")
                                
                # Anne Tarafı Kardeşler (Dayılar ve Teyzeler)
                dosya.write("\nAnne Tarafı Kardeşler (Dayı ve Teyzeler):\n")
                if anne_tc:
                    cursor.execute("SELECT * FROM `101m` WHERE ANNETC = %s AND TC != %s", (anne_bilgisi['ANNETC'], anne_bilgisi['TC']))
                    anne_tarafi_kardesler = cursor.fetchall()
                    if anne_tarafi_kardesler:
                        for kardes in anne_tarafi_kardesler:
                            dosya.write(f"Dayı/Teyze: {kardes['ADI']} {kardes['SOYADI']}, TC: {kardes['TC']}\n")
                    else:
                        dosya.write("Anne tarafında kardeş yok.\n")

                # Baba Tarafı Kardeşler (Amcalar ve Halalar)
                dosya.write("\nBaba Tarafı Kardeşler (Amca ve Halalar):\n")
                if baba_tc:
                    cursor.execute("SELECT * FROM `101m` WHERE BABATC = %s AND TC != %s", (baba_bilgisi['BABATC'], baba_bilgisi['TC']))
                    baba_tarafi_kardesler = cursor.fetchall()
                    if baba_tarafi_kardesler:
                        for kardes in baba_tarafi_kardesler:
                            dosya.write(f"Amca/Hala: {kardes['ADI']} {kardes['SOYADI']}, TC: {kardes['TC']}\n")
                    else:
                        dosya.write("Baba tarafında kardeş yok.\n")

                # Baba Tarafı Kuzenler (Amca ve Hala Çocukları)
                dosya.write("\nBaba Tarafı Kuzenler (Amca ve Hala Çocukları):\n")
                if baba_tc and baba_tarafi_kardesler:
                    baba_tarafi_kuzenler_var = False
                    for kardes in baba_tarafi_kardesler:
                        cursor.execute("SELECT * FROM `101m` WHERE ANNETC = %s OR BABATC = %s", (kardes['TC'], kardes['TC']))
                        kuzenler = cursor.fetchall()
                        if kuzenler:
                            baba_tarafi_kuzenler_var = True
                            for kuzen in kuzenler:
                                dosya.write(f"Kuzen: {kuzen['ADI']} {kuzen['SOYADI']}, TC: {kuzen['TC']}\n")
                    if not baba_tarafi_kuzenler_var:
                        dosya.write("Baba tarafı kuzeni yok.\n")

                # Anne Tarafı Kuzenler (Dayı ve Teyze Çocukları)
                dosya.write("\nAnne Tarafı Kuzenler (Dayı ve Teyze Çocukları):\n")
                if anne_tc and anne_tarafi_kardesler:
                    anne_tarafi_kuzenler_var = False
                    for kardes in anne_tarafi_kardesler:
                        cursor.execute("SELECT * FROM `101m` WHERE ANNETC = %s OR BABATC = %s", (kardes['TC'], kardes['TC']))
                        kuzenler = cursor.fetchall()
                        if kuzenler:
                            anne_tarafi_kuzenler_var = True
                            for kuzen in kuzenler:
                                dosya.write(f"Kuzen: {kuzen['ADI']} {kuzen['SOYADI']}, TC: {kuzen['TC']}\n")
                    if not anne_tarafi_kuzenler_var:
                        dosya.write("Anne tarafı kuzeni yok.\n")

            print(f"{dosya_adi} dosyası oluşturuldu.")
        else:
            print("Bu kriterlere uygun bir kişi bulunamadı.")
        
except mysql.connector.Error as err:
    print(f"Bir hata oluştu: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
