Title: Ngabuburit dengan PHP
Date: 2007-8-9
Tags: 

Assalamu'alaikum ...

hari minggu, lagi nunggu buka di kantor, sambil nunggu burning suse ma xandros desktop, bosan mau ngapain, jadi ngisi blog deh. mau cerita tentang PHP, one of the most powerfull programming language in the web environments.di project yg sekarang, aku make php dan xml (ini sih mungkin biasa ya),mbikin monitoring tools(baca:kulit) buat aplikasi sms gateway nya kannel.benernya kannel dah nyediain sih, interface cgi mereka, namun biar bisa dijual, kayaknya interface yg mereka sediain gak cukup "menarik", makanya php datang sebagai pahlawan bertopeng :p. Tau kan, di kannel mereka nge bind port tertentu buat monitoring sms gateway mereka, kalo disini sih port 13000, tergantug settingan adminport di kannel.conf nya.Nah, tantangannya adalah bagaimana informasi status gateway yg update tiap detik tuh bisa diterima langsung di klien tanpa halaman web yg dibangun tuh "berkedip", you know, blinking, kalo kita ngerefresh halamannya kan jelek, masak tiap detik refresh. Nah, untuk yg satu ini, salut deh buat microsoft, yg, harus diakui, bener bener paling bagus ngimplementasiin XML di browser mereka. Dengan javascript timer, dan microsoft XMLHTTP, it's done, jadi deh. Jadi ceritanya tuh, kita tetep ngupdate info, narik ke client lewat browser, tapi nggak dengan cara ngerefresh satu halaman. Untuk monitoring seperti ini, kan informasinya harus realtime, berarti butuh koneksi terus menerus antara klien dengan server kannel. Kalo lewat web, setiap kita minta koneksi ke server, kan selanjutnya udah, putus, walaupun masih ada objek session, tapi gak ada gunanya, soalnya kita bener bener minta info yg terbaru dari server. Jadi, konsepnya, kita tetep minta info ke server tiap detik, via javascript timer dan XMLHTTP tadi, tapi lewat "jalan belakang, dimana user juga gak tau bahwa web browsernya sedang ngerequest halaman terus menerus ke server, yg mereka tau ada tulisan berisi status yg keupdate terus di layar mereka. Kalo di mozilla, entahlah, belum tau. YG jelas, implementasi XML Data Island di Mozilla gak sebagus dan semudah punya Microsoft (omongan jujur dari pecinta linux :p ).

Selain itu, aku juga make php buat generate report dengan format excel dan pdf, bikin chart juga dengan library jpgraph. Agar php support format pdf, harus download dulu library dari pdflib, setelah itu, untuk memulai, ada library/class php bagus milik fpdf di http://www.fpdf.org, cool, kita bisa masukin gambar juga di pdf kita.

Masalah lain ada pada waktu generate pdf.Kan di aplikasi web itu aku juga bikin graph chart dari library jpgraph gd, file yg terbentuk kan berasal dari php, jadi nggak murni file grafik, cuman di set content-type nya berupa grafik. Ehh, si fpdf nggak mau, errornya bilang, bahwa file grafik hasil generate dari php itu nggak ditemukan. Hmm, pusing juga, padahal path nya bener loh. Akhirnya aku ngoprek lagi tuh jpgraph, sampai pada settingan dimana jpgraph mendukung cache, jadi file hasil generate tadi bisa disimpan sebagai cache berbentuk FILE ASLI bertipe...macem macem sih, kebetulan punyaku berformat png, ya udah deh, tinggal set pdfnya supaya ngambil gambar dari file asli di direktori cache tadi, beres...

eh, dah dulu yak, dah buka nih....mau cari minum dulu di pantry, bye,.....

Originally posted : 31/10/04 5:49