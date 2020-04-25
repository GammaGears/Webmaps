# import folium
# import pandas
#
# data = pandas.read_csv("Volcano.txt")
# lat = list(data["LAT"])
# lon = list(data["LON"])
# elev = list(data["ELEV"])
#
# html = """<h4>Volcano information:</h4>
# Height: %s m
# """
#
# map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
# fg = folium.FeatureGroup(name = "My Map")
#
# for lt, ln, el in zip(lat, lon, elev):
#     iframe = folium.IFrame(html=html % str(el), width=200, height=100 )
#     fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
#
#
# map.add_child(fg)
# map.save("Map_html_popup_simple.html")

# second popup
import folium
import pandas

data = pandas.read_csv("Volcano.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name = "My Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))

map.add_child(fg)
map.save("Map_html_popup_advanced.html")
