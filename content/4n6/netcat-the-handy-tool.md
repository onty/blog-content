Title: Netcat the handy tool
Date: 2018-04-03
Tags: 4n6 Unix Linux netcat Server Forensic
Category: 4n6

Netcat/nc is a command line based tool known as the swiss-army knife utility for networking. It can do lots of things when it comes to networking matters. In Forensic field, netcat or commonly known as nc is mostly used to open up a port as an I/O destination mostly to perform a remote forensic task. See the following simple example :

Run this on server :
```

```

Run this on client :
```

```

The example above will redirect whatever command output from the client into the server.

nc can also be used to execute a reverse shell command. A listener on the server side can be open to receive any incoming remote-shell connection from the client. The possibilities of what can be done using a reverse shell tunnel is just unimaginable. It's like you have a shell account where the world has access to your machine.

Now, obviously security and integrity concern are valid here. At least the following case :

1. Sending forensic data in plaintext can be a very thick pixie dust when it comes to criminal case. Here's how to send the data over the ssl channel. I remember one of my lecturer in UCD told me this, he was one of the ex-Scotland Yard forensic investigator. Pixie dust is where the other side is trying to undermine the proposed evidence by questioning it's integrity. Anything that doesn't sound very well can be questionable and be put into pixie dust.

2. There's also another important concept called the fruit of a poisonous tree. If the remote system's binary has already been compromised, then executing nc using the 'poisoned' binary might raises a concern too.
