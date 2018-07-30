### Blocking hosts

There were some users attempting to SSH into his vm originating from China/Russia/Vietnam. I have seen around 350~ IPs myself.

If you have sudo and you wish to block these and all other IPs that are coming towards your machine.

First,
```
git clone https://github.com/Portsmouth-Computing/SSH-Blocking-and-Scanning.git
```
This will download the reposity for the file from GitHub.

Then,
```
sudo crontab -e
```
This will open up a text editor which you will enter the following line into to edit the cron job.

Afterwards,
```bash
15,30,45,0 * * * * /usr/bin/python3.5 /home/upID/SSH-Blocking-and-Scanning/cron_main.py
```
This will create a cron job that will run at minutes "15,30,45,0" aka every 15 minutes. 
Then it will use python3.5 to run that specific file.
Make sure to change "upID" to your username within the VM aka the one that you use to login as that is where the file is stored.

If you want to do every hour just do "0". If you want to mess around with it more have a look at this [link](https://crontab.guru/)

### In case of errors

If your cron job is having a issue / you want to have updates in case of issues
```bash
MAILTO=email
15,30,45,0 * * * * /usr/bin/python3.5 /home/up857256/SSH-Blocking-and-Scanning/cron_main.py
```
Change email to a email address such as email@myemail@co.uk and it will email you in case of errors.

### When done

If you want to check that it is running on your machine.

If you are going to be waiting for it to run,
```
sudo tail -f /var/log/auth.log | egrep "cron"
```
This will show all the activety that is happening on your machine that is related to cron. Wait until the time that it should occur and you should see some activety from cron such as this
```
Dec 25 12:00:01 myUsername CRON[1]: pam_unix(cron:session): session opened for user root by (uid=0)
Dec 25 12:00:02 myUsername sudo:     root : TTY=unknown ; PWD=/root ; USER=root ; COMMAND=/usr/sbin/service sshd restart
Dec 25 12:00:02 myUsername sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Dec 25 12:00:02 myUsername sshd[2]: Received signal 15; terminating.
Dec 25 12:00:03 myUsername sshd[3]: Server listening on 0.0.0.0 port 22.
Dec 25 12:00:03 myUsername sshd[3]: Server listening on :: port 22.
Dec 25 12:00:03 myUsername sudo: pam_unix(sudo:session): session closed for user root
Dec 25 12:00:03 myUsername CRON[1]: pam_unix(cron:session): session closed for user root
```

Or if it has already run and you don't feel like waiting.
```
sudo less /var/log/auth.log
```
You can then scroll through the entire log using the arrow keys and Page Up/Down
If you want to jump to the end press Shift+G.
Then look through the logs and try to find when your cron job happened and you should see something like this,
```
Dec 25 12:00:01 myUsername CRON[1]: pam_unix(cron:session): session opened for user root by (uid=0)
Dec 25 12:00:02 myUsername sudo:     root : TTY=unknown ; PWD=/root ; USER=root ; COMMAND=/usr/sbin/service sshd restart
Dec 25 12:00:02 myUsername sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Dec 25 12:00:02 myUsername sshd[2]: Received signal 15; terminating.
Dec 25 12:00:03 myUsername sshd[3]: Server listening on 0.0.0.0 port 22.
Dec 25 12:00:03 myUsername sshd[3]: Server listening on :: port 22.
Dec 25 12:00:03 myUsername sudo: pam_unix(sudo:session): session closed for user root
Dec 25 12:00:03 myUsername CRON[1]: pam_unix(cron:session): session closed for user root
```
