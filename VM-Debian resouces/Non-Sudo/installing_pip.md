### Getting Pip for Python without Sudo

If you do not have sudo you won't have access to the normal way which is

```
sudo apt-get install python3-pip
```

Instead you will have to do this manually.
If you want this all done for you please just download the gist [here](https://gist.github.com/Lagicrus/5dd000c3e072542f8a288660a044651a)
If not please follow the steps bellow

Solution 1, using both wget and python3

#Within linux console
```
me@server:~$ wget "https://bootstrap.pypa.io/get-pip.py" -O get_pip.py
```
#This will download the file and save it to the specified name
```
me@server:~$ python3 get_pip.py
```
Solution 2, using just python3
```Python
import urllib.request
url = "https://bootstrap.pypa.io/get-pip.py"
urllib.request.urlretrieve(url,"get-pip.py")
print("Saved file to {}".format(os.getcwd()+"/get-pip.py"))
subprocess.check_output(["python3.5","get-pip.py","--user"])
```
