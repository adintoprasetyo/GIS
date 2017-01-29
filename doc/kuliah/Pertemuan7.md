Menjalankan Map Proxy dan Map Server

Latar Belakang Masalah:
Siapa yang tidak tahu google maps, penggunaannya di Indonesia maupun dunia sudah menjadi kebutuhan pokok banyak orang, dalam pemanfaatan geografis pada sistem digital ada berbagai macam cara, bahkan sudah sampai ada yang menyediakan map yang dapat kita custom sesuai dengan keinginan kita, yaitu "Google Maps". tetapi apakah kalian tahu bahwa kita dapat membuat Maps Custom kita sendiri

Cara menjalankan Map Proxy dan Map Server

Solusi Masalah:
1: Kita perlu mempersiapkan terlebih dahulu agar bisa ditampilkan nantinya di Map Proxy. Kalian bisa mendownload data geospasial di situs ini. http://www.halaman.download/ pilih "Procedure" dan klik " Indonesia Mapproxy".
2. Jika sudah download ekstrak file tersebut (Penting: Ketahui dimana anda mengekstrak file tersebut karena path-nya akan digunakan untuk mengedit file yang ada di direktori yang telah di ekstrak tersebut, Disini saya simpan di direktori Downloads (Huruf kecil dan besar harus diperhatikan)
3. Pada file indomap ->  mapproxy, akan terdapat 3 file. Buka agm.yaml
4. Pada file agm.yaml, edit beberapa baris ini sesuai dengan direktori tempat anda menyimpan file tersebut:
- pada baris binary: /usr/libexec/mapserver ubah menjadi binary: /usr/lib/cgi-bin/mapserv
- pada baris map: var/mapdata/mapfile/indo.map ubah menjadi map: /home/dinto/Downloads/indomap/mapfile/indo.map
- kemudian direktori baru dengan nama tmp pada direktori indomap ubah baris working_dir: /var/mapdata/tmp menjadi /home/dinto/Downloads/indomap/tmp kemudian Save
5. Kemudian pada direktori mapproxy(di terminal/cmd), gunakan perintah:
vi mapproxy.ini
edit baris chdir=/var/mymapproxy/ menjadi chdir=/home/dinto/Downloads/indomap/mapproxy kemudian Save
6. Ubah file config.py pada direktori mapproxy ubah application = make_wsgi_app(r'/var/mymapproxy/agm.yaml') menjadi application = make_wsgi_app(r'/home/dinto/Downloads/indomap/mapproxy/agm.yaml')
7. Untuk menjalankan programnya gunakan perintah uwsgi mapproxy.ini
8. Untuk cek apakah mapproxy sudah terinstall atau belum, buka browser kemudian ketik localhost:8000
9. Klik demo atau ketik localhost:8000/demo
10. Pada bagian WMTS klik dibawah Image Format yaitu.png
11. Tunggu beberapa saat karena datanya sedang di proses.
12. Map Peta akan tampil

Penutup
Kesimpulan
Jadi para pertemuan 7 ini, kita dapat mengetahui bagaimana cara menjalankan map server dan map proxy di dalam sistem operasi ubuntu

Saran
Lebih banyak mempelajari lebih dalam lagi, dengan mencari referensi internet maupun dibuku yang berkaitan dengan materi.
Nama: Adinto Prasetyo
Kelas: D4 3A Teknik Informatika
NPM:1144018

Link Github;//github.com/adintoprasetyo/GIS
Link Plagiarisme:
https://drive.google.com/open?id=0B5xhIVMVh6huRGVHNFpoY1d3dms
https://drive.google.com/open?id=0B5xhIVMVh6hub3Bnbl9VZ25lQkU
Referensi:
https://mapproxy.org/
https://dennycharter.wordpress.com/2008/05/09/cara-kerja-mapserver/