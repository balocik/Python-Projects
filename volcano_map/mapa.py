#---------------------------
#      22/10/2017
# created by Wojciech Kuczer 
#---------------------------
import pandas
import folium

def colour_elevation(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

data = pandas.read_csv("volcanos.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
volcano_name = list(data["NAME"])
elevation = list(data["ELEV"])


map = folium.Map(location=(52.204717, 0.457957), zoom_start=6, tiles="Mapbox Bright")
fgv = folium.FeatureGroup(name="Wulkany")
for lt, ln, name, el in zip(lat, lon, volcano_name, elevation):
    fgv.add_child(folium.Marker(location=(lt, ln), popup=folium.Popup(name, parse_html=True), icon=folium.Icon(color=colour_elevation(el))))
fgp = folium.FeatureGroup(name="Populacja")
fgp.add_child(folium.GeoJson(data=(open("world.json", "r", encoding="utf-8-sig").read()),
                                  style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Moja_Mapa.html")
