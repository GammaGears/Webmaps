import folium
import pandas
data=pandas.read_csv("volcano.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
# def color_producer(elevation):
#     if elevation<1000:
#         return "green"
#     elif 1000 <= elevation <3000:
#         return "orange"
#     else:
#         return "red"
map = folium.Map(location=[38.0,-99.88],zoom_start=10,tiles="Stamen Terrain")
fg=folium.FeatureGroup(name="mymap")
for lt,ln,el in zip(lat,lon,elev):
    # fg.add_child(folium.Marker(location=[lt,ln], popup=str(el),icon=folium.Icon(color=color_producer(el))))
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(el),icon=folium.Icon(color='green')))
# fg.add_child(folium.Marker(location=[11.243535,76.656788], popup="Hai i am marker",icon=folium.Icon(color='red')))
map.add_child(fg)
map.save("Map1.html")
