from .constants import DATA_FILE_PATH
import csv


def get_data_map():
    data_map = {}
    with open(DATA_FILE_PATH, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data_map[row[0]] = row[1]
    return data_map
