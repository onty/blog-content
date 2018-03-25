Title: The power of lsof command
Date: 2018-03-21
Tags: aTutor Unix Linux Forensic Server Internet lsof
Category: 4n6

After few years using Linux and dealt with *lsof*, so far I only used it to check the file and dependancy library. It's very helpful to during the troubleshooting when a running binary crashed unexpectedly after some library upgrade in the server. At least that was according to my yearly experience dealing with Linux/Unix in Telco environment. Below is the example of the lsof output command against a named process in my Pine64. It shows the list of files and library opened by named process.

```
COMMAND   PID USER   FD      TYPE             DEVICE SIZE/OFF   NODE NAME
named   23423 bind  cwd       DIR              179,2     4096  24142 /var/cache/bind
named   23423 bind  rtd       DIR              179,2     4096      2 /
named   23423 bind  txt       REG              179,2   571200  15849 /usr/sbin/named
named   23423 bind  mem       REG              179,2  4391541  25637 /usr/share/GeoIP/GeoIPv6.dat
named   23423 bind  mem       REG              179,2  1160739  25639 /usr/share/GeoIP/GeoIP.dat
named   23423 bind  mem       REG              179,2    84824  26359 /usr/lib/aarch64-linux-gnu/openssl-1.0.0/engines/libgost.so
named   23423 bind  mem       REG              179,2    39272  52247 /lib/aarch64-linux-gnu/libnss_files-2.23.so
named   23423 bind  mem       REG              179,2    39312  52255 /lib/aarch64-linux-gnu/libnss_nis-2.23.so
named   23423 bind  mem       REG              179,2    76632  52263 /lib/aarch64-linux-gnu/libnsl-2.23.so
named   23423 bind  mem       REG              179,2    31408  52259 /lib/aarch64-linux-gnu/libnss_compat-2.23.so
named   23423 bind  mem       REG              179,2    70664    587 /lib/aarch64-linux-gnu/libgcc_s.so.1
named   23423 bind  mem       REG              179,2  1554312  35082 /usr/lib/aarch64-linux-gnu/libstdc++.so.6.0.21
named   23423 bind  mem       REG              179,2 25913104  36301 /usr/lib/aarch64-linux-gnu/libicudata.so.55.1
named   23423 bind  mem       REG              179,2    76456  52252 /lib/aarch64-linux-gnu/libresolv-2.23.so
named   23423 bind  mem       REG              179,2    14176  10038 /lib/aarch64-linux-gnu/libkeyutils.so.1.5
named   23423 bind  mem       REG              179,2    39440   4764 /usr/lib/aarch64-linux-gnu/libkrb5support.so.0.1
named   23423 bind  mem       REG              179,2    14496    595 /lib/aarch64-linux-gnu/libcom_err.so.2.1
named   23423 bind  mem       REG              179,2   170320   4773 /usr/lib/aarch64-linux-gnu/libk5crypto.so.3.1
named   23423 bind  mem       REG              179,2   643136  52250 /lib/aarch64-linux-gnu/libm-2.23.so
named   23423 bind  mem       REG              179,2   116816    483 /lib/aarch64-linux-gnu/liblzma.so.5.0.0
named   23423 bind  mem       REG              179,2    92400   1064 /lib/aarch64-linux-gnu/libz.so.1.2.8
named   23423 bind  mem       REG              179,2  1611832  36295 /usr/lib/aarch64-linux-gnu/libicuuc.so.55.1
named   23423 bind  mem       REG              179,2   757296   4753 /usr/lib/aarch64-linux-gnu/libkrb5.so.3.3
named   23423 bind  mem       REG              179,2   252040   4744 /usr/lib/aarch64-linux-gnu/libgssapi_krb5.so.2.2
named   23423 bind  mem       REG              179,2  1265992  52262 /lib/aarch64-linux-gnu/libc-2.23.so
named   23423 bind  mem       REG              179,2  1575720  26244 /usr/lib/aarch64-linux-gnu/libxml2.so.2.9.3
named   23423 bind  mem       REG              179,2   219544  22863 /usr/lib/aarch64-linux-gnu/libGeoIP.so.1.6.9
named   23423 bind  mem       REG              179,2   139560  52257 /lib/aarch64-linux-gnu/libpthread-2.23.so
named   23423 bind  mem       REG              179,2    22944    613 /lib/aarch64-linux-gnu/libcap.so.2.24
named   23423 bind  mem       REG              179,2    10400  52264 /lib/aarch64-linux-gnu/libdl-2.23.so
named   23423 bind  mem       REG              179,2   405376  15866 /usr/lib/aarch64-linux-gnu/libisc.so.160.0.0
named   23423 bind  mem       REG              179,2    34880  15871 /usr/lib/aarch64-linux-gnu/libisccc.so.140.0.4
named   23423 bind  mem       REG              179,2   147048  15878 /usr/lib/aarch64-linux-gnu/libisccfg.so.140.3.0
named   23423 bind  mem       REG              179,2    51040  10408 /usr/lib/aarch64-linux-gnu/libbind9.so.140.0.10
named   23423 bind  mem       REG              179,2  1639096  26368 /lib/aarch64-linux-gnu/libcrypto.so.1.0.0
named   23423 bind  mem       REG              179,2  1757560   6890 /usr/lib/aarch64-linux-gnu/libdns.so.162.1.3
named   23423 bind  mem       REG              179,2    67536  15906 /usr/lib/aarch64-linux-gnu/liblwres.so.141.0.3
named   23423 bind  mem       REG              179,2   125776  52261 /lib/aarch64-linux-gnu/ld-2.23.so
```

