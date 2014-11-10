Title: Nexenta Alpha 5
Date: 2007-6-3
Tags: 

Hehe, alhamdulillah, seneng juga bisa nyobain nexenta alpha 5 walau hanya di vmware. Sempat kaget nggak nemu pkgadd, malah nemu apt-get. Dan pertama bingung juga waktu mau install package dasar -> GCC karena kalo install satu-satu dependancy nya kan nggak mungkin (bisa kriting). Akhirnya nemu repository yg harus ditambahin di /etc/apt/sources.list yaitu :

deb http://gnusolaris.org/apt-obsolete elatte-unstable main contrib non-free
deb-src http://gnusolaris.org/apt-obsolete elatte-unstable main contrib non-free

Terus, kepentok juga ketika menghadapi proxy kantor yg make ISA Server, dimana harus masukin username/password domain. Solusinya, make ini : http://ntlmaps.sourceforge.net/

Happy nexenta-ing ... :)

Sekarang mau coba me linux kan nih solaris, terus mau coba zoning di solaris, trus mau coba....WAAA IYAAAA, laptopnya mau dituker ama kantor beberapa hari lagi :( mosok install ulang rek :(( semoga vmware bisa dikopi doang .vmx nya, hopefully ....

originally posted 6/26/06