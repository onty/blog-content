Title: Tora(Toolkit for Oracle) Installation
Date: 2007-6-1
Tags: Linux stuff
Category: Unix/Linux

Yesterday I managed to install my laptop with Tora. I'm using Kubuntu Feisty Fawn.For you who doesnt have any idea what kind of animal Tora is, let me give you some hint. If you used to use Toad in M$-Windows to do your oracle database-related jobs, well, you can say that Tora has similar usage.It can runs on Linux, make your life simpler, and easier, he he. Hey, it's your laptop that should work for you, not you're the one that has to work for your laptop, right ?
Ok, here's the step I saved from my installation adventure :

1\. get Oracle instant client
You can get it here :
http://download.oracle.com/otn/linux/instantclient/instantclient-basic-linux32-10.2.0.3-20061115.zip
http://download.oracle.com/otn/linux/instantclient/instantclient-sdk-linux32-10.2.0.3-20061115.zip

2\. Unzip it at some directory, e.g : /opt/instantclient_10_2

3\. Add the directory to /etc/ld.so.conf, dont forget run /sbin/ldconfig.
Here's the sample from my laptop :
\------------------
onty@phoenix:~$ cat /etc/ld.so.conf
/lib
/usr/lib
/usr/lib/firefox/plugins
/opt/instantclient_10_2
\------------------

4\. Install libqscintilla.
Thank God, I'm using Kubuntu,and having great internet connection in my office. So just simply run apt-get.
root@phoenix:/opt# apt-get install libqscintilla6 libqscintilla-dev

5\. Download and Unzip tora
You can get it [here][1]. I'm using version 1.3.21.

6\. compile start
oracle@phoenix:/opt/tora-1.3.21$ ./configure --with-qt-dir=/usr/lib/qt3 --with-oracle-libraries=/opt/instantclient_10_2 --with-oracle-includes=/opt/instantclient_10_2/sdk/include --with-oci-version=10G --with-instant-client
oracle@phoenix:/opt/tora-1.3.21$ make
oracle@phoenix:/opt/tora-1.3.21$ make install

7\. In the midde of make, I'm getting error says that toThreadStartWrapper has not been declared. I googled around to find the solution, and found out that I have to edit a file named tothread.cpp around line 157 like below.

#define THREAD_ASSERT(x) if((x)!=0) {
throw (qApp->translate("toThread","Thread function "%1" failed.").arg(QString::fromLatin1( #x ))); }

/* new added start */
void *toThreadStartWrapper(void *t);
/* new added end */

void toThread::initAttr()

After that, I continued with make, and make install.

And finally, run ./tora and you can see ORACLE option in your connection. That connection refers to wherever you put our TNSNAMES.ORA in your ORACLE_HOME.


OK, that's for today's tip.

[1]: http://sourceforge.net/projects/tora
