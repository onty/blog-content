Title: Ruby Install on DSL Linux
Date: 2007-11-13
Tags: Ruby DSL Linux stuff
Category: Unix/Linux

Went home earlier than before today, after a day full of meeting with client. I missed my linux. Got a bling about ruby. This stuff sounds cool. Lot's of java programmer migrating to this language, let's give it a shot. I started my adventure by googling with some 'beginner standars' keyword regarding ruby : "howto install ruby", and I got these links :
\- http://www.ruby-lang.org/id
\- http://hivelogic.com/narrative/articles/ruby_rails_lighttpd_mysql_tiger?status=301
Great, I boot up my DSL linux under qemu, and start downloading the necessary package. I tried to install using DSL's extension facilities (MyDSL-ruby.dsl) but, I don't know if it's work. So I decided to download the source, and compile it, just like the good old days :)
First, I downloaded ruby [here][1]. And then as usual, run 3 commands :
dsl@1[ruby-1.8.6]$ ./configure --prefix=/opt/ruby-1.8.6
dsl@1[ruby-1.8.6]$ make
dsl@1[ruby-1.8.6]$ sudo make install
And, I got my ruby installed in /opt/ruby-1.8.6. Dont forget to add the path reference to ruby's bin/ directory installation as follows (mine at /opt/ruby-1.8.6/bin) :
export PATH=/opt/ruby-1.8.6/bin:$PATH
To make my life easier, I put that line in /etc/profile, and run : source /etc/profile. Check whether it points to the right path, type : irb, it should shows you some prompt like this :
dsl@0[Installer]$ irb
irb(main):001:0>

Ok, I continued my journey by getting a tools called RubyGems. This RubyGems is a handy command-line tool for managing the installation of Ruby packages, like Rails ('quoted from [here][2] ').
I downloaded it from [here][3].
After that, I unpack it, and went inside the exploded directory and type : ruby setup.rb
This will start the installation process of RubyGems.

OK, next I installed Rails, what is it ?.
Quoted from http://rubyonrails.org/, ruby itself is a programming language, and Rails is the framework, just like Struts in Java. Rails is a full-stack framework for developing database-backed web applications according to the Model-View-Control pattern.

After RubyGems installed, it's all easy to install Rails, I just have to type :
sudo gem install rails --include-dependencies
And RubyGems will download all the needs.

While RubyGems downloading my Rails installation, I went to next step and install PCRE and Lighttpd. PCRE is a Ruby regex extensions stands for Perl Compatible Regular Expression. I downloaded it from [here][4]. While Lighttpd is a webserver that became the default one when we choose Rails. I downloaded Lighttpd from [here][5].
First, PCRE. I run : ./configure, make, and make install. I done the same command with Lighttpd, only that I gave different prefix on each ./configure like this :
PCRE : ./configure --prefix=/opt/pcre-7.4
Lighttpd : ./configure --prefix=/opt/Lighttpd-1.4.18
And the rest make and make install commands were same.

Ok, I should be ready for rock and roll with ruby on rails.
I'll write my next experiments later. Now, it's time to get rest, we'll have a great patch deployment tomorrow :)

[1]: ftp://ftp.ruby-lang.org/pub/ruby/stable-snapshot.tar.gz
[2]: http://hivelogic.com/narrative/articles/ruby_rails_lighttpd_mysql_tiger?status=301
[3]: http://rubyforge.org/frs/?group_id=126
[4]: ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-7.4.tar.gz
[5]: http://www.lighttpd.net/download/lighttpd-1.4.18.tar.bz2
