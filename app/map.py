import folium
from app.tools import convert_adress_to_coordinates


def create_bars_map(current_location, bars_list, path='app/templates/_map.html'):
    current_coordinates = convert_adress_to_coordinates(current_location)

    map = folium.Map(
        location=current_coordinates,
        zoom_start=12,
    )
    folium.Marker(
    location=current_coordinates,
    popup='Here I am',
    icon=folium.Icon(color='red', icon='check')
    ).add_to(map)

    tooltip = "Let's drink!"
    for bar in bars_list:
        name = bar['title']
        folium.Marker(bar['coordinates'], popup=f'<i>{name}</i>', tooltip=tooltip).add_to(map)
    map.save(path)