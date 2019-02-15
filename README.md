# python-app-examples
Application examples on python. Made to consolidate your knowledge

## Interactive Dictionary
An interactive dictionary will return the values of the word that the user entered.
If the user has made a typo, the program will suggest the most suitable word. In this case, the program will ask - "perhaps you meant?".
If the word has more than one meaning, then the program should return them all.

## Folium Map
Create a map using python and folium. Folium is a library for visualizing geodata or other data that uses location and coordinates.
To install folium we need a pip.
To install pip we need to execute commands in the terminal (console).
I use OpenSuse Leap.
```
#OpenSuse
sudo zypper install python3-pip

#Ubuntu
sudo apt install python3-pip

pip install folium
```

## Site blocker
An example of a simple site blocker.
During business hours, the program should block access to the specified sites.
At the end of the working time unlock access to the sites blocked by this program.

## Flask Web site
An example of creating a site on python and Flask.
Flask - microframework for web development.

## pseudo-scrapper
Sample application for web scraping. It may be necessary when there is a need to scan a web page and extract data.
Written for informational purposes.
For work we need a library BeautifukSoup.
```
pip install beautifulsoup4
```

## Parser
An example of parsing a file. The data in the file corresponds to the user class.

### Add .idea to git ignore
* open cmd or terminal
* go to project directory
* enter commands
```
echo '.idea' >> .gitignore
git rm  -r --cached .idea
git add .gitignore
git commit -m 'enter your message'
git push
```
