import os
import json

class DDAFileValidator:
    def __init__(self, dda_file_path):
        self.dda_file_path = dda_file_path
        self.file_names = []
        self.file_exists = []

    #Get the names of expected data sets
    #Returns a list with file names and boolean values true - if they exist
    def validate_files(self, folder_path):
        with open(self.dda_file_path) as f:
            data = json.load(f)

            for item in data:
                file_name = item['name']
                file_path = os.path.join(os.path.dirname(folder_path), f"{file_name}.json")
                exists = os.path.isfile(file_path)

                self.file_names.append(file_name)
                self.file_exists.append(exists)

        return list(zip(self.file_names, self.file_exists))

        
