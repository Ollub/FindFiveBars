from flask import Flask

from tools import read_json_file, fetch_bar_geo, sort_list_of_dicts, convert_adress_to_coordinates
from map import create_bar_map_template


app = Flask('__name__')

def main():
    bars = read_json_file('data/bars_data.json', 'CP1251')
    bars_geo = []
    current_location = 'Reutov'
    current_coordinates = convert_adress_to_coordinates(current_location)
    for bar in bars[:20]:
        bar_geo = fetch_bar_geo(bar, current_coordinates)
        bars_geo.append(bar_geo)
    bars_geo = sort_list_of_dicts(bars_geo)
    print(bars_geo)
    create_bar_map_template(current_coordinates, bars_geo[:5])


if __name__ == '__main__':
    main()