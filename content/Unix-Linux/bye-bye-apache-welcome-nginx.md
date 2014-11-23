Title: Bye bye apache, welcome Nginx
Date: 2008-12-22
Tags: aTutor Unix Linux stuff Web Server Internet Nginx
Category: Unix/Linux

Bagi saya, php tetap memiliki kenangan yang indah dalam mengisi hari-hari pemrograman saya terdahulu. Programming language yang fleksibel, dan nggak pake ribet. Justru kesulitan ditemui ketika deploy di server. Kebanyakan server yang tersedia sudah diinstall default dengan bundle apache, beserta modul-modul yang sudah di tentukan sebelumnya. Kalau pake keluarga Redhat, iya kalau kebetulan dapet rpm yang pas versinya, kalo nggak ? Cara paling enak memang tetap dengan compile dari source, karena kita bisa bongkar pasang modul yang kita inginkan, tambahkan semaunya, kurangi sesukanya. Jaman dulu(nggak dulu banget sih, 2004), saya hanya kenal Apache dan IIS buat jadi webserver untuk skrip php saya. Belakangan ini, muncul sebuah webserver yang tidak terlalu terkenal, tapi sepertinya ampuh. Kenapa ampuh ? Coba anda pergi ke netcraft.com, dan coba anda scan situs wordpress.com dan detik.com, apa webserver mereka ? Mereka pakai Nginx (baca:engine X). Ini dua situs besar loh, dan saya sangat yakin, tiap hari banyak diantara kita yang berinteraksi dengan kedua situs ini, ya tho ? Nggak mungkin dong mereka pake webserver yang kurang 'terkenal' kalo nggak karena mereka merasakan keampuhan dibaliknya, tul ndak ? Coba buka aja deh langsung di [situsnya][1].


Ok, karena saya bukan pembuat Nginx, sejarahnya tidak akan saya beberkan disini. Berikut sebagai pengingat saja buat saya (syukur kalau berguna buat anda juga) untuk ngebangun server PHP siap pakai dengan Nginx dan lighttpd.

Berikut Linux saya, ubuntu 7.10 :

```
lintang@cygnus:~$ uname -a
Linux cygnus 2.6.22-14-generic #1 SMP Sun Oct 14 23:05:12 GMT 2007 i686 GNU/Linux
```

Disini kebetulan waktu nginstall, saya pake apt-get saja untuk nginx nya, baru php dan lighttpdnya yang compile dari source. Selain nginx, kita juga harus install dependenciesnya, terutama pcre dan zlib, serta openssl kalau anda ingin.

```
root@cygnus:~# apt-get install libpcre3 libpcre3-dev zlib1g zlib1g-dev nginx
```

Tunggu sejenak, bikin kopi dulu juga boleh. Atau kalau anda ingin waktu anda efisien, mari kita donlot dulu PHP dan Lighttpd nya :D
Saya ambil PHP versi 5.2.6, dan Lighttpd versi 1.4.19. Dari mana ? please deh, silakan googling, mudah didapat kok kedua-duanya.
Ok, kita mulai dengan PHP dulu, silakan ekstrak, compile, dan install. Berikut opsi yang saya gunakan untuk PHP saya.

```
lintang@cygnus:~$ ./configure --prefix=/usr/local/php-5.2.6 --with-mysql --enable-fastcgi --with-sockets --with-zlib
```

Ini berarti, kita akan instal PHP kita nanti di direktori /usr/local/php-5.2.6, mengikut-sertakan library koneksi php untuk mysql, membuat PHP yang berfungsi sebagai interpreter CGI ( nantinya skrip PHP bisa dijalankan dari shell, mirip /bin/bash atau /usr/bin/perl), lalu PHP tersebut dapat memiliki/membuka socket tersendiri (nantinya PHP akan berjalan sebagai process yang terpisah dari webserver, tidak seperti model Apache dimana PHP berjalan sebagai modul di dalamnya), lalu yang terakhir, mengikut sertakan library php untuk support kompresi dengan tipe Gzip.
Tunggu sejenak, setelah sukses, silakan lakukan langkah dibawah seperti biasa :

```
lintang@cygnus:~$ make
lintang@cygnus:~$ sudo make install
```

Nah, coba cek di direktori /usr/local/php-5.2.6/bin, seharusnya ada file executable bernama php-cgi. File inilah yang akan berjalan sebagai interpreter PHP anda dari shell.
Menurut beberapa sumber dari internet, sebenarnya php-cgi ini saja cukup untuk dipanggil dari Nginx nantinya untuk menjalankan PHP, namun akan lebih baik apabila kita mengambil spawner dari project Lighttpd. Spawner ini akan mengeksekusi php-cgi kita. Berikut langkah-langkahnya, seperti biasa, silakan ekstrak Lig

```
lintang@cygnus:~$ ./configure --prefix=/opt/lighttpd-1.4.19 --enable-static --disable-shared
```

