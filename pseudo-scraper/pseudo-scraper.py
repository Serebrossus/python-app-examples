import requests
from bs4 import BeautifulSoup


url_path = input('Enter site url path with http(s): ')
# For example, I use the information from the site
# "https://www.fifa.com/worldcup/players/player/201200/profile.html"
# This program is written for informational purposes.
# The task is to learn how to use the capabilities of python for writing different applications.

if len(url_path) == 0:
    print('url path is empty')
else:
    # download page
    page = requests.get(url_path)
    soup = BeautifulSoup(page.content, "html.parser")

    name = soup.find("div", {"class": "fi-p__name"}).text.replace("\n", "").strip()
    country = soup.find("div", {"class": "fi-p__country"}).text.replace("\n", "").strip()
    role = soup.find("div", {"class": "fi-p__role"}).text.replace("\n", "").strip()
    print(name, "\n", country, "\n", role, "\n")
