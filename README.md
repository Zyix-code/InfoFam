# 🔍 PersonQuery Tool – Gelişmiş Aile ve Kişi Sorgulama Sistemi

<p align="center">
  <img src="https://media.giphy.com/media/Y4ak9Ki2GZCbJxAnJD/giphy.gif" width="150px">
</p>

<p align="center">
  <b>Python ve MySQL altyapısı ile geliştirilmiş, yerel veritabanı üzerinden çalışan detaylı veri sorgulama aracı.</b><br>
  Kişi, aile ve detaylı kütük bilgilerine hızlı ve güvenli erişim sağlar.
</p>

---

## 🚀 Özellikler

- ✔ **Aile Sorgu:** T.C. veya soyadı üzerinden aile bireylerini listeleme ve bağları görüntüleme.
- ✔ **Kişi Sorgu:** Tekil kişiler için temel kimlik bilgilerini hızlıca getirme.
- ✔ **Detaylı Sorgu:** Seçilen kişinin tüm veritabanı kayıtlarına ve ilişkili verilerine derinlemesine erişim.
- ✔ **Yapılandırılabilir Sistem:** `settings.json` dosyası üzerinden veritabanı bağlantı ayarlarını kolayca yönetme.

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white&style=flat-square">
  <img src="https://img.shields.io/badge/Database-MySQL-4479A1?logo=mysql&logoColor=white&style=flat-square">
  <img src="https://img.shields.io/badge/Config-JSON-000000?logo=json&logoColor=white&style=flat-square">
  <img src="https://img.shields.io/badge/License-GPLv3-blue.svg?style=flat-square">
</p>

---

## 🧠 Sistem Nasıl Çalışır?

Uygulama, yerel sunucu (localhost) üzerinde çalışan MySQL veritabanı ile haberleşir:

### 1️⃣ Bağlantı (Connection)
- Program başlatıldığında `settings.json` dosyasını okur.
- Buradaki `Host`, `User`, `Password` ve `Database` bilgileri ile MySQL sunucusuna bağlanır.

### 2️⃣ Sorgu İşleme (Query Execution)
- Kullanıcının seçtiği modüle göre (Aile, Kişi vb.) dinamik SQL sorguları oluşturulur.
- Veritabanından dönen ham veriler işlenerek kullanıcıya okunabilir formatta sunulur.

---

## 🛠️ Kurulum ve Kullanım

### 1️⃣ Gereksinimler
- Python 3.x
- MySQL Server (Localhost)
- Gerekli Python kütüphaneleri (örn: `mysql-connector-python`)

### 2️⃣ Yapılandırma
Proje dizinindeki `settings.json` dosyasını kendi veritabanı bilgilerinizle düzenleyin:

```json
{
  "host": "localhost",
  "user": "root",
  "password": "YOUR_PASSWORD",
  "database": "db_name"
}```


## 3️⃣ Çalıştırma
Terminal veya komut satırını açarak ana dosyayı çalıştırın:

```bash
python main.py
```

⚖️ Lisans
Bu proje GNU General Public License v3.0 ile lisanslanmıştır. Projenin tüm kullanıcıları, lisansın koşullarına uymak kaydıyla projeyi özgürce kullanabilir, değiştirebilir ve paylaşabilir.

🤝 İletişim
<p align="left"> <a href="https://discordapp.com/users/481831692399673375"><img src="https://img.shields.io/badge/Discord-Zyix%231002-7289DA?logo=discord&style=flat-square"></a> <a href="https://www.youtube.com/channel/UC7uBi3y2HOCLde5MYWECynQ?view_as=subscriber"><img src="https://img.shields.io/badge/YouTube-Subscribe-red?logo=youtube&style=flat-square"></a> <a href="https://www.reddit.com/user/_Zyix"><img src="https://img.shields.io/badge/Reddit-Profile-orange?logo=reddit&style=flat-square"></a> <a href="https://open.spotify.com/user/07288iyoa19459y599jutdex6"><img src="https://img.shields.io/badge/Spotify-Follow-green?logo=spotify&style=flat-square"></a> </p>
