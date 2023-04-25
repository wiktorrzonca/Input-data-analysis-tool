import csv
import json

class CsvJsonComparator:
    def __init__(self, path_to_csv, path_to_json):
        self.path_to_csv = path_to_csv
        self.path_to_json = path_to_json

    def compare_csv_to_json(self):
        # Load JSON file
        with open(self.path_to_json, 'r') as json_file:
            json_data = json.load(json_file)

        # Get column names and types from JSON
        column_names = [item['name'] for item in json_data]
        column_types = [item['type'] for item in json_data]

        # Load CSV file
        with open(self.path_to_csv, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_column_names = next(csv_reader)
            csv_column_types = [type(cell).__name__ for cell in next(csv_reader)]

        # Compare column names
        if column_names != csv_column_names:
            print("Column names in CSV file do not match column names in JSON file")
            return False

        # Compare column types
        if column_types != csv_column_types:
            print("Column types in CSV file do not match column types in JSON file")
            return False

        # If everything matches, return True
        return True
