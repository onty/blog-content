Title: Glassfish for Tomcat and WebMethods
Date: 2007-12-1
Tags: 

These recent days I've been played around with Glassfish in my project. I have to build connectivity between our existing Card Management for Telco company product, created with pure jsp (yes, jsp treated as PHP, spaghetti or whatever you name it) to integrate with SAP. Our client provides WebMethods Integration server 6.5 as our only and only way to interact with the SAP. OK then, I grabbed some code from my previous project with Tomcat and WebMethods 6.1 and try to reuse them in this project. Well, it works. But this code only deals with connectivity. Tomcat contacts WebMethods, and that's it. All transaction maintained by WebMethods, no need to think about rollback, commit, or anything, we apply that on WebMethods's flow services. So simple and cool !. But this current project is different. Installed WebMethods dont have any license of JDBC Adapter, it only has SAP Adapter. So in order to save to database or whatever to our Card Management system, we have to build our own connectivity method. Previously we thought about creating Stored Procedure inside our database that later can be invoked by WebMethods's JDBC Adapter, but the client doesnt want to buy the license. Hmm....

Besides just store to database, our Card Management product also have to provide interfaces so that later on, it could synchronize any document with SAP. So SAP will hit our services if..let's say some PO created in SAP. In here, I _need to provide them with webservices_ to access all of our Card Management API in proper way.

On other side, our Card Management also must be able to synchronize any action triggered from our side. Ok, I can use my previous code just to call the WebMethods's service, but I can not predict how long will it take. WebMethods will continue our request to SAP, and then SAP done some process inside, and after that it will returns a value to us. Based on those values, we must done an action, and after we finished done those action in our side, we must push the result back to SAP, send our document number also. I cant imagine how long the users will be wait for these sequence action. They will bury us :D

I see that we can divide this process by synchronous and asynchronous action. There's some action that we need to retrieve the results back from SAP immediately, such as get price. I can't do anything for this action. Saving the price list in our Card Management will blow our mandays. And other process where the users dont care whether they get the result in real time or not. They can check back later to see what happen to their process. So, in here, I _need a messaging service_.

So, two needs, webservice and messaging. I was thought that I will install a several products for this. Spring webservice framework to make my life easier when creating webservices (their POJO style's are really cool and simple) and ActiveMQ to provide the messaging broker. All can be integrated within our tomcat instance. But,later I also have own more concern. I must not change too many configuration on currently running tomcat instance, since it runs stable right now. And also, user portal and backend integrations are 2 different thing. The users must not feel any __'world wide wait'__ thing when the backend process works hard to full fill their request. So here I decided to install one more instance of application servers for integration needs. And after some browsing, I decide to install Glassfish V2.

Why glassfish ? well, let's say, first I impressed with it's admin console. JBoss guys should really pay attention on this admin console. And secondly, I fall in love with it's support of WebServices. Glassfish support WebServices monitoring. Here I can monitor who called my webservices, on what time, what data sent, and what data returned. This is very useful when reconcile any lost datas. And the third part is, this Glassfish thing has a great messaging supports based on Sun's IMQ. I also browsed the net for this feature, and many guys out there recommends it. Last but not least, Glassfish V2 is JEE 5 compliance app.server (if not the RI itself). Creating WebServices, session EJB's and MDB's are easier with Annotations. Say good bye to deployment descriptor.

Ok, that's my review, maybe I'll write more about this later.