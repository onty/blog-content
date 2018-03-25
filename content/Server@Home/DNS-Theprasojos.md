Title: DNS Setup for Theprasojos in Ubuntu@Pine64
Date: 2018-03-25
Tags: Unix Linux Bind Server Internet Named
Category: Server@Home

Long time I have not write on this blog, mostly because I can't remember how to configure the pelican in my mac (yeah, this blog uses pelican generator for html content, bye bye Wordpress, I guess you are no longer impress everyone by now). And luckily this blog's content is stored in a repos, making me easier to pull the content back. After some googling with keyword = 'pelican', I manage to get the set up back up and running.

Now, the problem is my ego :p, with hi-speed broadband, unlimited, and IPv6 allocation, sometime I felt so ashamed if I don't have my own server kingdom. Paying AWS just for playing around is just too much. At home I have my Pine64, several Raspberry Pi, all of them lying around without any use, so that's why I decided to host my own DNS, mail server, and of course, this blog. Problem with the blog is that, since I put it under IPv6 range, then the web client should also have IPv6. Well ok, I don't have lots of requirements for the webserver since I use pure HTML. So I put the mirror on other place as well, no big deal, as long as they can server HTML, fine for me. Hence you can read this blog from http://onty.maclab.org too. This post will not cover the concept on how DNS works, but this is rather just me, sharing how my server is configured, that's all.

Now, since my Pine64 has 2GB RAM, 64bit ARM CPU, 4 Core, and plenty of micro SD card space, I decided to use it as my Primary NS, Mail Server, and Web Server :D. My other old Raspberry Pi 1B is the Secondary NS. This old Raspberry 1B also hosts other functions, which is my radio streaming client, and it also runs Docker (yeah, Docker, you got it right) running tvheadend-server to receive digital TV (DVB-T2) broadcast here in Dublin. Pretty much stuff crammed into and old board, I don't care, and so far it serves its purpose very well :p. I can share this later, stay tuned.

So, yeah, I am using ubuntu in my Pine64. Here's the uname -a result just to give a slight hint on what I use:

```
root@pegasus:~# uname -a
Linux pegasus 3.10.105-0-pine64-longsleep #3 SMP PREEMPT Sat Mar 11 16:05:53 CET 2017 aarch64 aarch64 aarch64 GNU/Linux
```

And the CPU info :

```
root@pegasus:~# cat /proc/cpuinfo
Processor       : AArch64 Processor rev 4 (aarch64)
processor       : 0
processor       : 1
processor       : 2
processor       : 3
Features        : fp asimd aes pmull sha1 sha2 crc32
CPU implementer : 0x41
CPU architecture: AArch64
CPU variant     : 0x0
CPU part        : 0xd03
CPU revision    : 4
Hardware        : sun50iw1p1
```

And the Memory info :

```
root@pegasus:~# cat /proc/meminfo
MemTotal:        2036424 kB
MemFree:          985348 kB
Buffers:          116548 kB
Cached:           628944 kB
```

For the nameserver software, I used the famous Bind9. No particular reason why I used Bind9 instead of others like PowerDNS or djbdns. Kenny G once said it's just for *sentimental* reason :)

So, I started by installing bind9 by using the most obvious command in Ubuntu.

```
root@pegasus:~# apt-get install bind9 bind9-utils
```

Then the configuration festival begins. The main configuration file is stored at */etc/named.conf* with the pointers to other configuration file. The idea here is to split the configuration file based on it's purpose so that if I wanted to add more zones , I will just have to touch particular part of the configuration without touching anything else. Better safe than sorry, right? So this below is the only content of my */etc/named.conf* file.

```
include "/etc/bind/named.conf.options";
include "/etc/bind/named.conf.local";
include "/etc/bind/named.conf.default-zones";
```

The first file referred to from the main *named.conf* is *named.conf.options*. This file contains the options to be configured for the running Bind9 daemon. It tells the Bind9 daemon on which interface it should listen to, where to store the bind9 cache, and where to forward any DNS query that belongs to outside our zone (here I used google's 8.8.8.8 and 8.8.4.4). It also defines the other name server in our network we would like to use as the secondary name server (on this case it's 192.168.9.50).

```
options {
        directory "/var/cache/bind";
        forwarders {
                8.8.8.8;
                8.8.4.4;
        };
        dnssec-validation auto;
        auth-nxdomain no;    # conform to RFC1035
        listen-on-v6 { any; };
        allow-query { any; };
        allow-transfer { 192.168.9.50; localhost; };
        also-notify { 192.168.9.50; };
        recursion no;
        notify yes;
};
```

The *allow-transfer* option controls which server that we allowed to do the full zone transfer to. And the *also-notify* option controls which server (which is the secondary name server) that the primary server should *Notify* when there are some changes in this primary name server. The secondary nameserver then will check the serial number of the record from the primary name server and then request for the incremental changes of the zone record to be added/removed on it's record, making the two name server always sync each other.

The next file is */etc/named.conf.local*. This is where the zone is configured. So, I hijacked one of the domains in afraid.org called blogs.or.id and add 1 level domain above it (theprasojos), making it theprasojos.com.

```
zone "theprasojos.com" IN {
        type master;
        file "/var/lib/bind/db.theprasojos.com";
};

zone "0.8.2.1.1.2.a.6.4.8.0.8.4.9.a.2.ip6.arpa" IN {
        type master;
        file "/var/lib/bind/db.0.8.2.1.1.2.a.6.4.8.0.8.4.9.a.2.ip6.arpa";
};
```

In the future, if more zones are to be added, then this is the only configuration file that needs to be touched.

