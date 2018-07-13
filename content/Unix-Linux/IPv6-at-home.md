Title: FreeBSD at Home (2) : IPv6 Setup for Home Network
Date: 2018-07-01
Tags: Unix Linux
Category: Unix/Linux

So I have this plenty of time to kill, and I decided to do something with the Pine64 board. Currently it's powered by Ubuntu Xenial base Image by Longsleep, and everything was fine (well the initial boot up was stuck couple of times, and I have to reset it several times until it boots properly, but overall it's ok). Then I was thinking to leave out of the comfort zone by putting FreeBSD on it. Before that, I have tried Remix OS (nice GUI, pretty stable, useful for Multimedia use), Android (the worse and slowest OS I have ever run on this board). I have to say with Ubuntu OS installed there, I did not use it that much. I put Postfix mail server, Nginx webserver, and that's it. Sometime I also use it to run some disk/partition repair job for my 1TB disk using the *TestDisk* tool (pretty cool stuff from cgSecurity, well done guys).

Anyway, back to the topic. I have to be in Indonesia for quite some time, and in here the ISP only gave us 1 IPv4 public dynamic IP Address ( and thats it :p ). In Dublin, my ISP gave us set of IPv6 addresses, so I can put every board/devices and assign each one of them with a unique IPv6 Address. This is very useful for me passing my Sage certified from HE (thanks for the cool t-shirt there).

<p align="center">
<img width="300" height="350" src="{filename}/images/sage.jpg"/>
</p>

Now I can't reach my board in Dublin from Jakarta because of this, unless I setup the IPv6 cloud at my premise in Jakarta too. Then I stumbled upon the tunnel broker feature from HE. It basically provides the tunnel mechanism from IPv4 to IPv6. This is a perfect fit for my needs, and I was thinking that doing this with FreeBSD might be just the challenge I need. I began my search in google, and stumbled upon these URL's that helped me a lot to understand what needs to be done.

