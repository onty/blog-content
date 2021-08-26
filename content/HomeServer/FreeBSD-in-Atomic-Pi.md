Title: FreeBSD in Atomic Pi
Date: 2021-08-04
Tags: Unix Linux CSGO FreeBSD
Category: HomeServer

So, I got Atomic PI back from 2019 around the house. I used it as my casual-non-mission-critical daily driver and have Parrot linux installed in it. It boots from eMMC, it detects the Condor webcam that came together bundled with the Atomic PI, it detects the wifi card albeit the reception is weak, it detects the bluetooth  hardware so that I can play youtube music via my bluetooth speaker (with Opera of course, forget about Firefox or Chrome), so everything is running fine as it should (not perfect, just fine) ... until that day came. Yep, like most [other](https://dlidirect.com/community/champ/forums/1778-atomic-pi-user-forum/topics/18140-don-t-hit-that-reset-button) Atomic PI owner, of course I accidentally pressed the eMMC bios reset button. The position of that button is 'strategically' located near the adaptor plug, I mean, what could've gone wrong anyway, right ?.. Yes, I know I can restore the UEFI and boot loader back using live USB stick, but this time  I wanted something different. I decided to install FreeBSD on it, but instead of putting the OS installation into the eMMC, I put it in the micro SD card. At least when someone accidentally pressed that eMMC bios reset button, it won't affect anything since I don't have my main OS installation in the eMMC card :p . The bios boot order will (should, in theory) still detect the UEFI from my FreeBSD installation.

Installing FreeBSD into Atomic PI's micro sd card involves several tricks. Lots of tips from [here](https://famicoman.com/2019/06/04/installing-freebsd-12-on-the-atomic-pi/) and [here](https://programmingmiscellany.wordpress.com/2020/04/16/freebsd-on-an-atomic-pi/) to install FreeBSD in atomic pi already and it is all correct, so I won't rewrite that again here. In my case I was using usb disk for the FreeBSD installer, and during the installation of course it was detected as the first USB device (sd0), and that my micro SD card is detected as the second device (sd1), what could've gone wrong again, right ? Yeah, first reboot after installation, I unplug the USB installer hoping that now it should boot from the newly installed micro SD card, but Atomic PI says no OS detected ! Did not took too much time for me to realize that the /etc/fstab by default will now place the micro SD as sd1 device and then when it tried to search for the kernel, for sure it won't find it because there's no such thing as sd1, only sd0 there is ... 

I am glad it was installed in micro SD card. I needed to update the /etc/fstab content and replace all the entries from sd1 into sd0. I have a Raspberry Pi 1B+ machine running FreeBSD 13 around, so I just need to mount the micro SD card via USB to Micro SD adapter from that machine (which happily detected the UFS partitions for / ), made the changes there and Voila, when I inserted it back to the Atomic PI it boots perfectly from 'sd0'. One obstacle solved.. 

The rest is pretty standard, I mountd an m2 SSD to it and format it as ZFS under `datazfs`, tricked /usr/src to be mounted on top of the ZFS (`/datazfs/SRC/`) in that SSD disk, and build custom kernel according to the standard FreeBSD documentations (see how the path was built in my uname -a output).

```bash

$ uname -a
FreeBSD bsdgw 13.0-CURRENT FreeBSD 13.0-CURRENT #0 r370304: Fri Aug 13 14:17:22 WIB 2021 root@bsdgw:/usr/obj/datazfs/SRCSYS/amd64.amd64/sys/THEPRASOJOS  amd64

```

