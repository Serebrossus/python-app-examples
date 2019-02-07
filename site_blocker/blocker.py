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
        #open file and read content
        file = open(host_path, "r+")
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                #write IP of localhost and name of website to block
                file.write(redirect + " " + website + "\n")

    else:
        print("I am God")

    time.sleep(5)