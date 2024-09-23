#from foliumLocal import *
import folium
from xyzservices import TileProvider

tileprovider = TileProvider(
    name="Esri Worldimagery",
    url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attribution="Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, "
                "IGP, UPR-EGP, and the GIS User Community", )


def draw(shapelist, schnittflaeche, colorIn):
    """
    Draws polygon on map (leaflet), shows result in browser
    :param shapelist: List of Polygons to be drawn in WGS84 Decimal
    :param schnittflaeche: Polygon of intersection area
    """
    print("Length shapelist: "+str(len(shapelist)))
    my_map = folium.Map(location=shapelist[0].shape[0], zoom_start=8, tiles=None)
    folium.TileLayer("OpenStreetMap").add_to(my_map)
    folium.TileLayer(tileprovider, show=False, name="Esri Worldimagery").add_to(my_map)
    folium.LayerControl().add_to(my_map)
    i=0
    for y in shapelist:
        i= i+1
        locations = y.shape
        if i<10:
            color="#"+str(i)+str(i)+"0000"
        else:
            color="#"+str(i)+"0000"
        print("Color: "+color)
        folium.Polygon(
            locations=locations,
            fill_opacity=0.15,
            fill=True,
            color=color
        ).add_to(my_map)
    folium.Polygon(
        locations=schnittflaeche,
        color="#ff0000",
        fill_opacity=0.15,
        fill=True,
    ).add_to(my_map)
    print("Before show my map")
    map_path= my_map.show_in_browser()
    del my_map
    print("After show my map: "+map_path)
    return map_path

def drawNoOverlap(shapelist, colorIn):
    """
    Draws polygon on map (leaflet), shows result in browser
    :param shapelist: List of Polygons to be drawn in WGS84 Decimal
    """
    print("Length shapelist: "+str(len(shapelist)))
    my_map = folium.Map(location=shapelist[0].shape[0], zoom_start=8, tiles=None)
    folium.TileLayer("OpenStreetMap").add_to(my_map)
    folium.TileLayer(tileprovider, show=False, name="Esri Worldimagery").add_to(my_map)
    folium.LayerControl().add_to(my_map)
    i=0
    for y in shapelist:
        i= i+1
        locations = y.shape
        if i<10:
            color="#"+str(i)+str(i)+"0000"
        else:
            color="#"+str(i)+"0000"
        folium.Polygon(
            locations=locations,
            fill_opacity=0.15,
            fill=True,
            color=color
        ).add_to(my_map)
    print("Before show my map")
    map_path= my_map.show_in_browser()
    del my_map
    print("After show my map"+map_path)
    return map_path
"""
    save = input("Do you want to save your Result? (y)es/(n)o: ")
    if "y" in save.lower():
        my_map.save("result.html")
"""
