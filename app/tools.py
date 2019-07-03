import json
from yandex_geocoder import Client
from geopy import distance


def read_json_file(file_path, encoding):
    with open(file_path, 'r', encoding=encoding) as file:
        return json.load(file)


def convert_adress_to_coordinates(location):
    return [float(coordinate) for coordinate in Client.coordinates(location)[::-1]]


def calculate_distance(coordinates_1, coordinates_2):
    return distance.distance(coordinates_1, coordinates_2).km


def sort_list_of_dicts(bars_list, keyword='distance'):
    return sorted(bars_list, key=lambda bar: bar[keyword])