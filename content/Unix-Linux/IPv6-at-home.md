Title: FreeBSD at Home (2) : IPv6 Setup for Home Network
Date: 2018-07-01
Tags: Unix Linux
Category: Unix/Linux

So I have this plenty of time to kill, and I decided to do something with the Pine64 board. Currently it's powered by Ubuntu Xenial base Image by Longsleep, and everything was fine (well the initial boot up was stuck couple of times, and I have to reset it several times until it boots properly, but overall it's ok). Then I was thinking to leave out of the comfort zone by putting FreeBSD on it. Before that, I have tried Remix OS (nice GUI, pretty stable, useful for Multimedia use), Android (the worse and slowest OS I have ever run on this board). I have to say with Ubuntu OS installed there, I did not use it that much. I put Postfix mail server, Nginx webserver, and that's it. Sometime I also use it to run some disk/partition repair job for my 1TB disk using the *TestDisk* tool (pretty cool stuff from cgSecurity, well done guys).

Anyway, back to the topic. I have to be in Indonesia for quite some time, and in here the ISP only gave us 1 IPv4 public dynamic IP Address ( and thats it :p ). In Dublin, my ISP gave us set of IPv6 addresses, so I can put every board/devices and assign each one of them with a unique IPv6 Address. This is very useful for me passing my Sage certified from HE (thanks for the cool t-shirt there). I can't reach my board in Dublin because of this. Then I stumbled upon the tunnel broker feature from HE. It's basically provides the tunnel mechanism from IPv4 to IPv6. This is a perfect fit for my needs, and I was thinking that doing this with FreeBSD might be just the challenge I need. I began my search in google, and stumbled upon these URL's that helped me a lot to understand what needs to be done.

[https://www.sixxs.net/faq/connectivity/?faq=usingsubnet&os=kame.host](https://www.sixxs.net/faq/connectivity/?faq=usingsubnet&os=kame.host)

[https://forums.he.net/index.php?topic=1128.0](https://forums.he.net/index.php?topic=1128.0)

[https://www.freebsddiary.org/ipv6.php](https://www.freebsddiary.org/ipv6.php)

[https://www.slashorg.net/read-141-IPv6-routing-using-FreeBSD.html](https://www.slashorg.net/read-141-IPv6-routing-using-FreeBSD.html)

First is to figure out the network diagram. Currently I have a fiber modem that also acts as a router and DHCPv4 server. This is pretty much a normal setup for everyone with internet home connectivity. I don't see any IPv6 setup related there, so quick assumption, it doesn't support IPv6. But it's ok, I just need the IPv4 tunnel to be passed through to it, nothing IPv6 specific I expected this modem to do anyway. Also, the idea after setting up this tunnel is that, it should also act as a IPv6 gateway for the other devices that I have at home. So yeah, the end goal will be IPv6 for all home devices with minimum changes on the current IPv4 network setup. This means for all IPv4 related (gateway/router, DHCPv4 server), existing node must be kept as is, while introducing the IPv6 layers on top of it seamlessly. Later I came to know that this decision might have some consequences, especially the default gateway assignment setup for each IPv6 client node. I will highlight this later.

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
rtadvd_enable="YES"             # let our LAN know the IPv6 default route
rtadvd_interfaces="awg0"      
```

My Pine64 network interface was detected as *awg0* by FreeBSD. The tunnel interface itself is *gif0*. There I also utilise *rtadvd* which comes as a basic package in FreeBSD to advertise the IPv6 address assignment and routing towards my local network.

To setup the IPv6 address and routing advertisement, the following also required in */etc/rtadvd.conf*.
```
awg0:\
	:addrs#1:addr="[range address of routed /48 ]":\
	:prefixlen#64:\
	:tc=default:\
	:raflags#192:\
	:rdnss="2001:db8:1221::1,2001:4860:4860::8888,2001:4860:4860::8844":
```

> To be continued.