[https://www.freebsd.org/doc/handbook/network-ipv6.html](https://www.freebsd.org/doc/handbook/network-ipv6.html)

[https://www.sixxs.net/faq/connectivity/?faq=usingsubnet&os=kame.host](https://www.sixxs.net/faq/connectivity/?faq=usingsubnet&os=kame.host)

[https://forums.he.net/index.php?topic=1128.0](https://forums.he.net/index.php?topic=1128.0)

[https://www.freebsddiary.org/ipv6.php](https://www.freebsddiary.org/ipv6.php)

[https://www.slashorg.net/read-141-IPv6-routing-using-FreeBSD.html](https://www.slashorg.net/read-141-IPv6-routing-using-FreeBSD.html)


First is to figure out the network diagram. Currently I have a fiber modem that also acts as a router and DHCPv4 server. This is pretty much a normal setup for everyone with internet home connectivity. I don't see any IPv6 setup related there, so quick assumption, it doesn't support IPv6. But it's ok, I just need the IPv4 tunnel to be passed through to it, nothing IPv6 specific I expected this modem to do anyway. Also, the idea after setting up this tunnel is that, it should also act as a IPv6 gateway for the other devices that I have at home. So yeah, the end goal will be IPv6 for all home devices with minimum changes on the current IPv4 network setup. This means for all IPv4 related (gateway/router, DHCPv4 server), existing node must be kept as is, while introducing the IPv6 layers on top of it seamlessly.

<p align="center">
<img src="{filename}/images/Matoa-IPv6-2.png"/>
</p>

I started the setup by creating a new tunnel in my HE tunnelbroker account. There's no specific preferance, but I have to bridge the connection between Jakarta and Dublin, so I will avoid those tunnel servers in US or Japan. So far I have tried those tunnel in Singapore, but it seems less stable than the Frankfurt one. London might be a better choice. Anyway, I have set it up using the tunnel server in Frankfurt. The following information from HE tunnelbroker that we just created will be required to setup our IPv6 gateway :

<p align="center">
<img width="400" height="450" src="{filename}/images/he-setup.png"/>
</p>

Here's what I setup in my rc.conf to build the HE IPv6 tunnel:

```
ipv6_activate_all_interfaces=YES
cloned_interfaces="gif0"
create_args_gif0="tunnel 192.168.1.98 216.66.80.30"

ifconfig_awg0_ipv6="inet6 [first address of routed /48 (::1) ] prefixlen 64"
ifconfig_gif0_ipv6="inet6 [client ipv6 address] [server ipv6 address] prefixlen 128"
ipv6_defaultrouter="-interface gif0"
ipv6_gateway_enable="YES"
```

My Pine64 network interface was detected as *awg0* by FreeBSD. The tunnel interface itself is *gif0*. First try is to ping an IPv6 address from this gateway.

```
$ ping6 ipv6.google.com
PING6(56=40+8+8 bytes) xxxx:yyyy:zzzz:355::2 --> 2404:6800:4003:c04::65
16 bytes from 2404:6800:4003:c04::65, icmp_seq=0 hlim=45 time=485.395 ms
16 bytes from 2404:6800:4003:c04::65, icmp_seq=1 hlim=45 time=486.170 ms
```

Looks good ! My gateway can ping the other IPv6 address out there. Hello World6!
Now, the next thing is to configure the rest of the home network to be able to get IPv6 address too. This is where SLAAC comes into play.

The software I used is *rtadvd* which comes as a basic package in FreeBSD. This software supposed to advertise the IPv6 address assignment and routing towards my local network.

To setup the IPv6 address and routing advertisement, the following also required in */etc/rtadvd.conf*.

```
awg0:\
	:addrs#1:addr="xxxx:yyyy:zzzz:358::":\
	:prefixlen#64:\
	:tc=ether:\
	:raflags#192:\
	:rdnss="2001:db8:1221::1,2001:4860:4860::8888,2001:4860:4860::8844":
```

And don't forget to enable rtadvd in rc.conf file :
```
rtadvd_enable="YES"             # let our LAN know the IPv6 default route
rtadvd_interfaces="awg0"      
```

Just to make sure, I rebooted the gateway. I also did some tcpdump to see what are the packets that actually flying around that causes all the client gets their own IPv6 address assignment.

<p align="center">
<img width="500" height="350" src="{filename}/images/solicitat.png"/>
</p>

Then after that, obviously go to one of the client machine, e.g your mac or your linux (or windows, whatever) and perform the following configuration below before pinging some IPv6 address like www.v6.facebook.com from there.

- Linux

Set the following parameter, you can put it on sysctl.conf to make it survive after reboot.

```
net.ipv6.conf.wlan0.accept_ra=1
net.ipv6.conf.wlan0.forwarding=0
```
- FreeBSD

Set the following parameter. You can also put it on sysctl.conf

```
net.inet6.ip6.accept_rtadv=1
net.inet6.ip6.forwarding=0
```

If you don't want to reboot, make sure sysctl is re-reading the new entry in sysctl.conf by performing below as root :
```
# sysctl -f /etc/sysctl.conf
```

If the ping still failed from the client, there might be something wrong with the client's routing table. You might want to check if there's another router in your network soliciting a different IPv6 gateway for you ( because that is what happened to me :p). I was stuck for couple of days because of the client always get a strange default gateway that points to *fe80::1*, wth is this route advertisement come from. then I took the tcpdump and 1 string came up in **clear**

<p align="center">
<img width="500" height="350" src="{filename}/images/router-adv.png"/>
</p>

Yeah, I forgot that my switch is actually not-so-dummy switch. Instead it was actually modem/router from different ISP of which I already terminate the contract but they did not want their CPE back, so I used them as *dummy switch*. This *switch* turns out has the capability to support IPv6 by broadcasting their own Router Solicitation message. It broadcasts their own configured gateway fe80::1 into the network, making all the devices in the network to accept this address as their default IPv6 gateway. Now, the worst part, I can't seem to disable it :D. So, I decided to put a dirty hacks by changing the address fe80::1 into something *bigger* than the local-link address of my IPv6 tunnel gateway. I set it to fe80:ffff:ffff:ffff:ffff::1 :D. Here's the routing list shown in one of the IPv6 client after the changes was made.

```
pi@ebookserver:~ $ ip -6 route show
2001:470:36:9c8::/64 dev wlan0 proto kernel metric 256  expires 2591718sec pref medium
fe80::/64 dev wlan0 proto kernel metric 256  pref medium
default via fe80::ba:22ff:fea0:5651 dev wlan0 proto ra metric 1024  expires 1518sec hoplimit 64 pref medium
default via fe80:ffff:ffff:ffff:ffff::1 dev wlan0 proto ra metric 1024  expires 1518sec mtu 1472 hoplimit 64 pref medium
```

> I called this *the poorman's switch hacks*.

Now all devices at my home (except those Android mobile phone) is using IPv6.

<p align="center">
<img width="300" height="350" src="{filename}/images/WhatIs.png"/>
</p>
