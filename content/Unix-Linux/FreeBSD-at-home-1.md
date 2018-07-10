Title: FreeBSD at home (1)
Date: 2018-06-19
Tags: Unix Linux
Category: Unix/Linux


So, this past few weeks I have been playing around with FreeBSD. Been trying to replace the Raspbian OS for my Pine64 and Raspberry Pi 1 B. End up compiling the FreeBSD source for Pine64 since those img files provided by raspbsd.org doesn't seem stable, and obviously outdated. I used Google's cloud based instance with Intel processor and 2 GB of RAM., fetched the sources r335557 from svn, and voilla, this is what I ended up with :
```
$ uname -a
FreeBSD pegasus.theprasojos.id 12.0-CURRENT FreeBSD 12.0-CURRENT #0 r335557: Sat Jun 23 05:15:53 UTC 2018     root@freebsd-11-1-taiwan.c.theprasojos-ie.internal:/home/lintang_prasojo/crochet/work/obj/usr/src/arm64.aarch64/sys/GENERIC
```

Before spinning up a GCP instance, I tried to compile the source using the FreeBSD installed in the Pine64 itself. I was thinking there was no need to do a cross-source compilation for this since I believe Pine64 itself is enough ( 4 processors, 2 GB RAM, Gigabit Interface, plus un-stable FreeBSD img :p ). All of the 4 CPU always reached 100% (see below image), and I always end up getting weird error. So I decided, lets spin up a GCP instance and try to use the Free Credit I have :D

Anyway, long story short. That was the attempt for Pine64 on FreeBSD. I plan to use this board as IPv6 gateway among other things (it will be my next post).
I then continued with my other board, RPI1-B. My initial intention was to replace the Raspbian OS that holds the installation for my web cameras to FreeBSD. Of course, driver issue for the camera was the most annoying problem at the beginning, since FreeBSD only detected my Logitech webcam as ugen0.x device. For this board, I did not compile the source using crochet, but instead I used the 12-Current *r335760* version (well, actually I also tried 11-2 Release and 11-2 Stable too, but somehow the *cuse4bsd*, *webcamd*, and *Motion* did not work well together, my webcam did not detected properly, hence the 12-Current).

```
$ dmesg| grep ugen
ugen0.1: <DWCOTG OTG Root HUB> at usbus0
ugen0.2: <vendor 0x0424 product 0x9514> at usbus0
ugen0.3: <vendor 0x0424 product 0xec00> at usbus0
ugen0.4: <vendor 0x046d Webcam C170> at usbus0
ugen0.5: <FTDI FT232R USB UART> at usbus0
ugen0.6: <vendor 0x046d product 0x0802> at usbus0
```

After spending some time browsing the net, the following website gave me enough clue on what I need to do by utilizing *webcamd* and *cuse4bsd*.

*http://www.rockafunk.org/InstallWebcamd.html*

So this *webcamd* looks like a middle layer driver in FreeBSD that deals with webcam, DVB, and some remote control usb devices. After enabling this *webcamd*, I began to see the device /dev/videoX in my FreeBSD which then will be used by the actual webcam software ( I used Motion for this). Webcamd requires a kernel module called *cuse*. To make sure that your FreeBSD has this module compiled, go to */boot/kernel/*, there you should see a file called *cuse.ko*. This will then needs to be loaded using *kldload* command.
Here's before the *cuse* module was loaded :

```
root@phoenix:~ # kldstat
Id Refs Address                Size Name
 1    1 0xffff000000000000  13d7bb8 kernel
```

And here's after the module was loaded :
```
root@phoenix:~ # kldload cuse
root@phoenix:~ # kldstat
Id Refs Address                Size Name
 1    2 0xffff000000000000  13d7bb8 kernel
 2    1 0xffff00005ce00000    41000 cuse.ko
```

Eh , but what if we don't have this *cuse* installed yet in our system ? Well, since I used RPI1-B, compiling from the ports source tree is the laaaast thing I want to do. So grab your coffee and start pkg-ing :). Install a package called *cuse4bsd-kmod*. And don't forget to install the *webcamd* package as well. Installing these 2 packages might take some time, so I used to run *screen* (or tmux if you prefer), and executes everything from there. It surely gave me the flexibility to simply go back to the session where I left it off ( especially if the internet connection is not *speedy* enough to reach a FreeBSD mirror somewhere in Japan :p ).

Also, one important thing. Since I wanted this *cuse* module to be loaded everytime my server gets re-booted, I added below entry in my */boot/loader.conf*.
```
cuse_load="YES"
```

Now, since *webcamd* is supposed to create a new file that represents the device, here's how *devfs* comes into play. Since the new file/device needs to be accessed by other third party programs (Motion on this case), then it has to have the correct permission. This can be configured in */etc/devfs.rules* by adding below :
```
[system=10]
add path 'video*' mode 0666
```
This will ensure that later on, /dev/videoX will have the necessary permission to be able to read by *Motion*.

Next is the usual *rc.conf* style configuration in BSD/Unix. I added the following line to enable all the daemon during the boot time.
```
webcamd_enable="YES"            # enabling the webcamd
devfs_system_ruleset="system"   # enabling the devfs.ruleset
motion_enable=YES               # enabling the Motion software
```

Don't forget to restart the devd daemon:
```
root@phoenix:~ # service devd restart
```

And now, the (almost) final peace, which is the device creation to represent our webcam. My web cameras are Logitech, and according to the dmesg entry above, it was detected below (notice the vendor id 0x046d belongs to Logitech ):

```
ugen0.4: <vendor 0x046d Webcam C170> at usbus0
ugen0.6: <vendor 0x046d product 0x0802> at usbus0
```

Now to create /dev/videoX, all we need to do is to execute the following command :
```
root@phoenix:~ # webcamd -d ugen0.6 -i 0 -v 0   ==> this will create /dev/video0
root@phoenix:~ # webcamd -d ugen0.4 -i 0 -v 1   ==> this will create /dev/video1
```

The order of which ugen0 device that should be /dev/video0 or /dev/video1 doesn't matter for me. It will then be handled by *Motion* software anyway.


That's it. The webcam is now ready to be used by *Motion*, so next is the *Motion* software configuration which I will not cover on this post.

Few things I noted after running FreeBSD in Pine64 and RPI1B. Those RPI1B 12-Current seems a bit lagging after cuse, webcamd, and motion was installed. I either suspect the SDCard, or the CPU specs of RPI1B. But then, this lagging problem remains even after I replaced the SDCard with the new one, while the RAM utilisation it self was low, never reach more than 128MB (RPI1B has 512MB RAM). On the other hand, I observed that sometimes the CPU spikes until 100%. This high CPU utilisation seem to affect the connectivity. I can see that the USB Camera is still working ( the light was On), but I could not reach/ssh the RPI. At this point after several time testing, I decided to switch back to Raspbian for my RPI1B.

How about the Pine64 FreeBSD ? until the next post... :)
