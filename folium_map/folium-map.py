import folium
from folium.plugins import MarkerCluster
import pandas as pd

#Load data
data = pd.read_csv("Vulcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

#function to change color
def color_change(elevation):
    if(elevation < 1000):
        return ('green')
    elif(1000 <= elevation < 3000):
        return ('orange')
    else:
        return ('red')

#create base map
map = folium.Map(location=[37.296933-121.9574983], zoom_start=5, title='Mapbox bright')

#create cluster
marker_cluster = MarkerCluster().add_to(map)
#Plot markers
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.CircleMarker(location=[lat, lon], radius=9, popup=str(elevation) + ' m', fill_color=color_change(elevation),
                  icon=folium.Icon(color='grey', fill_opacity=0.9)).add_to(marker_cluster)

#save map
map.save("map1.html")
