import time
from datetime import datetime as dt

#path to the host file
#In Windows - C:\Windows\System32\drivers\etc\hosts
#In Unix - etc/hosts
host_path = '/etc/hosts'

#Redirect to localhost
redirect = '127.0.0.1'

#Websites to block
website_list = ["www.netflix.com", "www.facebook.com"]

#condition
while True:
    #Check for the current time
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now():
        print("Work time")
    else:
        print("I am God")

    time.sleep(5)