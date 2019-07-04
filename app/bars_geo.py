from app.tools import read_json_file, sort_bars, convert_adress_to_coordinates, calculate_distance


def define_bar_geo(bar_info, current_coordinates):
    distance = calculate_distance(bar_coordinates, current_coordinates)
    bar_geo = {
        'title': bar_info['Name'],
        'coordinates': bar_info['geoData']['coordinates'][::-1],
        'distance': distance,
    }
    return bar_geo


def fill_bars_geo(current_location):
    bars = read_json_file('app/data/bars_data.json', 'CP1251')
    bars_geo = []
    current_coordinates = convert_adress_to_coordinates(current_location)
    for bar in bars:
        bar_geo = define_bar_geo(bar, current_coordinates)
        bars_geo.append(bar_geo)
    return sort_bars(bars_geo)