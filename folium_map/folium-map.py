import folium
import pandas as pd

#Load data
data = pd.read_csv("Vulcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

#create base map
map = folium.Map(location=[37.296933-121.9574983], zoom_start=5, title='Mapbox bright')

#Plot markers
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.Marker(location=[lat, lon], popup=str(elevation) + ' m', icon=folium.Icon(color='gray')).add_to(map)

#save map
map.save("map1.html")
