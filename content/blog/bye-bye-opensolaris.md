Title: Bye bye OpenSolaris ?
Date: 2010-8-14
Tags: OS Linux stuff OpenSolaris solaris
Category: Unix/Linux

So, I heard that OpenSolaris will be dead a.k.a discontinued.
Me my self, currently has no reason to use OpenSolaris. Why ? Simple question, what cant a Solaris box do compared to OpenSolaris ? currently Solaris also stil free, gcc stil runs on it, (sunfreeware.com ?). Need to install Oracle ? Oracle onlys supports Solaris distribution - not OpenSolaris. Need SUN's good old JDK ? use Solaris :) Not to mention that OpenSolaris distro's loves x86 too much instead Sparc ( well, almost all of my machines in my test lab were sparc :D ). Nexenta for example, the one that I -was- believe to be the ice breaker in Solaris world with their apt-get style, seems love x86 too much. Not too mention the stupidness of OpenSolaris AI installer for Sparc, which need an x86 OpenSolaris to be installed first, plus its additional macro thingy to be configured during wanboot. Why would I need that in Solaris ? Why cant I just plug the disc and do boot - install to my sparc machine ?

So now, there are only 2 options for my sparc machines, use Solaris, or Linux :D. Debian can run on Sparc platform. Just install sparc-utils, and we'll get the similar administration CLI just as we did on Sparc Solaris.

But too bad, Debian's apt package for solaris mostly compiled for 32 bit platform. If we need to boost the performace for our apps, we should re-compile it. No big deal, gcc is available :)
