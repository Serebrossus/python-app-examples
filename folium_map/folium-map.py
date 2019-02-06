import folium

#create base map
map = folium.Map(location=[37.296933-121.9574983], zoom_start=8, title='Mapbox bright')

#Add marker
folium.Marker(location=[37.4074687-122.086669], popup='Google HQ', icon=folium.Icon(color='gray')).add_to(map)

#save map
map.save("map1.html")