Kira-kira maksudnya, kita akan menconfigure Lighttpd sebagai library static yang dependenciesnya mutlak terhadap file-file .so tertentu. Opsi static ini membuat program yang kita compile akan jauh lebih cepat, karena versi dependencies di dalamnya seperti di hardcode. Berkebalikan dengan ketika kita compile dengan modus dinamis, hasilnya program akan lebih lambat, namun dependencies terhadap versi library tertentu bisa dihindari. Kalau kita ingin membuat server yang cepat, siapa peduli dengan dinamisasi, bukan begitu ? :p
Lalu seperti biasa, kita jalankan make, tapi kali ini tanpa make install.

```
lintang@cygnus:~$ make
```

Seharusnya nanti, di direktori src/ akan ada file bernama spawn-fcgi. Kopikan file tersebut ke directory /usr/bin sebagai berikut :
lintang@cygnus:~$ sudo cp spawn-fcgi /usr/bin/
Lalu anda buat skrip .sh sederhana sebagai berikut :

```
lintang@cygnus:/usr/local/php-5.2.6$ cat > /usr/bin/php-fastcgi #!/bin/sh

/usr/bin/spawn-fcgi -a 127.0.0.1 -p 8999 -f /usr/local/php-5.2.6/bin/php-cgi

```

Ini adalah skrip untuk menjalankan PHP sebagai proses CGI yang terpisah dari webserver anda nantinya. PHP akan membuka socket di port 8999, dan akan binding di interface lo(127.0.0.1) anda, sehingga hanya bisa diakses dari mesin anda sendiri.
Ok, langkah terakhir tinggal setup nginx.conf anda, punya saya ada di sini /etc/nginx/nginx.conf.
Berikut isi file konfigurasi Nginx saya :
```
user www-data;
worker_processes 4;

error_log /var/log/nginx/error.log;
pid /var/run/nginx.pid;

events {
worker_connections 1024;
}

http {
include /etc/nginx/mime.types;
default_type application/octet-stream;

access_log /var/log/nginx/access.log;

sendfile on;
#tcp_nopush on;

#keepalive_timeout 0;
keepalive_timeout 65;
tcp_nodelay on;
gzip on;

include /etc/nginx/sites-enabled/*;

}
```
Perhatikan baris yang di bold, bahwa Nginx saya berjalan atas nama user www-data, sehingga user ini mutlak harus ada sebelumnya, sepertinya kalau di Ubuntu, user ini dibuatkan otomatis ketika kita install Nginx yah, saya lupa sih :D.
Baris selanjutnya, worker_processes, saya isi 4. User yang mengakses webserver saya disini kurang dari 100 orang, dan selama ini, 4 worker sudah cukup sih.
Lalu selanjutnya, gzip on, ini modul gzip compress yang kita aktifkan setelah sebelumnya kita install zlib. Dan yang terakhir, kita akan meng-include kan semua file konfigurasi di direktori /etc/nginx/sites-enabled. Berikut contoh file konfigurasi saya di direktori tersebut :

```
Filename : atutor.conf
server {
listen 80;
server_name atutor;

access_log /var/log/nginx/atutor.access.log;

location / {
root /var/www/nginx-default;
index index.html index.htm index.php;
}

#error_page 404 /404.html;

# redirect server error pages to the static page /50x.html
#
error_page 500 502 503 504 /50x.html;
location = /50x.html {
root /var/www/nginx-default/ATutor;
}

# proxy the PHP scripts to Apache listening on 127.0.0.1:80
#
#location ~ .php$ {
#proxy_pass http://127.0.0.1;
#}

# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
#
location ~ .php$ {
fastcgi_pass 127.0.0.1:8999;
fastcgi_index index.php;
fastcgi_param SCRIPT_FILENAME /var/www/nginx-default$fastcgi_script_name;
include /etc/nginx/fastcgi_params;
}
}
```

Konfigurasi ini mengatakan bahwa, saya memiliki sebuah aplikasi (kebetulan aTutor), yang saya letakkan di /var/www/nginx-default, dan untuk semua URL yang berakhiran .php, maka saya akan lemparkan requestnya ke CGI interpreter PHP yang berjalan di port 8999 seperti konfigurasi PHP diatas.

And that's it, kita bisa mengetes konfigurasi nginx kita dengan perintah :

```
lintang@cygnus:~$ sudo nginx -t
```

Lalu untuk menjalankan nginx bisa dengan perintah sbb :

```
lintang@cygnus:~$ sudo nginx
```

Kalau kita ada perubahan konfigurasi nginx, setelah selesai mengedit file konfigurasi, untuk merestart nginx bisa dengan perintah sbb :

```
lintang@cygnus:~$ sudo killall -HUP nginx
```

Udah deh, silakan arahkan browser anda di port 80, aplikasi anda siap melayani user :)

[1]: http://nginx.net/
