Title: Playing around with low end VPS box
Date: 2010-4-5
Tags: Tips Unix Linux stuff Web Server Nginx
Category: Unix/Linux

Last week I just bought a VPS account for playing around with. It feels so great having our own shell account with root login so that we can do anything inside. I bought it from [here][1]. First of all, I bought the minimalist one, with 64mb memory, with no burstable ram :D, using Centos. I simply cant do anything, their Centos installation itself took around 20-30mb ram. I also not well enough playing with Yum. This is not great, so I upgraded the account to 128mb ram. At the same time I noticed that besides Centos, the hosting provider also provide Debian Lenny as the OS....why dont you said that from the beginning ??? :D Now, I'm running Lenny with 128mb ram. The VM specs itself it's not that bad, considering it's powered with 2 cpu @3Ghz, 128mb ram with no swap ( this guy [here][2] shares a great script to create a fake swap, but I dont need it any longer ;) read the rest of the entry to know why... ), and with 10Gb disk, more than enough storage for minimalist like me :)

So, first thing first, chop all the unnecessary program, replace it with the program with smaller 'cost'. Just do ps -ef and there I found apache2 and Sendmail sitting around and eating my memory. Just do :

```
# apt-get remove --purge sendmail apache2
```
And dont forget to kill them, and remove them from startup script.
```
# kill -9 pid
# update-rc.d -f remove apache2
# update-rc.d -f remove sendmail
```
Ok, that left me around 5 mb used memory. Not bad :)
Next thing is to replace the default shell, since bash shell become greedy enough to eat my memory. I replaced it with pdksh since after googling around, this pdksh shell saves ~1mb for every shell session...good enough. So I install it :
```
# apt-get install pdksh
```
Dont remove the bash shell yet, since it has a lot of dependencies. Leave it there, but dont use it :) How do we do that ? Just edit your own default shell to become pdksh in /etc/passwd :
```
# vi /etc/passwd
```
Change the line using /bin/bash, into /bin/pdksh, and voillaa, next login session will be using pdksh.


Not enought with just # prompt ? It's time to decorate your shell with some fancy prompts, just edit the .profile located inside the user's home directory ( just do ls -la to see it, since it's a hidden file ). Add the following line :


	:::term
	HOSTNAME=`hostname`
	PS1=`print "


[1]: http://www.pasarhosting.com
[2]: https://www.vpsmart.com/clients/knowledgebase.php?action=displayarticle&id=4
