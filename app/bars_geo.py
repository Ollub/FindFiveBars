from app.tools import read_json_file, sort_list_of_dicts, convert_adress_to_coordinates, calculate_distance


def fetch_bar_geo(bar_info, current_coordinates):
    bar_geo = {}
    bar_coordinates = bar_info['geoData']['coordinates'][::-1]
    distance = calculate_distance(bar_coordinates, current_coordinates)
    bar_geo['title'] = bar_info['Name']
    bar_geo['coordinates'] = bar_coordinates
    bar_geo['distance'] = distance
    return bar_geo


def fetch_bars_geo(current_location):
    bars = read_json_file('app/data/bars_data.json', 'CP1251')
    bars_geo = []
    current_coordinates = convert_adress_to_coordinates(current_location)
    for bar in bars:
        bar_geo = fetch_bar_geo(bar, current_coordinates)
        bars_geo.append(bar_geo)
    return sort_list_of_dicts(bars_geo)