Title: IPv6 at home
Date: 2018-07-01
Tags: Unix Linux
Category: Unix/Linux

So I have this plenty of time to kill, and I decided to do something with the Pine64 board. Currently it's powered by Ubuntu Xenial base Image by Longsleep, and everything was fine (well the initial boot up was stuck couple of times, and I have to reset it several times until it boots properly, but overall it's ok). Then I was thinking to leave out of the comfort zone by putting FreeBSD on it. Before that, I have tried Remix OS (nice GUI, pretty stable, useful for Multimedia use), Android (the worse and slowest OS I have ever run on this board). I have to say with Ubuntu OS installed there, I did not use it that much. I put Postfix mail server, Nginx webserver, and that's it. Sometime I also use it to run some disk/partition repair job for my 1TB disk using the *TestDisk* tool (pretty cool stuff from cgSecurity, well done guys).

Anyway, back to the topic. I have to be in Indonesia for quite some time, and in here the ISP only gave us 1 IPv4 public dynamic IP Address ( and thats it :p ). In Dublin, my ISP gave us set of IPv6 addresses, so I can put every board/devices and assign each one of them with a unique IPv6 Address. This is very useful for me passing my Sage certified from HE (thanks for the cool t-shirt there). I can't reach my board in Dublin because of this. Then I stumbled upon the tunnel broker feature from HE. It's basically provides the tunnel mechanism from IPv4 to IPv6. This is a perfect fit for my needs, and I was thinking that doing this with FreeBSD might be just the challenge I need. I began my search in google, and stumbled upon these URL's that helped me a lot to understand what needs to be done.

https://www.sixxs.net/faq/connectivity/?faq=usingsubnet&os=kame.host
https://forums.he.net/index.php?topic=1128.0
https://www.freebsddiary.org/ipv6.php
https://www.slashorg.net/read-141-IPv6-routing-using-FreeBSD.html

First is to figure out the network diagram. Currently I have a fiber modem that also acts as a router and DHCPv4 server. This is pretty much a normal setup for everyone with internet home connectivity. I don't see any IPv6 setup related there, so quick assumption, it doesn't support IPv6. But it's ok, I just need the IPv4 tunnel to be passed through to it, nothing IPv6 specific I expected this modem to do anyway. Also, the idea after setting up this tunnel is that, it should also act as a IPv6 gateway for the other devices that I have at home. So yeah, the end goal will be IPv6 for all home devices.

![Home IPv6 network plan]({filename}/images/Matoa-IPv6 for Home.png)
