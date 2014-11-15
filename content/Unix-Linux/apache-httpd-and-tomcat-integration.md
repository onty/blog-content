Title: Apache Httpd and Tomcat integration using mod_jk, part 1
Date: 2007-6-3
Tags: 
Category: Unix/Linux

In my other blog, I've wrote about howto use mod_jk2 to integrate httpd and tomcat. The article can be accesed [here][1] and [here][2].
Now, since mod_jk2 has not supported again by apache-tomcat-connector developers, so in this article I will use mod_jk. I'm using :


* httpd-2.2.4, can be downloaded [here][3]
* tomcat-5.2.23, can be downloaded [here][4]
* tomcat-connector, can be downloaded [here][5]

I prefer apache.the.net.id since this is the nearest mirror from Indonesia. O ya, Im using Kubuntu Feisty Fawn in my laptop.
First, we install the httpd-2.2.4 first. Unzip it, place it at some directory you like. In my environment, my user has full access to /opt directory, so I'm using it.
onty@phoenix:/opt$ gunzip httpd-2.2.4.tar.gz
onty@phoenix:/opt$ tar -xvf httpd-2.2.4.tar
onty@phoenix:/opt$ mv httpd-2.2.4 httpd-2.2.4-src
onty@phoenix:/opt$ cd httpd-2.2.4-src
Configure, put the result in /opt/httpd-2.2.4, enable shared object, enable cgi support. Enabling shared object makes us able to load dynamic shared object library. We're using mod_jk's shared object, so we need to enable apache to support dynamic shared object library. This also usefull if you want to enable your apache httpd server to serve PHP also. Same like this, you would also compile PHP as shared object, and then load it dynamically to apache httpd using LoadModule syntax in your httpd.conf .
onty@phoenix:/opt/httpd-2.2.4-src$ ./configure --prefix=/opt/httpd-2.2.4 --enable-so --enable-cgi
onty@phoenix:/opt/httpd-2.2.4-src$ make  onty@phoenix:/opt/httpd-2.2.4-src$ make install
Now, try to start it using root :
onty@phoenix:/opt/httpd-2.2.4-src$ cd /opt/httpd-2.2.4
onty@phoenix:/opt/httpd-2.2.4$ su -
root@phoenix:/opt/httpd-2.2.4# bin/apachectl start
If everything ok, you should be able to point your browser to http://localhost now, and see if you can read any "It works" there.
OK, now we continue to install the tomcat connector. Apache has provided us with the binary version of the connector. As mentioned in before, we should now already download it. I'm using mod_jk-1.2.21-apache-2.2.x-linux-i686.so. What we need to do is just load this shared object so that can be used by apache, that simple ? yes :D
Edit your httpd.conf, add this line :
Include conf/extra/mod_jk.conf
This is new style from apache that makes us easier to maintain our configuration file in modular basis.
Now create a new file in conf/extra/ name it mod_jk.conf.
\--------------------------------------------- mod_jk.conf -----------------------------------
JkWorkersFile /opt/httpd-2.2.4/conf/workers.properties
JkShmFile /var/log/httpd/mod_jk.shm
JkLogFile /opt/httpd-2.2.4/logs/mod_jk.log
JkLogLevel info
JkLogStampFormat "[%a %b %d %H:%M:%S %Y]"
JkMount /tomcat-docs/* router

JkMount jkstatus
Order deny,allow
Deny from all
Allow from 127.0.0.1

\-------------------------------------------------------
From the configuration file, we can see that :
We will place the log file in /opt/httpd-2.2.4/logs/mod_jk.log.
We will configure the connectors with a file named workers.properties located in /opt/httpd-2.2.4/conf .
We will have shared file that will be used by apache and tomcat, located in /var/log/httpd/mod_jk.shm. If the directory /var/log/httpd doesnt exist yet, we should create it first using root user.
The logger level will be INFO.
We will map /tomcat-docs/ request in httpd to be handled by tomcat, so make sure that this webapp exist in tomcat. By default if you download tomcat, this webapp is already exist. Later you can change it to your own webapp. And this request will be handled by a worker named 'router'.
Last one is for jkmanager monitoring tools. There will be new context path named /jkmanager/ that will show us status for our jk_module. This context path only allowed to be accessed from 127.0.0.1 (localhost).

Ok, now we need to create workers.properties in conf/ directory. See part 2 of this post.



[1]: http://www.jroller.com/page/JPrasojo/?anchor=setup_tomcat_clustering_and_load
[2]: http://www.jroller.com/page/JPrasojo/?anchor=setup_tomcat_clustering_and_load1
[3]: http://apache.the.net.id/httpd/httpd-2.2.4.tar.gz
[4]: http://apache.the.net.id/tomcat/tomcat-5/v5.5.23/bin/apache-tomcat-5.5.23.tar.gz
[5]: http://apache.the.net.id/tomcat/tomcat-connectors/jk/binaries/linux/jk-1.2.21/mod_jk-1.2.21-apache-2.2.x-linux-i686.so
