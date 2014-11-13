Title: Solaris Jumpstart on Linux
Date: 2010-8-10
Tags: jumpstart Unix Linux stuff solaris

**_Intro :_
**
\- Linux, Debian based (mine: Lenny), hostname : pegasus, act as the Solaris jumpstart server.
\- Solaris, Solaris 10, hostname: solclient, will be the machine to be installed.
\- IP addresses range 192.168.10.x (class C), make sure you use standard network class IP, this is where the standard broadcast address (192.168.10.255) comes into play during arp broadcast.
\- solclient will broadcast arp request, replied by pegasus's rarpd, and then and IP address will be assigned. solclient will then download the minimum kernel using tftp. The kernel file name will be the ip address of the solclient. For example, if the assigned IP is 192.168.10.5, and then the kernel name will be C0A80A05. Another way is to use this command:
```
elinpra@pegasus > printf "XXXXn" 192 168 10 5
C0A80A05
```
This file should be stored inside the root directory of tftp. Check the tftp setting on **/etc/inetd.conf**. Here is mine:

```
elinpra@pegasus > cat /etc/inetd.conf
tftp dgram udp4 wait nobody /usr/sbin/tcpd /usr/sbin/in.tftpd /srv/tftp/
```
Then, the file C0A80A05 should be put in** /srv/tftp**.

Steps :

1\. Install bootparamd, rarpd, tftpd and nfs-kernel-server in Linux server (pegasus)
```
root@pegasus > apt-get install bootparamd rarpd tftpd nfs-kernel-server
```
2\. Run iptables -F, make sure no firewall in Linux server
```
root@pegasus > iptables -F
```
3\. Check the mac address of the solaris client.
Try boot from {ok}, see the mac address during booting (if the system is currently up, go to init 0 mode) :
```
ok boot net

Resetting ...
LOM event: 56d 21h39m43s host reset

þ
Sun Fire V120 (UltraSPARC-IIe 648MHz), No Keyboard
OpenBoot 4.0, 1024 MB memory installed, Serial #61911409.
Ethernet address 0:3:ba:b0:b1:71, Host ID: 83b0b171.

Back to lom> or sc> using 'break' command.
```

4\. Set **/etc/ethers** and **/etc/hosts** in Linux server with the mac address and hostname of the solaris client.

```
elinpra@pegasus > echo "0:3:ba:b0:b1:71 solclient" >> /etc/ethers
elinpra@pegasus > echo "192.168.10.5 solclient" >> /etc/hosts
```

5\. Start the rarpd if has not started yet.( I’m using debian based linux here )
```
root@pegasus > /etc/init.d/rarpd start
```

6\. If you're installing using Solaris iso file, mount the iso file to a directory using the following command, otherwise if using Solaris CD/DVD, directly go to step 8:
```
root@pegasus > mkdir -p /mnt/sol10
root@pegasus > mount -o loop solaris_iso_file.iso /mnt/sol10
root@pegasus > cd /mnt/sol10
```

7\. If you have the Solaris 10 CD, insert it on pegasus, do the following steps :
```
root@pegasus > cd /mnt/cdrom/ (to your solaris cdrom directory)
```

8\. Find the suitable kernel for your machine type. Mine is SunFire v120, so it will be sun4u type. If your hardware is T5220, T2000 etc then you need sun4v kernel.
Locate the kernel on directory Solaris_10/Tools/Boot/platform/sun4u/inetboot for sun4u, or Solaris_10/Tools/Boot/platform/sun4v/inetboot for sun4v.
Copy it to **/srv/tftp** and make symbolic link to that file into C0A80A05.

```
root@pegasus > cp inetboot /srv/tftp
root@pegasus > ln -s /srv/tftp/inetboot /srv/tftp/C0A80A05
```

9\. Start tftpd daemon in pegasus :
```
root@pegasus > /etc/init.d/openbsd-inetd restart
```

10\. start nfs service in pegasus :
```
root@pegasus > /etc/init.d/nfs-kernel-server start
```

11\. Prepare nfs mount so that solclient later on can download the entire installation package using nfs mount. Set the mount root into where the cdrom or iso files are mounted. Make sure that the nfs mount root from solclient is /sol10.

```
root@pegasus > exportfs *:/mnt/cdrom -o fsid=0,ro,no_root_squash,crossmnt,no_subtree_check,sync exportfs *:/mnt -o fsid=0,ro,no_root_squash,crossmnt,no_subtree_check,sync Check if the nfs shares can be mounted correctly.
```
