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

2\. Maintain lifecycle 

3\. Maintain announcement list buat pelanggan

4\. Revenue Reporting



