Instalasi Map Proxy dan Map Sever

Latar Belakang Masalah:
Siapa yang tidak tahu google maps, penggunaannya di indonesia maupun dunia sudah menjadi kebutuhan pokok banyak orang, dalam pemanfaatan geografis pada sistem digital ada berbagai macam cara bahkan sudah sampai ada yang menyediakan map yang dapat kita custom sesuai dengan keinginan kita sendiri yaitu Google Maps, tetapi apakah kalian tahu bahwa kita dapat membuat peta kita sendiri.

1. Apa itu Map Proxy?
2. Apa itu Map Server?
3. Bagaimana cara install Map Proxy?
4. Bagaimana cara install Map Server?

- Map Proxy (mapproxy.org) adalah open source ubin geospasial proxy yang mendukung proyeksi ulang. Awalnya dikembangkan oleh Omniscale, Maproxy adalah server proxy python untuk gambar geospasial. Hal ini dapat membaca data dari WMS, ubin, mapserver, mapnik, dan cache. Melayani data bahwa sebagai WMS, WMTS, TMS, dan KML. Hal ini juga dapat melakukan reprojections antara berbagai sistem koordinat referensi.

-Map Server adalah sebuah lingkungan pengembangan open source untuk membangun aplikasi internet spasial diaktifkan. Hal ini dapat dijalankan sebagai program CGI atau melalui Mapscript yang mendukung beberapa bahasa pemrograman (menggunakan SWIG). MapServer dikembangkan oleh University of Minnesota. Seiring dan lebih khusus disebut sebagai UMN MapServer, untuk membedakannya dari komersial  peta server. Mapserver awalnya dikembangkan dengan dukungan dari NASA, yang membutuhkan cara untuk membuat citra satelit yang tersedia untuk umum.

Installasi Map server & Map Proxy
1. Siapkan terlebih dahulu sistem operasi ubuntu (bisa menggunakan versi linux yang lain)
2. Buka terminal kemudian gunakan perintah:
sudo apt-get install cgi-mapserver
3. Untuk mengetahui struktur direktori Map Server, gunakan perintah:
dpkg -L cgi-mapserver
4. Karena saya menjalankannya menggunakan python, install python juga dengan menggunakan perintah:
sudo apt-get install python-pip python-dev
5. Install uwsgi
sudo pip install uwsgi
6. Install Map Proxy
sudo pip install MapProxy

Penutup
Kesimpulan
Jadi pertemuan 6 ini dapat mengetahui bagaimana menginstall map server dan map proxy

Saran
Lebih banyak mempelajari dengan mencari referensi di internet maupun dibuku yang berkaitan dengan materi.
Nama: Adinto Prasetyo
Kelas: D4 3A Teknik Informatika
NPM:1144018

Link Github://github.com/adintoprasetyo/GIS
Link Plagiarisme:
https://drive.google.com/open?id=0B5xhIVMVh6huRGVHNFpoY1d3dms
https://drive.google.com/open?id=0B5xhIVMVh6hub3Bnbl9VZ25lQkU
Referensi:
https://dennycharter.wordpress.com/2008/05/09/cara-kerja-mapserver/
https://mapproxy.org/