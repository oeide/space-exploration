#from foliumLocal import *
import folium
from xyzservices import TileProvider
import utm_no_numpy as utm
import re

def drawPointOnly(pointsUTM):
    #my_map = folium.Map(location=shapelist[0].shape[0], zoom_start=8, tiles=None)
    my_map = folium.Map()
    folium.TileLayer("OpenStreetMap").add_to(my_map)
    #folium.TileLayer(tileprovider, show=False, name="Esri Worldimagery").add_to(my_map)
    folium.LayerControl().add_to(my_map)
    
    # create lat-long for the points to add
    coordLines= re.split("#", pointsUTM)
    for pointUTM in coordLines:
        coordsUTM= re.split(",", pointUTM)
        pointLatLong= utm.to_latlon(float(coordsUTM[0]), float(coordsUTM[1]), int(coordsUTM[2]), coordsUTM[3])
        placeName= coordsUTM[4]
    
        i=0
        folium.CircleMarker(
            location=pointLatLong,
            radius=10,
            color="cornflowerblue",
            stroke=True,
            fill=True,
            fill_opacity=0.6,
            opacity=1,
            popup=placeName,
            tooltip=placeName,
            label=placeName
        ).add_to(my_map)

    print("Before show my map")
    map_path= my_map.show_in_browser()
    del my_map
    print("After show my map "+map_path)
    return map_path

points= "355316,6940513,33,S,Rutten Field#339346.29,6950319.97,33,S,bræcke gaard#314217.93,6943363.98,33,S,Røraas#310910.73,6973645.07,33,S,hof annex eller aalens annex#304353.24,6983241.91,33,S,holtaalens hoved Kircke#279377.2,6986568.3,33,S,Singsaas annex#261922.42,6997816.47,33,S,Størens hoved Kircke#260918.39,7009706.51,33,S,Horrigs annex#263937.88,7024750.04,33,S,Meehl-hus hovet Kircke#265139.91,7030363.44,33,S,Solberg i Liinstrandens Annex#270337.87,7041814.2,33,S,Trondhiem"
drawPointOnly(points)
