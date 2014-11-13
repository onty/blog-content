Title: Telco Billing #1, Interconnect that matters...
Date: 2009-1-10
Tags: Interconnect Telekomunikasi Telco Billing Interkoneksi
Category: Telco

Seperti disebutkan dalam judul diatas, bidang interkoneksi adalah bidang yang sangat berpengaruh dalam kelangsungan operasional sebuah operator, terutama buat operator non incumbent. Bagaimana tidak, bagi operator baru, tidak ada interkoneksi berarti tidak terhubung ke jaringan lain, pelanggan tidak akan bisa bertelpon/ber-sms ke operator lain ( terutama jika operator itu incumbent ), dan ini vital sekali. Peraturan Menkominfo tentang interkoneksi ini bisa di unduh [disini][1] .
Dalam bidang interkoneksi dikenal istilah-istilah berikut :
**1\. POC (Point of Charge)**
Kalau jaman PSTN(telpon rumah kabel) hanya ada cuma Telkom saja seperti dulu, POC ini kita kenal dengan istilah kode area. Katakanlah Mojokerto, maka kode area nya 0321, Surabaya, 031, dst. Seiring dengan waktu, muncullah telepon seluler, yang untuk menentukan POC nya sebenarnya lebih sulit, karena sifatnya yang mobile dan dapat berpindah-pindah, akibatnya POC untuk telepon seluler ini tidak menyerap 100% dari POC milik PSTN dan FWA(telepon cdma yang non seluler, seperti flexi, esia, hepi). POC ini adalah basis yang digunakan untuk menentukan dimana lokasi penelpon dan penerima telpon.
**2\. POI (Point of Interconnection)**
Adalah titik dimana alur traffic mengarah masuk atau keluar, dari network lokal milik operator yang bersangkutan, menuju ke network milik operator lain. Kita akan lebih mudah memahami ini dengan contoh kasus, yang akan diulas lebih lanjut di bawah. Yang jelas, semakin banyak kita memiliki POI dengan operator lain (dan yang ter-utilisasi dengan optimal tentunya ) maka cost interkoneksi ini akan jauh lebih bisa ditekan.
**3\. Originasi**
Adalah titik dimana alur traffic berasal.
**4\. Transit**
Adalah titik dimana alur traffic disalurkan melalui network operator lain, untuk kemudian bisa sampai ke tujuan. Bayangkan ini seperti ketika kita memaketkan barang lewat tiki. Tiki adalah titik transit pertama kita, untuk kemudian bisa sampai ke tujuan.
**5\. Terminasi**
Adalah titik dimana alur traffic berakhir di tujuan.

Ke-lima komponen ini berpengaruh penting dalam penentuan tarif biaya interkoneksi, yang pada ujungnya juga akan mempengaruhi tarif retail akhir yang akan ditawarkan ke pelanggan. Itulah kenapa ketika pemerintah memutuskan untuk menurunkan tarif interkoneksi antar operator, tarif retail juga diharapkan akan ikut turun.

Kita akan bahas ini dengan mengambil contoh langsung kasusnya, sebuah perusahaan telekomunikasi selular X.
Ketika pertama kali didirikan, operator X sudah harus menetapkan basis daerah awal dimana saja mereka akan beroperasi. Dari sinilah kemudian operator tersebut menyusun POC mana saja yang akan mereka miliki. Dan dari sini pulalah mereka akan membuat pemetaan prefix nomor mereka. Sebagai contoh, untuk daerah Jakarta, operator X akan membuat prefix 08XX170YYYY. 4 digit pertama (08XX) dikenal sebagai NDC, National Destination Code. Ini prefix yang menandakan blok nomor seluler tertentu milik operator tertentu.

Setelah memiliki POC, maka operator X harus juga membuka layanan interkoneksi dengan operator lain. Karena di Indonesia terdapat 12 operator, maka interkoneksi ini harus dibuat ke seluruh operator-operator tersebut. Pembuatan infrastruktur interkoneksi menuju operator-operator lain ini juga bukan dengan biaya yang kecil, apalagi jika alur traffic menuju operator-operator tersebut masih sangat kecil, karena tentu operator X juga membutuhkan biaya untuk balik modal kan ;).
Dari sini, muncullah operator Y yang bertindak sebagai operator transit. Artinya, operator X tidak perlu membangun jaringan interkoneksi ke seluruh operator yang ada, yang diperlukan hanya 1 buah infrastruktur interkoneksi, menuju operator Y sebagai operator transit, yang nantinya akan menyalurkan alur traffic menuju operator tujuan yang sebenarnya. Dari sini kita sudah mendapatkan gambaran, bagaimana kira-kira maksud dari originasi, terminasi, dan transit.

Lalu, kapan sebuah operator perlu membangun jaringan interkoneksinya sendiri ? Dari data statistik operator X tiap bulan, tentu operator X bisa melihat kemana tujuan paling banyak alur traffic dari pelanggannya. Dan begitu juga darimana pelanggannya paling banyak menerima panggilan. Jika cost transit ini diperkirakan sudah akan lebih mahal daripada membangun infrastruktur interkoneksi langsung dengan operator tujuan, maka sudah saatnya infrastruktur interkoneksi langsung ini dibangun.

Oh ya, dari tadi ini kita masih membicarakan panggilan suara (voice) yah, kalau untuk SMS, infrastruktur interkoneksi harus dibuat satu-persatu menuju operator tujuan, karena SMS ke operator lain tidak bisa disampaikan melalui jaringan transit.

Lalu bagaimana dengan penentuan tarif interkoneksi ? Tunggu di bagian #2 yah...

[1]: http://www.blogger.com/mod=