Now, lsof binary exist not only in Linux, but it also exist in OSx and FreeBSD. Well, if you don't have it, then you should probably install it first. OSx user can install this using brew, and FreeBSD user can install this with pkg. Here's the sample of the output from my Mac.

```
$ sudo lsof -p 133
Password:
COMMAND   PID USER   FD   TYPE DEVICE   SIZE/OFF       NODE NAME
aslmanage 133 root  cwd    DIR    1,5        448 4335236222 /private/var/log/DiagnosticMessages
aslmanage 133 root  txt    REG    1,5      65216 4335245721 /usr/sbin/aslmanager
aslmanage 133 root  txt    REG    1,5     837248 4338232972 /usr/lib/dyld
aslmanage 133 root  txt    REG    1,5 1156890624 4338816345 /private/var/db/dyld/dyld_shared_cache_x86_64h
aslmanage 133 root    0r   CHR    3,2        0t0        313 /dev/null
aslmanage 133 root    1u   CHR    3,2        0t0        313 /dev/null
aslmanage 133 root    2u   CHR    3,2        0t0        313 /dev/null
```

Now, the other side of *lsof* that I just _came to know_ is it's -i option. It shows the list of opened socket by each process **and** most importantly it's destination. See below output from my Mac:
```
$ lsof -i
COMMAND     PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
loginwind   119 onty    8u  IPv4 0xe46a6ed4502cbdf7      0t0  UDP *:*
UserEvent   320 onty    4u  IPv4 0xe46a6ed4502cc0a7      0t0  UDP *:*
SystemUIS   327 onty   10u  IPv4 0xe46a6ed4502cc357      0t0  UDP *:*
SystemUIS   327 onty   11u  IPv4 0xe46a6ed4502cbb47      0t0  UDP *:*
SystemUIS   327 onty   12u  IPv4 0xe46a6ed4502cb897      0t0  UDP *:50074
SystemUIS   327 onty   13u  IPv4 0xe46a6ed4502cb5e7      0t0  UDP *:*
SystemUIS   327 onty   20u  IPv4 0xe46a6ed4502cde37      0t0  UDP *:*
cloudd      343 onty  150u  IPv4 0xe46a6ed45872612f      0t0  TCP 10.9.0.162:54525->17.248.147.114:https (ESTABLISHED)
sharingd    354 onty    4u  IPv4 0xe46a6ed450cf4e17      0t0  UDP *:*
sharingd    354 onty    5u  IPv4 0xe46a6ed450cf48b7      0t0  UDP *:*
sharingd    354 onty    9u  IPv4 0xe46a6ed44c2aa317      0t0  UDP *:*
sharingd    354 onty   10u  IPv4 0xe46a6ed44c2aab27      0t0  UDP *:*
sharingd    354 onty   11u  IPv4 0xe46a6ed44c2ac8b7      0t0  UDP *:*
WiFiProxy   377 onty    5u  IPv4 0xe46a6ed44ffd9e17      0t0  UDP *:*
identitys   378 onty   19u  IPv4 0xe46a6ed44ffdae37      0t0  UDP *:*
rapportd    402 onty    3u  IPv4 0xe46a6ed45828d12f      0t0  TCP *:53729 (LISTEN)
rapportd    402 onty    4u  IPv6 0xe46a6ed4590dc347      0t0  TCP *:53729 (LISTEN)
rapportd    402 onty    7u  IPv4 0xe46a6ed44d23b6af      0t0  TCP 10.1.10.139:53729->10.1.10.136:49804 (ESTABLISHED)
rapportd    402 onty    8u  IPv4 0xe46a6ed4586f8877      0t0  UDP *:xserveraid
assistant   409 onty    4u  IPv4 0xe46a6ed4502cc8b7      0t0  UDP *:*
WiFiAgent   412 onty    5u  IPv4 0xe46a6ed44ffd7877      0t0  UDP *:*
SpotifyWe   433 onty    5u  IPv4 0xe46a6ed4523a912f      0t0  TCP localhost:4380 (LISTEN)
Tunnelbli   452 onty   18u  IPv4 0xe46a6ed451b41a8f      0t0  TCP localhost:52236->localhost:menandmice-dns (ESTABLISHED)
com.apple  2553 onty    6u  IPv4 0xe46a6ed4517cb12f      0t0  TCP 10.9.0.162:54344->lb-192-30-253-124-iad.github.com:https (ESTABLISHED)
com.apple  2553 onty    7u  IPv4 0xe46a6ed4587286af      0t0  TCP 10.9.0.162:52598->39.4a.37a9.ip4.static.sl-reverse.com:https (ESTABLISHED)
com.apple  2553 onty    9u  IPv4 0xe46a6ed45b9b7a8f      0t0  TCP 10.9.0.162:54249->waw02s16-in-f14.1e100.net:https (ESTABLISHED)
com.apple  2553 onty   10u  IPv4 0xe46a6ed451b436af      0t0  TCP 10.9.0.162:54450->waw02s17-in-f14.1e100.net:https (ESTABLISHED)
com.apple  2553 onty   11u  IPv4 0xe46a6ed4587286af      0t0  TCP 10.9.0.162:52598->39.4a.37a9.ip4.static.sl-reverse.com:https (ESTABLISHED)
com.apple  2553 onty   12u  IPv4 0xe46a6ed451b4112f      0t0  TCP 10.9.0.162:54479->waw02s08-in-f2.1e100.net:https (ESTABLISHED)
com.apple  2553 onty   13u  IPv4 0xe46a6ed45b7486af      0t0  TCP 10.9.0.162:54456->waw02s13-in-f2.1e100.net:https (ESTABLISHED)
com.apple  2553 onty   15u  IPv4 0xe46a6ed45828e3ef      0t0  TCP 10.9.0.162:54482->waw02s08-in-f4.1e100.net:https (ESTABLISHED)
com.apple  2553 onty   16u  IPv4 0xe46a6ed45b6d16af      0t0  TCP 10.9.0.162:54483->waw02s08-in-f195.1e100.net:https (ESTABLISHED)
com.apple  2553 onty   17u  IPv4 0xe46a6ed45c418d4f      0t0  TCP 10.9.0.162:54455->waw02s08-in-f193.1e100.net:https (ESTABLISHED)

```

