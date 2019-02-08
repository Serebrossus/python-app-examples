import requests
from bs4 import BeautifulSoup

url_path = input('Enter site url path with http(s): ')
if len(url_path) == 0:
    print('url path is empty')
else:
    #download page
    page = requests.get(url_path)
    soup = BeautifulSoup(page.content, "html.parser")

    name = soup.find("div", {"class": "fi-p__name"}).text.replace("\n", "").strip()
    country = soup.find("div", {"class": "fi-p__country"}).text.replace("\n", "").strip()
    role = soup.find("div", {"class": "fi-p__role"}).text.replace("\n", "").strip()
    print(name, "\n", country, "\n", role, "\n")

