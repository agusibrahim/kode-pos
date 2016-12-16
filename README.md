## Indonesian post codes scraper, data taken from www.nomor.net
Kode Pos Indonesia, data diambil dari www.nomor.net
Data meliputi Kode Pos, Nama Kelurahan, Kecamatan, Jenis tingkat daerah, Kota, dan Provinsi. Data pertanggal 16 Desember 2016 berjumlah 82509. 
Tool ini berguna untuk mengambil data daerah dari situs www.nomor.net, parsing manual dari halaman webnya. Data yang dihasilkan berupa CSV dan SQLite clean/bersih. Namun untuk kamu yang males scraping, disini saya sediakan data siap pakai berupa CSV dan SQLite nya.
## Persiapan
Alat utama yang dibutuhkan untuk scraping www.nomor.net yaitu Python, disarankan memakai sistem berspek tinggi karena proses scraping membutuhkan proses yang lumayan lama. Lengkapnya seperti ini
* Python 2.7
* Modul Beautifulsoup4 dan Requests
* csv2sqlite dari https://github.com/rufuspollock/csv2sqlite (sudah ada didalam)

## Memulai
Untuk kamu yang memakai CPU atau koneksi internet pas-pasan, disarankan melakukannya di server menggunakan ssh/telnet. Saya sendiri menggunakan console dari Heroku memakan waktu kurang lebih 10 menit. 
Jalankan perintah:
```
python kodepos.py
```
Maka proses akan dimulai. Data akan disimpan sebagai data.csv dan data.db. Atau kamu bisa mengkustom nama maupun data buffer dengan cara
```
python kodepos.py <buffer> <out>
```
Buffer secara default berisi 1000, dan out defaultnya data.csv
## Keterbatasan
Ini bukanlah download instan, tapi data perlu diolah agar menjadi data yang bersih sehingga siap untuk digunakan. Jadi, proses akan sedikit memakan waktu. Dan mungkin saja akan terjadi error dimasa mendatang dikarenakan perubahan data halaman web dari www.nomor.net
## Credits
* http://www.nomor.net
* https://github.com/rufuspollock/csv2sqlite
* http://www.crummy.com/software/BeautifulSoup
* http://python-requests.org
## 
## Author: [Agus Ibrahim](http://mynameisagoes)