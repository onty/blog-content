Apa itu Online Charging System(OCS) Part 1
###########################################
:date: 2014-11-23 18:34
:author: Lintang JP
:category: Telco
:tags: Charging System, OCS, Prepaid System, Intelligent Network
:slug: apa-itu-ocs-part-1

Assalamu'alaikum,

Cihuy, gaya dikit, sekarang ngeblog pake vim :D. Setelah sukses migrasi 2 blog lama ke github, sekarang pertama kalinya nulis lagi pake vim :D
Udah lama pengen nulis tentang seri telekomunikasi, setelah melepaskan diri dari dunia J2EE application server sejak 6 (hampir 7 tahun yang lalu) karena insyaf :D
Ternyata di tempat yang sekarang, pengetahuan java itu masih dibutuhkan sedikit-sedikit kok, apalagi konsep pemrograman. Java tetep dipake, tapi karena sourcenya nggak dipublish sama team Design Unit, jadi ya, cara mudah nge-trace problem tentu dengan decompile .class nya :D, karena ternyata nggak di obfuscate juga :D. Knowledge programming dan dasar-dasarnya juga alhamdulillah masih terpakai, walaupun seringnya sekarang debug script, bukan bikin script, he he. Unix/Linux juga kepake banget, database knowledge juga (jadi siapa tuh yang bilang kuliah ngga ada gunanya ? :D ). Ya kalo anda memutuskan jalan hidup yang keras untuk jadi engineer ya resikonya begini lah. Lho Bill Gates apa bukan engineer juga ? Dia drop out kuliah lho ? Kalo anda mikir gitu ya silakan, saya ndak maksa. Nanti kalau ada sukses karena terinspirasi tulisan ini, kasih tau saya ya :D.

Yakk, balik ke topik (enak juga ngetik di vim ternyata ya), lancar jaya. Jadii, di tulisan saya yang lain di topik Telco, dulu saya pernah menulis bahwa Billing adalah jantungnya telekomunikasi. Ini masih benar, karena Billing tetap sumber pemrosesan pemasukan perusahaan Telekomunikasi. Tapi ada satu yang kurang disitu, anda tau ? Yak, betul. Kebanyakan billing tidak melakukan prosesnya secara realtime. Bukan berarti kuno, karena Billing punya fungsi dan keunggulannya sendiri. Nanti kita bahas ya bagaimana Online Charging System dan Billing System bisa co-exist satu sama lain.

Lalu bagaimana dengan Online Charging System ? ya tentu saja sesuai namanya, 'Online', berarti harus On terus, dan realtime. Online Charging System (kita singkat OCS aja ya) dalam hal ini secara simplenya bertugas melakukan fungsi Rating secara online dan realtime. Berikut kira-kira list lengkap fungsi dari OCS :

0\. Subscriber database


1\. Realtime rating
Masih ingat apa itu rating ? Yak, di artikel yang duluuu banget tentang Billing ( cari sendiri ya, belum tau caranya refer link di halaman yg sama pake markdown :p) yaitu proses untuk menentukan cost dari sebuah event. Nah, karena realtime, maka semua parameter yang dibutuhkan untuk menentukan cost tsb ya harus tersedia saat itu juga..nah, ini bedanya sama Billing, dan ini salah satu yang bikin mereka bisa co-exist :). 

Contohnya untuk menentukan cost dari sebuah voice call antar operator pada jam tertentu misalnya. Berikut parameter realtime yang harus ada dan akan dibutuhkan kira-kira seberti berikut :

```
- **Calling Number** ( sering disebut A#, A party, etc )
- **Called Number** ( sering disebut B#, B party, etc), buat nentuin tujuan nelponnya kemana. Kalo sesama operator biasanya gratis atau lebih murah daripada nelpon ke beda operator kan ? Trus kalo yang sering nelpon ke nomer premium, pasti tarifnya beda juga kan ? :)
- **Location Information**, kalo di spek 3GPP disebut locationNumber, berupa angka tertentu yang menunjukkan lokasi A# saat melakukan panggilan. Biasanya dipakai untuk menggabungkan beberapa cell-id menjadi satu. Kenapa harus digabungin ? ya bayangin aja, operator gede BTS nya sampe puluhan ribuan, masing-masing BTS biasanya punya 3 cell-id, mabok dah kalo yang dijadiin parameter buat Rating nya cell-id :D. Dari parameter ini juga ketauan, pas lagi nelpon ini lagi di Home Network ( dalam negeri biasanya ), atau lagi Roaming di luar negeri.
- **Calling Time**, waktu dimana event itu terjadi. Dari MSC biasanya dalam millisecond, tapi operator berhak rounding dong ke second terdekat ;)
- **Faktor lain**, misal: Sisa Bonus, daftar paket promo apa nggak 
```

2\. Realtime charging
Nah, setelah costnya berhasil ditentukan, tinggal ngurangin pulsa deh, secara realtime. Jadi begitu voice call selesai ditutup, langsung cek pulsa, keliatan deh sisa pulsa tinggal berapa, ga perlu nunggu sebulan pas billingnya keluar :) 

3\. Realtime balance management
Balance management ini termasuk didalamnya manajemen sisa pulsa :D. Tau kan, jaman sekarang pake smartphone, data nyala terus, sambil kirim sms, pulsa habis, trus pelanggan isi ulang dan ngecek sisa pulsanya. Nah, ada duit masuk, duit keluar, dan bisa jadi menuju ke 'dompet pulsa' yang sama. Ini maksudnya balance management.

