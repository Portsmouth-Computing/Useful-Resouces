### Stop restart at 30 mins of inactivity
#### Inorder to use this you must have sudo access as it is write protected  
Restart schedule is setup as to check if a users is inactive at which point shutdown as a VM  
This is setup a cron job that is used to check every 30 mins etc  
Easy fix is just to kill the process which is located at  
```
/etc/uop/uop-timeout
```
```
sudo nano /etc/uop/uop-timeout
```
will show
```
#!/bin/bash
#
#Bens script to shutdown vms if theyre idle

#Figure out if a user is logged in
loggedin=`w | wc -l`

#Clear the counter if its old
find /etc/uop -name uop-timeoutcounter -type f -mmin +90 -delete

#Set new counter file if it doesnt exist
if [ -f /etc/uop/uop-timeoutcounter ];
then
        echo "File exists and is active"
else
        echo "0" > /etc/uop/uop-timeoutcounter
        echo "File didn't exist and is now active"
fi

#Sets counter in action
counter=$(cat /etc/uop/uop-timeoutcounter)

#2 means there are no logged in users
if [ $loggedin = 2 ]; then
        let counter++
        echo $counter > /etc/uop/uop-timeoutcounter
else
        echo "0" > /etc/uop/uop-timeoutcounter
        counter=0
fi

#Final check to see if anyone has set a cancel file
servername=`hostname`
dothomecancel=`find /home/$servername/ -name .uop-cancel -print | wc -l`
homecancel=`find /home/$servername/ -name uop-cancel -print | wc -l`
if [ $dothomecancel -eq 1 -o $homecancel -eq 1 ];
then
        if [ -f /etc/uop/uop-cancel ];
        then
                echo "Both lecturer and student are cancelling each other"
        else
                echo "0" > /etc/uop/uop-timeoutcounter
                echo "No lecturer file present, cancelling shutdown"
        fi
else
        echo "Nothing to do!"
fi

#Shutdown machine if counter gets high
if [[ "$counter" -gt 5 ]]; then
       echo "0" > /etc/uop/uop-timeoutcounter
       /sbin/shutdown -h now
fi
```
At which point you can just comment out the ``` /sbin/shutdown -h now ``` to get it to not stop your VM