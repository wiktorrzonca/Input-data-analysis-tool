import tarfile
import os
import csv
import datetime
class Csv_file_reader:

    #to tak pogladowo narazie potem do posprzatania
    def __init__(self, path_to_tar):
        self.path_to_tar = path_to_tar + '/csv_files.tar.gz'
        self.csv_path = path_to_tar + '/csv_files'
        self.json_path = path_to_tar + '/test_files/'


    def extract(self):
        with tarfile.open(self.path_to_tar, 'r:gz') as tar_ref:
            tar_ref.extractall('csv_files')

    #Tego w sumie od nas nie oczekiwali jak sie okazuje
    #Bo w tym dokumencie jest napisane tylko zebysmy sprawdzali czy sa wszystki mini jsony opisane w giga jsony
    #Ale jak juz mamy to niech bedzie
    #Ta funkcja sprawdza czy dla wszystkich csvek sa jsony
    def check_files(self):
        missing_files = []
        for file in os.listdir(self.csv_path): #otworzenie katalogu csv_files
                file_json = os.path.splitext(file)[0] + '.json' #zmiana rozszezenia na json
                if not os.path.isfile(self.json_path + file_json):
                    missing_files.append(file) 
        return missing_files #zwracana jest lista plikow ktorych brakuje, jak są wszystkie to zwraca pusta liste
    def validate_files(self,dictionary_true, csv_path):
        # Sprawdzenie ilości kolumn w pliku csv
        with open(csv_path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            headers = next(csv_reader)
            if len(headers) != len(dictionary_true):
                raise ValueError(
                    "Number of columns in CSV file does not match the number of objects in dictionary_file.")

            # Przejście po każdej kolumnie w pliku csv
            for index, column in enumerate(headers):
                # Sprawdzenie nazwy kolumny
                if column != dictionary_true[index].name:
                    raise ValueError(
                        f"Column name in CSV file ({column}) does not match the name in dictionary_file ({dictionary_true[index].name}).")

                # Sprawdzenie typu danych w kolumnie
                expected_type = dictionary_true[index].type
                with open(csv_path, newline='') as csvfile:
                    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                    next(csv_reader)  # pominięcie nagłówka
                    for row in csv_reader:
                        cell = row[index]
                        if expected_type == "int":
                            try:
                                int(cell)
                            except ValueError:
                                raise ValueError(f"Value in column {column} is not an integer.")
                        elif expected_type == "float":
                            try:
                                float(cell)
                            except ValueError:
                                raise ValueError(f"Value in column {column} is not a float.")
                        elif expected_type == "bool":
                            if cell.lower() not in ["true", "false"]:
                                raise ValueError(f"Value in column {column} is not a boolean.")
                        elif expected_type == "string":
                            pass  # wszystko jest dozwolone

                        # Sprawdzenie formatu czasu/daty
                        if dictionary_true[index].time_format is not None:
                            try:
                                datetime.datetime.strptime(cell, dictionary_true[index].time_format)
                            except ValueError:
                                raise ValueError(
                                    f"Value in column {column} does not match the time format in dictionary_file ({dictionary_true[index].time_format}).")
