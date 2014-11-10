Title: ESB #1 (Revised)
Date: 2007-6-3
Tags: 

Baru dapet chm tentang ESB(Enterprise Service Bus), karangan Dave Chappel dari [mas Ari][1]. Nih ulasan bab pertamanya :


Bab pertama ngejelasin tentang apa itu ESB(Enterprise Service Bus). Tahun-tahun sebelumnya kita mengenal istilah Service Oriented Architecture (SOA), Enterprise Application Integration (EAI), Business-to-Business (B2B), dan web services. Semua teknologi ini intinya sama, yaitu improvisasi hasil bisnis dari integrasi sistem-sistem yang telah ada sebelumnya. Sedangkan konsep ESB lebih kepada "..loosely coupled, highly distributed integration network that can scale beyond the limits of a hub-and-spoke EAI broker" . Jadi ketika bicara tentang ESB, maka didalamnya akan meliputi :

1\. Messaging

2\. Web Services

3\. Transformasi data

4\. Intelligent Routing yang mampu meneruskan message dari node satu ke yang lain tanpa melalui mekanisme broadcast.



Lebih lanjut dijelaskan dalam halaman berikutnya, tentang konsep-konsep apa saja yang telah diakomodir oleh generasi integrasi sebelumnya (SOA, EAI, B2B) sebagai berikut :


1.It must adapt to suit the needs of general-purpose integration projects across a variety of integration situations, large and small. Adaptability includes providing a durable architecture that is capable of withstanding evolutions in protocols, interface technology, and even process modeling trends.


2.It must link together applications that span the extended enterprise using a single unified approach and a common infrastructure.


3.It must extend beyond the boundaries of a single corporate IT data center and into automating partner relationships such as B2B and supply-chain scenarios.


4.It must have simplicity of design and low barriers to entry, enabling the everyday IT professional to become a self-empowered integration architect.


5.It must provide an SOA across the pervasive integration that enables integration architects to have a broad, abstract view of corporate application assets and automated business processes.


6.It needs the flexibility and ability to react to and meet the needs of changing business requirements and competitive pressures.


Gambar berikut menunjukkan lebih jelas tentang posisi ESB dan teknologi integrasi pendahulunya.

![][2]



1\. Traditional EAI Brokers.
Arsitektur EAI Broker seperti ini memiliki keunggulan dimana semua fungsi-fungsi yang disediakannya (termasuk manajemen routing dan bisnis rule) dapat diatur secara terpusat. Tetapi buku ini mengatakan bahwa arsitektur ini kurang cocok untuk level integrasi antar departemen atau unit bisnis yang berbeda. Lebih lanjut dijelaskan dalam bab 2 mengenai ini.

2\. Application Server.
Application server dapat menghubungkan protokol-protokol yang berbeda dengan baik, namun hasilnya adalah sebuah aplikasi yang saling bergantung satu sama lain, yaitu antara integration logic dan application logic.


3\. Message Oriented Middleware.
Menyediakan konektivitas yang baik, loosely coupled, dengan gaya asinkron, antar aplikasi. Hal ini memungkinkan beberapa aplikasi yang kecepatan responsenya berbeda, menjadi tidak saling menunggu satu sama lain. Namun, arsitektur MOM ini membutuhkan pemrograman low-level yang cukup lumayan, sehingga bisa jadi waktu development akan lama. Belum lagi masalah perbedaan fisik network yang menyebabkan beberapa infrastruktur MOM tertentu menjadi tidak bisa diandalkan.


4\. Yang terakhir, ESB.
Disini, kita tidak lagi bicara tentang pemrograman, tetapi lebih ke arah bagaimana sebuah service di konfigurasi. Di ESB juga terdapat pemisahan arsitektur yang jelas antara business logic(proses bisnis aplikasi) dengan integration logic(routing dan transformasi format data).



![][3]

**Traditional Integration Broker Architecture**




![][4]

**ESB Architecture**



Berikut karakteristik dari ESB :

**Pervasiveness. **


An ESB can be adapted to suit the needs of general-purpose integration projects across a variety of integration situations. It is capable of building out integration projects that can span an entire organization and its business partners.


**Highly distributed, event-driven SOA. **


Loosely coupled integration components can be deployed on the bus across widely distributed geographic deployment topologies, yet are accessible as shared services from anywhere on the bus.


**Selective deployment of integration components. **


Adapters, distributed data transformation services, and content-based routing services can be selectively deployed when and where they are needed, and can be independently scaled.


**
Security and reliability. **


All components that communicate through the bus can take advantage of reliable messaging, transactional integrity, and secure authenticated communications.


**
Orchestration and process flow. **


An ESB allows data to flow across any applications and services that are plugged into the bus, whether local or remote.


**
Autonomous yet federated managed environment. **


An ESB supports local autonomy at a departmental and business unit level, and is still able to integrate in a larger managed integration environment.


**
Incremental adoption. An ESB can be used for small projects. **


Each individual project can build into a much larger integration network, which can be remotely managed from anywhere on the bus.


**
XML support. **


An ESB can take advantage of XML as its "native" datatype.

originally posted 7/4/06

[1]: http://arih.wordpress.com
[2]: http://jroller.com/resources/j/JPrasojo/Clipboard01.jpg
[3]: http://jroller.com/resources/j/JPrasojo/Clipboard02.jpg
[4]: http://jroller.com/resources/j/JPrasojo/Clipboard03.jpg
