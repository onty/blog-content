Title: Why Telco? *Narsis
Date: 2006-12-07
Tags:
Category: Telco

Kalo ditanya, kenapa bahagia di industry telco. Simply karena di sektor ini kayaknya teknologi berkembang terus, hampir tiap waktu (terlepas dari..apakah teknologinya sekarang akan kepake ato nggak, e.g: 3G ). Alasan lain, karena kayaknya di sektor inilah, orang-orang IT bener-bener *dianggap*. Industri lainnya mungkin adalah perbankan sama perminyakan. Sedangkan di industri lainnya, orang IT ada yang hanya jadi IT Support, they deserve more than that! Mereka asset berharga perusahaan ... tentunya kalo perusahaan tahu gimana cara membuat mereka usefull.
Satu argumen dengan apa yg kumaksud *bener-bener dianggap*, artinya setelah mereka bikin aplikasi, jadi, mereka nggak ditinggalin gitu aja dan cuman buat support aplikasi itu. Jarang ada inovasi teknologi baru, kerjanya ya bikin Sistem Informasi. Kalo gitu ceritanya, gimana orang IT bisa berkembang, ya nggak ? Beda ama orang IT yg di 3 industri tadi, setelah aplikasi baru, jadi, mereka mungkin support, tapi mereka selalu dapet update teknologi terbaru. Mereka belajar banyak hal baru.

> Bicara tentang industri telko, menurutku dibagi jadi 2 bagian besar, bagian *kasar*, dan bagian *lunak*

Bicara tentang industri telko, menurutku dibagi jadi 2 bagian besar, bagian *kasar*, dan bagian *lunak*. Bagian *kasar* (ada quote nya loh, gak kasar beneran) itu bagiannya temen2 elektro jurusan telkom, sama mungkin arus lemah. Disitu ada BTS, BSC, MSC, dan lain sebagainya. Kalo bagian *lunak* nih bagiannya orang informatika, sama mungkin orang elektro jurusan komputer. Disini ada yang namanya Billing, CRM, midleware, SMS Gateway, SMSC, USSD, Smart Card , HLR, dst.

Bicara tentang bagian lunak, Billing nih jantungnya perusahaan telko. Disini semua tagihan dicatat. Tiap kali suatu service/layanan selesai diberikan (misal : telepon, sms, gprs) akan dibuat suatu file bernama CDR, yang nantinya akan di rating oleh mesin billing, yang nantinya (kalo postpaid) akan ditagihkan tiap bulan. Rating ini dilakukan tiap hari, untuk tiap event, untuk semua pelanggan. Jadi nggak usah dibayangin betapa sibuknya mesin billing ini tiap hari.

Di front desk, ada customer care yang berhubungan langsung dengan pelanggan menggunakan aplikasi CRM. Aplikasi CRM ini biasanya dibangun diatas sebuah platfor terintegrasi. Kenapa begitu ? iya dong, customer care kan harus bisa njawab semua pertanyaan pelanggan yang berkaitan ama service yg di deliver. Contoh nyata nya, kita dateng ke gallery, trus nanya ... mbak, tagihan bulan lalu yg harus saya bayar berapa ya ? mbak, hp saya kok nggak bisa dihubungi sejak kemarin ya ? mbak saya mau aktivasi MMS gimana caranya ya ? mbak saya mau terminate nomer saya bisa nggak ? mbak, saya mau pindah dari prepaid ke postpaid, dst dsb. Dari gambaran diatas, bisa dilihat bahwa aplikasi CRM ini terhubung ke Billing, ke HLR (buat mengetahui kondisi service number anda di network), dan ke aplikasi2 proprietary lainnya. Ruwet ? yep, banget.

> Dari situ, diperlukan sebuah, sesuatu, sesosok (halah..) mesin yang berfungsi mengintegrasikan semua sistem-sistem back end tadi

Dari situ, diperlukan sebuah, sesuatu, sesosok (halah..) mesin yang berfungsi mengintegrasikan semua sistem-sistem back end tadi. Aplikasi ini banyak disebut dengan istilah midleware. Salah satu implementasinya dalam bentuk ESB [disini][1]. Bayangannya, mesin ini punya konektor spesifik buat masing-masing back end system tadi (Service Engine) yang di ekspos dalam macam-macam bentuk protokol (Binding Components) seperti http, webservice, JMS, dst. Jadi misalnya, aplikasi CRM ingin mendapatkan data dari Billing, maka dia tidak harus connect langsung ke Billing menggunakan API API yg disediakan spesifik oleh billing, tapi dia bisa connect ke midleware menggunakan http, webservice, atau apapun yg disediakan oleh midleware. Tampak lebih rumit step nya ? nggak juga. Bayangin kalo sebuah operator memiliki beberapa sistem billing yang mempunyai API berbeda-beda, tentu sang CRM harus membuat konektor yg berbeda-beda pula. Bayangkan juga kalo yang harus memakai system billing tidak hanya aplikasi CRM, tentu untuk masing-masing aplikasi itu harus dibuat konektor ke billing. Arsitekturnya jadi bintang ruwet. Midleware menyederhanakan hal ini. Kita hanya harus membuat satu konektor untuk masing-masing system, kemudian konektor tadi di ekspose sebagai service yg bisa diakses melalui Binding Components. Untuk referensi bisa dibuka situs [ini][2].

Lalu ada sms gateway. Contoh paling simple kegunaannya nih ketika registrasi kartu pra bayar. Kirim sms ke 4444, ketik daftar#bla bla bla. Contoh lain yaa kalo ada acara AFI atau Indonesian Idol gitu lah. Sms gateway ini sesuai namanya - gateway -, berfungsi sebagai penghubung dua hal atau lebih yang berbeda. Kalau kita kirim sms, akan diterima dan diteruskan oleh SMSC. Nah, kalau untuk kasus diatas, registrasi kartu pra bayar, logikanya kan ada proses insert ke database. Nah, proses insert ini bukan bagiannya SMSC karena dia cuma meneruskan sms saja. Oleh karena itu, dibuatlah gateway yang menghubungkan antara SMSC, sehingga ujungnya tuh sms bisa kecatet dan masuk ke database. Atau untuk kasus AFI/Indonesian Idol, dari SMSC akan meneruskan ke Content Provider, yang nyediain layanan ini.

Pengembangan lebih lanjut dari layanan yang disediakan SMSC ini adalah WAP PUSH dan MMS. Contoh layanan WAP PUSH ini mungkin adalah detikportal.com yang diakses via HP. Sedangkan untuk MMS mungkin penjelasannya begini, ketika kita dapet kiriman MMS, maka kita akan dapat sms yang berisi link yang bisa di klik untuk di download. Untuk referensi bisa buka [disini][3].

Sekian dulu bloggingnya ... waktunya ishoma :D

logger.info("written @grhaXL, 9th floor" );


[1]: http://jroller.com/page/JPrasojo/?anchor=esb_1
[2]: http://www.eaipatterns.com
[3]: http://www.mbuni.org