The last file referred by named.conf is named.conf.default-zones. This file contains the zones that was by default configured by Bind9, so normally we don't need to touch anything on this file. These configurations listed in this file comes by default with the installation of Bind9 itself.

```
zone "." {
        type hint;
        file "/etc/bind/db.root";
};

// be authoritative for the localhost forward and reverse zones, and for
// broadcast zones as per RFC 1912

zone "localhost" {
        type master;
        file "/etc/bind/db.local";
};

zone "127.in-addr.arpa" {
        type master;
        file "/etc/bind/db.127";
};

zone "0.in-addr.arpa" {
        type master;
        file "/etc/bind/db.0";
};

zone "255.in-addr.arpa" {
        type master;
        file "/etc/bind/db.255";
};
```

Now, back to our zone, theprasojos.com. As pointed by the second file *named.conf.local*, this is the configuration file list for our zone. Here's the content of */var/lib/bind/db.theprasojos.com*. I put a random content there just to protect my network :)

```
root@pegasus:/etc/bind# cat /var/lib/bind/db.theprasojos.com
$TTL 1H
@   IN SOA  @ lintang.jp.icloud.com. (
                21   ; serial
                1H  ; refresh
                1H  ; retry
                3D  ; expire
                2H )    ; minimum
@            IN   NS     ns1.theprasojos.com.
@            IN   NS     ns2.theprasojos.com.
6            IN   AAAA   2a94:8084:6a21:1280:36c3:d2ff:fee4:cdf2
ns1          IN   AAAA   2a94:8084:6a21:1280:36c3:d2ff:fee4:cdf2
ns2          IN   AAAA   2a94:8084:6a21:1280:4ba:dd0:f892:fa91
nightwing    IN   AAAA   2a94:8084:6a21:1280:ba27:ebff:fe40:c2e
@            IN   MX     10 mail
mail         IN   AAAA   2a94:8084:6a21:1280:36c3:d2ff:fee4:cdf2
mail._domainkey IN      TXT     ( "v=DKIM1; k=rsa; "
          "p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDPdw2AmI8Ybbj5jNpbuqEcMW0VJoh+VU1fIO6b0+Yp5HPuat/DP4YakTdnSn0alzW0OpaFYdgj4ztTg/2NGzIqjHmDrrHUaw+Z6PsZaTT8UvG+R1icT5A8xH57xgU9yCaZdZQ4ZTs2IcFjajHvdzHNqYRFdlHf+c9aZpUC7B0+yQIDAQAB" )
@            IN   TXT    "v=spf1 mx -all"
@            IN   TXT    "PTR test"

```

Now, it happens that my ISP only grants a bunch of world-routable IPv6 to me, so this explains why I only have IPv6 content in it. There you can see I have several record with type = AAAA which points to IPv6 address. I also put several TXT record for my mail server which will be covered later on.

And finally below is the reverse zone record that I have. Again, since I only have IPv6 allocation, the content looks weird, but hey, it worked perfectly :)

```
root@pegasus:/etc/bind# cat /var/lib/bind/db.0.8.2.1.1.2.a.6.4.8.0.8.4.9.a.2.ip6.arpa
$TTL 1H
@   IN SOA  @ lintang.jp.icloud.com. (
                21   ; serial
                1H  ; refresh
                1H  ; retry
                3D  ; expire
                2H )    ; minimum
@       IN   NS     ns1.theprasojos.com.
@       IN   NS     ns2.theprasojos.com.

2.f.d.c.4.e.e.f.f.f.2.d.3.c.6.3    IN    PTR    ns1.theprasojos.com.
2.f.d.c.4.e.e.f.f.f.2.d.3.c.6.3    IN    PTR    mail.theprasojos.com.
1.9.a.f.2.9.8.f.0.d.d.0.a.b.4.0    IN    PTR    ns2.theprasojos.com.
e.2.c.0.0.4.e.f.f.f.b.e.7.2.a.b    IN    PTR    nightwing.theprasojos.com.

```

Btw, you might ask how did I construct those PTR record and the PTR zone file name ? I used the following tools provided [here](http://rdns6.com/zone) . It gives a good hint on how to construct the PTR record for IPv6 address.

Now it's time to test it. The DNS propagation will take some time. I used the tool [here](https://dnsmap.io) instead of those provided by Google. This is just to make sure that my zone is handled well only by Google's NS, but also other name server as well.

We can also test it from console. See below result :
```
$ dig -t ns +noall +answer theprasojos.com 8.8.8.8
theprasojos.com. 3424	IN	NS	ns2.theprasojos.com.
theprasojos.com. 3424	IN	NS	ns1.theprasojos.com.
```

And for the aaaa record :
```
$ dig -t aaaa +noall +answer www.theprasojos.com 8.8.4.4
www.theprasojos.com. 3518	IN	AAAA	2a94:8084:6a21:1280:36c3:d2ff:fee4:cdf2
```

And so on, so forth :)

Finally, last step is to make Bind9 running everytime the server starts. Since I use systemd, then the following file is required (/lib/systemd/system/bind9.service):
```
[Unit]
Description=BIND Domain Name Server
Documentation=man:named(8)
After=network.target

[Service]
EnvironmentFile=/etc/default/bind9
ExecStart=/usr/sbin/named -f $OPTIONS
ExecReload=/usr/sbin/rndc reload
ExecStop=/usr/sbin/rndc stop

[Install]
WantedBy=multi-user.target
```

And then the symbolic link :
```
/etc/systemd/system/multi-user.target.wants/bind9.service -> /lib/systemd/system/bind9.service
```
That's it. Thanks for reading.
