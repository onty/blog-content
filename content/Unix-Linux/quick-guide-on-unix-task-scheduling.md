Title: Quick guide on UNIX task scheduling with at and batch command
Date: 2009-5-18
Tags: Tips Unix Linux stuff
Category: Unix/Linux

While task scheduling in UNIX commonly uses Crontab facilities, UNIX based system (actually, Windows provide it too, at.exe) also provide at command. Both related to the same area, task scheduling. While Crontab aims to schedule a recurring command (every minutes, every month, every week, etc), at command aims to schedule a task that run once, with specific time arguments. Here’s one example of how we can schedule a task with at command:


```
$ at now 1 hour &1 > outfile | mailx mygroup
!
commands will be executed using /bin/tcsh
job 1242637613.s at Mon May 18 16:06:53 2009

```


As we can see from the example above, we want to schedule a task to be executed 1 hour from now, and the task to be executed is diff file1 file2 2>&1 > outfile | mailx mygroup. The at command then returns the job id, which we will able to list all the queueing at command using atq or at –l below:



```
$ atq
Rank Execution Date Owner Job Queue Job Name
1st May 18, 2009 17:06 minsat 1242637774.a a stdin

$ at -l
1242637774.a Mon May 18 16:18:45 2009

```


From above we can see that there are only 1 jobs queuing at queue named ‘a’ (this is special queue name for at, and it is used to distinguish between the job executed by at and batch command). We can also see that the execution time will be May 18, 2009 17:06.



And to cancel the scheduled at command, we use atrm or at –r command as follows:

```
$ atrm 1242637774.a
1242637774.a: removed

$ at -r 1242637774.a
1242637774.a: removed

```


There are lots of other parameter we can use for describing the time parameter and how to execute the at command which is I found it quite ‘human readable’. Here’s some list of other possible parameter we can use:



1\. Direct time
```
$ at 01.30
$ at 0815am Jan 24
$ at 5 pm FRIday
```

2\. Now keyword
```
$ at now 1 minutes
$ at now 1 hours
$ at now " 1day"
```

3\. Tomorrow keyword
```
$ at 0830 tomorrow
```

4\. Noon keyword
```
$ at noon tomorrow
```

5\. Midnight keyword
```
$ at midnight tomorrow
```

6\. Week keyword
```
$ at 2pm next week
```

7\. Piped with other command
```
$ echo "mail -s 'REMINDER: Task Scheduler samples' lintang.jp@gmail.com" | at '5/18/2009 10:00AM'
```

8\. Putting the job inside a file
```
$ at –f runScript.sh now 1 hour
```

9\. Sending an email after the job is completed
```
$ at –m –f runScript.sh now 1 hour
```

10\. Using another shell instead of the user’s default shell for execution
```
$ at –c –f runScript.sh now 1 week // C Shell
$ at –k –f runScript.sh now 1 week // Korn Shell
$ at –s –f runScript.sh now 1 week // Bourne Shell

```
Several behaviors and conditions that must be known when running at command as follows:



1\. All environment variables, current working directory, file creation mask, and system resource limits during at utility execution will be retained and used when the at job is executed. So it’s different with Crontab where we have to set our environment variables manually to be called inside our script execution.
2\. The default shell environment to be used during execution is the user’s default shell, listed in /etc/passwd.
3\. Any users that is allowed or forbidden to use at command are listed in the following file :



1\. /usr/lib/cron/at.deny // denied user
2\. /usr/lib/cron/at.allow // allowed user



If the file does not exist, for example: at.allow file does not exist, means that all users are allowed to use at command.

While batch command is similar with at -q b -m now commands. Meaning that the batch command will use different queue with at (special queue named ‘b’), and by default it will send a report via email. It will also execute right away. If the queue is full, then the command will have to wait to be executed one by one.



Resource : 1. Unix at man pages, with some slang modifications :p

Fiuh, alhamdulillah, that was hard to wrote :D
