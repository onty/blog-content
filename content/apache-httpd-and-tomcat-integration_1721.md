Title: Apache Httpd and Tomcat integration using mod_jk, part 2
Date: 2007-6-3
Tags: 
Category: Unix/Linux

This posting splitted because somehow blogspot just cut it. I don't know why but when I previewed the posting, blogspot just cut the postings, so I splitted it into 2 parts.

Ok, now we create workers.properties file.
```
onty@phoenix:/opt/httpd-2.2.4$ vi conf/workers.properties
\------------------------------------------------------------------------------------
worker.list=router,jkstatus
# Define a worker using ajp13
worker.worker1.port=8009
worker.worker1.host=localhost
worker.worker1.type=ajp13
worker.worker1.lbfactor=1
# Define prefered failover node for worker1
worker.worker1.redirect=worker2
# Define another worker using ajp13
worker.worker2.port=8009
worker.worker2.host=localhost
worker.worker2.type=ajp13
worker.worker2.lbfactor=1

# Define the LB worker
worker.router.type=lb
worker.router.balance_workers=worker1,worker2
# Define the status worker
worker.jkstatus.type=status

\------------------------------------------------------------------------------------
```
This file defines all our workers. Our 'router' worker will be a load balancer worker for other workers, including worker1 and worker2.

Now, we install (unzip, exactly) our apache. We use apache-5.2.23. We will modify the directory structure little bit, as shown like this.

![][1]
Give attention to tomcat1 and tomcat2 directory, and also directories inside it.We will use 2 instance of tomcat1 and tomcat2 as worker 'worker1' and 'worker2'. We also need to configure each server.xml in tomcat1 and tomcat2 so that they're not using the same port.
```
Tomcat1 :
Server port="8005" shutdown="SHUTDOWN"
..
..
Connector port="8009"
enableLookups="false" redirectPort="8443" protocol="AJP/1.3"
..
..

Connector port="8080" maxHttpHeaderSize="8192"
maxThreads="150" minSpareThreads="25" maxSpareThreads="75"
enableLookups="false" redirectPort="8443" acceptCount="100"
connectionTimeout="20000" disableUploadTimeout="true"

Tomcat2 :
Server port="9005" shutdown="SHUTDOWN"
..
..
Connector port="9009"
enableLookups="false" redirectPort="8443" protocol="AJP/1.3"
..
..

Connector port="8080" maxHttpHeaderSize="8192"
maxThreads="150" minSpareThreads="25" maxSpareThreads="75"
enableLookups="false" redirectPort="8443" acceptCount="100"
connectionTimeout="20000" disableUploadTimeout="true"
```

One more thing, we need to create startup and shutdown file for each tomcat instance. We call it start1.sh, start2.sh, stop1.sh, stop2.sh
```
start1.sh
#!/bin/bash
export CATALINA_BASE=/opt/apache-tomcat-5.5.23-cluster/tomcat1
export JAVA_HOME=/opt/jdk1.6.0
./startup.sh
start2.sh
#!/bin/bash
export CATALINA_BASE=/opt/apache-tomcat-5.5.23-cluster/tomcat2
export JAVA_HOME=/opt/jdk1.6.0
./startup.sh
stop1.sh
#!/bin/bash
export CATALINA_BASE=/opt/apache-tomcat-5.5.23-cluster/tomcat1
export JAVA_HOME=/opt/jdk1.6.0
./shutdown.sh
stop2.sh
#!/bin/bash
export CATALINA_BASE=/opt/apache-tomcat-5.5.23-cluster/tomcat2
export JAVA_HOME=/opt/jdk1.6.0
./shutdown.sh

```
Basically, these file just aimed to setup environment variable named CATALINA_BASE to point which tomcat instance we want to start/stop.

Now, lets try our installation. Start both tomcat instance, and also start your httpd server. Point out the browser to http://localhost/tomcat-docs/ and see if the request handled correctly. Httpd will redirect the request so that can be served by tomcat. Also point the browser to http://localhost/jkmanager/. This context path shows us the Load Balancing status for our tomcat instance.

Feel free to drop any comments about this posting.
Thanks, good luck trying !



[1]: http://bp0.blogger.com/_02IFrF9Xz98/RmKTVamjjKI/AAAAAAAABkI/CptR2eLPrpA/s320/opt-structure.png
