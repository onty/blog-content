Title: Webservices with spring
Date: 2007-4-19
Tags: 
Category: Java

These few days, I had a task to create a webservice client. Sounds interesting and challenging, because usually if we depends on weblogic's control, we can make any webservices client much much easier, just a few click, and tadaaa. The problem is, the webservice client will become stand alone module, so, I can't use any java controls since those controls will be managed by weblogic container during runtime.
Then I turn to find another simple and fast way to create webservice client. But, before that of course, since the remote system is not ready yet, I have to create some dummy web service first. Weblogic 9.2 having strange behaviour. First, we create webservice project from the Eclipse-based-IDE. After that, we generate the wsdl files. But, dont ever try to validate it :D because it will fail. Just pass and use those webservice to create weblogic client. That's strange, fail to validate, but it works :D

Ok, dont waste time, since I already had the webservice simulator works no matter how :p I began to create the webservice client. Coding from scratch ? no, it's painful, and I need to do it fast. I turn out to spring and axis which offers it's integration. This is my bean config sample :
```
org.apache.axis.client.ServiceFactory


http://localhost:7001/AggregatedInfoFeederSimulator/AggregatedInfo?WSDL


http://com/ericsson/aggregateinfo/sub/services


AggregatedInfoService


AggregatedInfoSoapPort


com.ericsson.mi3g.sub.aggregatedinfo.wsclient.RemoteInfoPortIntf


com.ericsson.mi3g.sub.aggregatedinfo.wsclient.RemoteInfoServiceIntf

```


I'm using AggregatedInfoJaxRpcProxyFactoryBean, this is a class that extends JaxRpcPortProxyFactoryBean. We need to extend it to override the postProcessJaxRpcService(Service service) method that will be used to register which deserializer would be used to object that I pull from webservice. First time I try to run, the method is not being called at all, I'm curious. But after googling, I found out that we need to import the right class for the arguments. It should be javax.xml.rpc.encoding.Service;

Ok, the webservice client is done, now it's time to develop the database persistence part. I'm using Ibatis. Ibatis is cool, and I prefer this to hibernate if we need to do the complex query. In telco apps, there are no such simple query, right ? also, we need to be ready if someday the query changed, new field added, depends on requirement.

The database persistence done. Now, create the ant script to run this module, since I had lots of CLASSPATH to include. I can't put it all in bash script and change all the path when it's moved out to production. 


And that's it, I'm done.



logger.info("from cyberjava with love....");
