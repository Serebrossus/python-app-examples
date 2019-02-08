import requests
from bs4 import BeautifulSoup

url_path = input('Enter site url path with http(s): ')
if len(url_path) == 0:
    print('url path is empty')
else:
    #download page
    page = requests.get(url_path)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup.prettify())