Nah, selain fungsi dasar diatas, biasanya OCS juga bisa melakukan hal-hal sbb:
1\. Mengirimkan notifikasi ke pelanggan
Pernah gak tiba-tiba nerima notifikasi 'sisa pulsa anda tinggal Rp xxx,- kirim 2 sms lagi untuk mendapat free sms seharian'. Nah, fitur notifikasi seperti ini bisa dimiliki oleh OCS. Alasannya ya wajar, karena OCS melakukan rating dan charging secara realtime, maka OCS bisa memberikan notifikasi lebih akurat juga. Fitur ini juga banyak dipakai buat pelanggan yang sedang roaming ke luar negeri, untuk menerima notifikasi peringatan tagihan ketika mencapai usage tertentu. Beberapa negara yang saya tau sudah mulai memiliki regulasi agar setiap operator memiliki fungsi notifikasi roaming control seperti ini.

2\. Maintain lifecycle 
Lifecycle itu lebih populer dengan nama 'masa tenggang' kalo di sistem prabayar. Masa tenggang pertama, anda hanya bisa menerima panggilan. Masa tenggang berikutnya, nomer anda di blok tidak bisa melakukan dan menerima panggilan. Masa tenggang berikutnya, pulsa anda hangus :). Masa tenggang terakhir ? Nomer anda sudah dihapus dari jaringan telekomunikasi (baca:hangus). Nah, karena OCS menyimpan data subscription (kapan mulai start berlangganan, kapan masa tenggang, berapa sisa pulsa, dst), maka OCS juga lah yang biasanya secara realtime akan melakukan komunikasi dengan network element (dalam hal ini HLR, Home Location Register), untuk melakukan pemblokiran nomer.

3\. Maintain announcement list buat pelanggan
Pernah gak, sisa pulsa tinggal 500 perak, lalu dipake buat nelpon ? Biasanya kita dapet 'ceramah' panjang dulu dari operator, isinya kira-kira 'pulsa anda hampir habis, silakan melakukan isi ulang bla bla bla', trus baru telponnya nyambung. Lalu contoh lain, ketika lagi gencar promo dari operator, 1x tiap hari ketika akan melakukan panggilan telepon, anda dapet 'ceramah' lagi ? nah, OCS juga bisa mengirimkan kode announcement ke MSC, berubah-ubah sesuai dengan kondisi pelanggan. MSC akan menerima perintah pemutaran announcement, dan memutar announcement yang diperintahkan.Atau ketika nomer anda hampir expired, anda akan mendengar 'ceramah' untuk segera membeli voucher baru :)

4\. Revenue Reporting
Kalo ini sepertinya udah jelas ya, OCS juga merupakan sumber digalinya laporan keuangan laba perusahaan :). Hal ini biasanya tidak diproses secara realtime, karena OCS dirancang untuk transaksi online, bukan sebagai transaksi reporting. Biasanya setiap kali sebuah event selesai dirating, OCS akan menulis data transaksi berupa file CDR ( Call Detail Record ) yang kemudian bisa di proses dan di feed kedalam database untuk keperluan reporting.

5\. QoS control
Nah, ini fungsi terbaru OCS yang paling keren di era Broadband. Yak, OCS juga bisa memberikan data mengenai QoS yang seharusnya dimiliki oleh pelanggan. Misal, seorang pelanggan A berlangganan paket data yang paling murah, seribu perak seharian, internet unlimited. Lalu ada pelanggan B, berlangganan paket data premium 500 ribu perak sebulan. Nah, karena OCS memaintain data paket apa saja yang dimiliki pelanggan, maka OCS juga merupakan sumber informasi QoS apa yang seharusnya diberikan pada pelanggan. Untuk pelanggan premium, tentu sudah seharusnya mendapat QoS paling tinggi, wajar karena dia bayar mahal untuk paket datanya. Nah, informasi QoS ini akan diberikan oleh OCS melalui sebuah protokol yang baru di sahkan oleh 3GPP, namanya Sy. Lebih lanjut tentang protokol charging di bagian ke 2 ya. Intinya, informasi QoS profile akan di feed oleh OCS ke PCRF, yang akan menerima query dari PCEF tentang QoS profile apa yang seharusnya di apply untuk tiap pelanggan.
Lho, ngapain harus lewat PCRF, kenapa PCEF nggak langsung nanya ke OCS kalo gitu, daripada harus lewat calo dulu kan ? :D. Ya bisa juga sih, spek 3GPP memungkinkan PCEF mengirim protokol Gx ke either PCRF atau OCS langsung (kalau OCS nya support). Masalahnya arsitektur yang terlanjur berkembang untuk paket data adalah, terpisahnya database pelanggan dan database QoS paket data. Arsitektur yang umum ( karena network operator biasanya adalah evolusi dari 2G, 3G, ke 4G ) yaitu database QoS ditaruh di PCRF, dan database pelanggan(account dan balance) berada di OCS. Nah untuk menyatukan data pelanggan ini, dan juga agar ketika mendaftarkan paket data tidak perlu mendaftarkan ke 2 tempat (OCS dan PCRF), maka arsitektur yang baru dikembangkan adalah, data pelanggan akan dimaintain di OCS, dan PCRS akan menggunakan protokol Sy untuk mengambil data QoS dari OCS, dan mengapply nya via PCEF. 


Udah pusing? berasa mbulet ? Silakan tinggalkan komentar. Kalau ada yang dirasa kurang masuk akal juga monggo silakan tinggalkan komentar. Kalau saya yang salah, tulisannya akan saya ralat, tidak usah kuatir ;)


Lanjut ke part 2 yah, protokol standar apa aja yang disupport oleh -kebanyakan- Online Charging System :)

Cheers.