I was just surprised since I always think that this is only possible in Linux using the netstat -natp command. See the output below from my Linux box:
```
COMMAND     PID      USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
ssh         498 netkernel    3u  IPv4 6825296      0t0  TCP 192.168.0.136:42692->99.subnet125-161-136.speedy.telkom.net.id:22222 (SYN_SENT)
nginx       537  www-data    6u  IPv6   20570      0t0  TCP *:http (LISTEN)
nginx       537  www-data    7u  IPv4   20571      0t0  TCP *:http (LISTEN)
nginx       537  www-data    8u  IPv4   20572      0t0  TCP *:https (LISTEN)
nginx       537  www-data    9u  IPv6   20573      0t0  TCP *:https (LISTEN)
nginx       538  www-data    6u  IPv6   20570      0t0  TCP *:http (LISTEN)
nginx       538  www-data    7u  IPv4   20571      0t0  TCP *:http (LISTEN)
nginx       538  www-data    8u  IPv4   20572      0t0  TCP *:https (LISTEN)
nginx       538  www-data    9u  IPv6   20573      0t0  TCP *:https (LISTEN)
nginx       539  www-data    6u  IPv6   20570      0t0  TCP *:http (LISTEN)
nginx       539  www-data    7u  IPv4   20571      0t0  TCP *:http (LISTEN)
nginx       539  www-data    8u  IPv4   20572      0t0  TCP *:https (LISTEN)
nginx       539  www-data    9u  IPv6   20573      0t0  TCP *:https (LISTEN)
nginx       540  www-data    6u  IPv6   20570      0t0  TCP *:http (LISTEN)
nginx       540  www-data    7u  IPv4   20571      0t0  TCP *:http (LISTEN)
nginx       540  www-data    8u  IPv4   20572      0t0  TCP *:https (LISTEN)
nginx       540  www-data    9u  IPv6   20573      0t0  TCP *:https (LISTEN)
ssh         661      root    3u  IPv4 6825330      0t0  TCP 192.168.0.136:42693->99.subnet125-161-136.speedy.telkom.net.id:22222 (SYN_SENT)
avahi-dae   770     avahi   12u  IPv4   12986      0t0  UDP *:mdns
avahi-dae   770     avahi   13u  IPv6   12987      0t0  UDP *:mdns
avahi-dae   770     avahi   14u  IPv4   12988      0t0  UDP *:42676
avahi-dae   770     avahi   15u  IPv6   12989      0t0  UDP *:35529
/usr/sbin   941      root    5u  IPv6   16795      0t0  TCP localhost:spamd (LISTEN)
dhclient   1070      root    7u  IPv4   16832      0t0  UDP *:bootpc
spamd\x20  1242      root    5u  IPv6   16795      0t0  TCP localhost:spamd (LISTEN)
spamd\x20  1243      root    5u  IPv6   16795      0t0  TCP localhost:spamd (LISTEN)
dhclient   1282      root    7u  IPv4   16774      0t0  UDP *:bootpc
sshd       1384      root    3u  IPv4   21922      0t0  TCP *:ssh (LISTEN)
sshd       1384      root    4u  IPv6   21924      0t0  TCP *:ssh (LISTEN)
nginx      1427      root    6u  IPv6   20570      0t0  TCP *:http (LISTEN)
nginx      1427      root    7u  IPv4   20571      0t0  TCP *:http (LISTEN)
nginx      1427      root    8u  IPv4   20572      0t0  TCP *:https (LISTEN)
nginx      1427      root    9u  IPv6   20573      0t0  TCP *:https (LISTEN)
opendkim   1512  opendkim    4u  IPv6   21083      0t0  TCP localhost:12301 (LISTEN)
master     1654      root   12u  IPv4   23731      0t0  TCP *:smtp (LISTEN)
master     1654      root   13u  IPv6   23732      0t0  TCP *:smtp (LISTEN)
```

This netstat -antp command only available in Linux, and not in OSx or FreeBSD, hence I searched for the  command with similar output. Good thing that now I found one :)
