Title: Solaris, SNMP, and OpenNMS
Date: 2007-6-3
Tags: 

These day, I explore about SNMP. After wikipedia-ing in [here][1], I try to install one of the recomended software called OpenNMS. After tried the live demo, it looks cool. So I decided to download it in [here][2].
I followed all the installation step guide from [here][3]. I also need to download and install the pre requisites package such as rrdtool, and the postgresql. Fortunately, blastwave.org has great tools called pkg-get, yeap, sounds familiar with you Debian users ? I also thought that only Nexenta OS has this such-thing tools, but now, all solaris distro can use this tools I guess, well, at least I tried that one and it works for Solaris in both Sparc and Intel machine.
Ok, back to the tools. If we followed the step exactly, and goes to this step : install -dis, I got an error said that fail to load the iplike.so because libgcc_so.1 not found. That's some problem I usually got on linux box. If this is linux box, I just have to locate it, insert the path to /etc/ld.so.conf, and run the /sbin/ldconfig as root. But this is solaris box, cant do that, so, after googling, I found the crle command. I tried that to point the location for shared object files. Still no works. Howcome ? Dont ask me, it just doesnt work:p, So...again, googling, and found same problem in [here][4]. So the problem will be solved by just copying the .so files to /usr/lib ? And, it works. This is weird, I alredy put the /usr/lib within the crle command like this :


-bash-3.00# crle -l /usr/local/lib:/usr/sfw/lib:/lib:/usr/lib/:/opt/opennms/lib:/usr/sfw/lib/gcc/sparc-sun-solaris2.10/3.4.3/



Ah, no idea, so I run the install -dis again, and this time it works.....


Next, playing around with OpenNMS and try to setup the weblogic snmp agent to send trap message to the OpenNMS poller. We'll see....



originally posted 4/11/07

[1]: http://en.wikipedia.org/wiki/Simple_Network_Management_Protocol
[2]: http://downloads.sourceforge.net/opennms/opennms-1.3.2-1-sol10-sparc-local.gz?modtime=1168971264&big_mirror=0
[3]: http://www.opennms.org/documentation/InstallUnStable.html
[4]: http://www.experts-exchange.com/Software/Server_Software/Web_Servers/Q_22464371.html
