**PEMBUATAN METHOD DAN CLASS RETRIVE DATA GEOSPASIAL**

**Latar belakang masalah :**

1. Apa itu Retrive Data ?
2. Apa itu Shapefile ?
3. Apa itu Geometri ?
4. Bagaimana Operasi Pengambilan Data ?
5. Buatlah Class Geospasial Editor ?
6. Bauatlah Method Select, Where Negara ?

**Isi :**
<p align="center">
    <img src="../../img/wd1.jpg">
    </p>
Retrive Data Geospasial adalah Meretrive Data Vektor.

Data Shapefile.shp

Operasi Retrive Data menggunakan Library python yang bernama py.shp

Shapefile adalah Syandard file

Vektor Geospasial dikeluarkan oleh ESRI

Geometri

Data koordinat yang membentuk bangun datar atau ruang diantaranya :

1. Point/titik [1]
2. Line/garis [3] shapefile,type
3. Polygon [5]



Method dari DBF

Fields : nama field

record(n)

Record (n) baris ke (n) records

# (n) adalah nomor sequence record

Method dari SHP

shapes() - Menampilkan semua

shape(n) - Menampilkan dengan parameter

1. bbox
2. parts
3. point s
4. shape type

bbox
boading box, merupakan batas view peta.

 Koordinat a,b,c,d itu di sebut bbox

- Parts itu apakah record ini bagian dari record lain/ precahan relasi
- points adalah koordinat pembentukan peta
- shapetype adalah jenis geometri dari points

1. Buat class geospasial pada editor.
<p align="center">
    <img src="../../img/1.jpg">
    </p>
2.Select Negara
<p align="center">
    <img src="../../img/2.jpg">
    </p>
polygon digunakan untuk batas tertutup/kembali ke titik awal
contoh : bentuk suatu benua atau wilayah
polyline tidak kembali ketitik awal
contoh : jalan, sungai, batas wilayah, dll.
 Penutup
 Kesimpulan : Kita dapat mengetahui bagaimana membuat class yang terdapat pada retrieve data
 Saran: sulitnya memahami penggunaan nya, karena kurangnya latihan dan memperbanyak praktek.
