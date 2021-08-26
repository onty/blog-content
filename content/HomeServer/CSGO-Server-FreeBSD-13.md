Title: CSGO dedicated server in FreeBSD 13
Date: 2021-08-24
Tags: Unix Linux CSGO FreeBSD
Category: HomeServer

Now, a CSGO server in FreeBSD 13 ....
I figure out nobody ever really documented this kind of installation before (and since FreeBSD 13 is just recently released). Most people will just use Linux GSM, some of them uses Docker and that is great, it's what it's meant for, to make portable apps running portably from one machine to another without having to solve it's dependancy bloat.. but I am using FreeBSD...


First thing first. Install the obvious package name from FreeBSD that has the word 'steam' on it :

```bash
$ pkg search steam
bitlbee-steam-1.4.2            Steam plugin for bitlbee
linux-steam-utils-20210616     Steam launcher for FreeBSD

```

The `linux-steam-utils` package above is the one we need to target. It utilizes FreeBSD's compatibility layer for Linux. When I installed it for the first time, it failed. After the usual copy-pasting the error message to Google search engine, the solution was pretty simple, to load the `linux` and `linux64` kernel module before installing the package, and this solutions looks to be specific to FreeBSD >= 13.00. Here's my resulting `kldstat` looks like :

```bash
22    1 0xffffffff8265e000    389e8 linux.ko
23    1 0xffffffff82697000    31bb8 linux64.ko

```

So, hold on, why do we need both `linux` and `linux64` module if the `linux-steam-utils` is for 64 bit architecture ? (see below)
```bash
$ pkg info linux-steam-utils
linux-steam-utils-20210616
Name           : linux-steam-utils
Version        : 20210616
Installed on   : Mon Aug  9 19:06:44 2021 WIB
Origin         : games/linux-steam-utils
Architecture   : FreeBSD:13:amd64 <== 64 bit architecture
Prefix         : /usr/local
Categories     : linux games
Licenses       : MIT
Maintainer     : iwtcex@gmail.com
WWW            : https://github.com/shkhln/linuxulator-steam-utils
Comment        : Steam launcher for FreeBSD
Annotations    :
        FreeBSD_version: 1300139
        repo_type      : binary
        repository     : FreeBSD
Flat size      : 452KiB
Description    :
A set of workarounds for running the Linux Steam client under FreeBSD.

WWW: https://github.com/shkhln/linuxulator-steam-utils
```

The answer is because while the `steam` client is 64 bit, the game itself (e.g CS GO) runs on 32 bit mode, so we will eventually need it later on when we run the game server.

Load the kernel module by using `kldload` command :

```bash

$ kldload linux64
$ kldload linux 
```

Then we can install the `linux-steam-utils` package with the usual `pkg install` command. I did not bother compiling it from ports, which is good thing. I always choose to install any package from `pkg` for simplicity reason.

Now, once it's installed, create a new dedicated user (steam) for all `steam` related process, and allocate disk space for it. I am using ZFS, so here's the command I used to allocate disk space (assuming your ZFS *tank* is in `datazfs` :

```bash
# zfs create datazfs/STEAM
# zfs set compression=lz4 datazfs/STEAM
# chown -R steam:steam /datazfs/STEAM

```
And since we rely pretty much on the Linux compatibility layer of FreeBSD, the following special files needs to be mounted. Put the following in `/etc/fstab` :

```bash
tmpfs    /compat/linux/dev/shm  tmpfs   rw,mode=1777    0       0
linprocfs   /compat/linux/proc  linprocfs       rw      0       0
linsysfs   /compat/linux/sys  linsysfs       rw      0       0
fdesc /dev/fd fdescfs rw 0 0
proc            /proc           procfs  rw,noauto       0       0


```

Although manual mount can be used to mount all those special files once added to `/etc/fstab`, at this point I'd prefer rebooting the machine just to ensure that those files will automatically be mounted during startup.

Now, let's switch to user `steam`  and install the Steam app as below. It will put all the required library under `/home/steam` directory.

```bash
$ steam-install

```

And run the following command to get into `Steam>` prompt.

```bash
$ LD_LIBRARY_PATH=/home/steam/linux32/ steam -textclient
```

Now to install the actual CSGO dedicated server following the steps outlined [here](https://developer.valvesoftware.com/wiki/Counter-Strike:Global_Offensive_Dedicated_Servers)

```bash
Steam> force_install_dir /datazfs/STEAM/
Steam> login anonymous
Steam> app_update 740 validate
```

And finally, still as `steam` user, run the following to start the CSGO dedicated server :

```bash
$ cd /datazfs/STEAM
$ LD_LIBRARY_PATH=/home/steam/linux32/:$LD_LIBRARY_PATH ./srcds_run -game csgo -console -usercon +game_type 0 +maxplayers 8 +game_mode 0 +mapgroup mg_active +map de_dust2 +sv_setsteamaccount [Game Server Login Token] -autoupdate

```

More information about Game Server Login Token can be found [here](https://docs.linuxgsm.com/steamcmd/gslt).
I observed lots of debugging-related message when starting the `steam -textclient` command, but so far it's all just a debugging message and nothing to worried about. Below is a good indicator message to see whether the dedicated server is ready to start hosting game and accept connections:

```bash
Connection to Steam servers successful.
   Public IP is xxx.xxx.xxx.xxx.
Assigned anonymous gameserver Steam ID [A:1:155311110:18312].
Gameserver logged on to Steam, assigned identity steamid:9015064214xxxxxxx
Set SteamNetworkingSockets P2P_STUN_ServerList to '103.10.124.165:3478' as per SteamNetworkingSocketsSerialized
VAC secure mode is activated.
GC Connection established for server version 1316, instance idx 1

```


Enjoy CSGO with your Friends and Family !
