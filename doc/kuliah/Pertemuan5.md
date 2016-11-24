Membuat dan Mengubah Data Geospasial

Latar Belakang Masalah
Pembahsan kali ini untuk melanjutkan dari pembahasan sebelumnya tentang manipulasi data geospasial. kali ini akan membahas tentang bagaimana cara membuat dan mengubah data geospasial menggunakan library pyshp

A. Cara Membuat Data Geospasial
Untuk membuat data geospasial, menggunakan library pyshp, dan untuk membuat data geospasial diperlukan file namafile.shp beserta namafile.dbf.

Adapun tahapannya sebagai berikut:
a. Import shapefile
b. Instanisasu writer method
    Sf = shapefile.Writer(param)
    Dimana param adalah pilih shapetype:
- shapeType = 1
- shapeType = 3
- shapeType = 5
c. Sama seperti read, kita lakukan method dbf dan shp.

 Shapefile (shp)
 Untuk menambahkan record tergantung dengan tipe ESRI-nya.
1. sf.point (x,y)
2. sf.line = (parts:[[x.y],[z.w],...])
3. sf.poly = (parts:[[x.y],z.w],...])

 Databasefile (dbf)
 Tahapannya adalah sebagai berikut:
a. Membuat atribut terlebih dahulu kemudian menambahkan record nya.
Contoh:
 sf.field('Nama Field','C','50')
 Dimana C adalah Character, dan 50 adalah length. Dalam arti nama atribut, nama field dengan panjang 50 karakter.
b. Tambahkan recird dibawah ini
 sf.record('Batam')
 sf. record('Batam','Sekupang')
c. Setelah selesai maka simpan, dengan perintah
 sf.save('namafile.shp')

B.Mengubah  Data Geospasial
Adapun dalam editing data geospasial hampir menyerupai langkah-langkah membuat data geospasial yang membedakannya adalah;
sf = shapefile.Writer(param)
diubah dengan
sf = shapefile.Editor(param)
dimana letak param adalah nama letak file.

Adapun operasi dalam editing pada shp dan dbf sama saja.
shp
dbf
sf.poly()
sf.line()
sf.point()
sf.record()
sf.delete(n), dimana n adalah baris ke-n dari tabel
Dan jika sudah selesai lalu simpan dengan perintah:
Sf.save('namafile')
PENUTUP
Kesimpulan
Membuat dan mengubah data geospasial tahapannya hampir menyerupai. Yang membedakannya adalah method yang digunakan, Method yang digunakan untuk membuat data geospasial adalah WRITE sedangkan untuk mengubah adalah EDITOR.

Saran
Adapun sarannya yaitu untuk memahami lebih lanjut dan lebih rinci tentang cara membuat dan mengubah data geospasial, bisa kita praktekan secara langsung menggunakan bahasa pemrograman python.