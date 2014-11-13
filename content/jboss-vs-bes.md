Title: JBoss Vs BES
Date: 2007-6-3
Tags: 
Category: Java

Finally, I know why I got this error :
javax.naming.NameNotFoundException: OracleDS not bound ...

Padahal di browse di Jboss console ada loh OracleDS. Udah kucoba ngeganti dengan java:OracleDS, java:/OracleDS, java:comp/env/OracleDS, semua nggak bisa....

Ternyata ada konfigurasi yg harus ditambahin di oracle-ds.xml, selama ini kalo lookup langsung OracleDS tuh, dia akan nyari di JVM yang sama. Pantesan, lha aku jalaninnya dengan debug di eclipse, jelas beda JVM ama JBoss nya. Setelah browsing, akhirnya nemu link yang bilang, bahwa ada konfigurasi yang harus ditambahin di oracle-ds.xml nya, yaitu ini :
false

Dengan begini, dia akan lookup JNDI name ke localhost:1099 dan dapet deh OracleDS. Happy ending deh...

Sekarang latihan bikin MDB di JBoss setelah sebelum nya sukses di BES. BES ? apa itu ? Borland Enterprise Server, J2EE nya Borland. Entah kenapa jatis partneran ma ni produk, kukira produk mereka hanya borland Delphi ama JBuilder, hehehe.

Sekilas tentang BES 6.5, nggak ada yg amazing yah, standar2 aja, masih J2EE 1.3 compliant. Ngga bisa dibandingin ama webmethods Integration Server karena emang beda. BES lebih ke J2EE App.Server, sedangkan webMethods lebih ke Middleware, EAI Broker. Tapi fitur yg menarik di JBoss (dan satu-satunya yg menarik buatku) adalah SonicMQ nya. Sebanding dengan webMethods Broker.

Semangat !!!


originally posted 7/4/06
