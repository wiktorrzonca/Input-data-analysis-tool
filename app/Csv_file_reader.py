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

    def validate_file(self, columns, csv_path):
        error_messages = []  # inicjalizacja pustej listy przechowującej komunikaty błędów

        # Sprawdzenie ilości kolumn w pliku csv
        with open(csv_path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            headers = next(csv_reader)
            if len(headers) != len(columns):
                error_messages.append(
                    "Number of columns in CSV file does not match the number of objects in dictionary_file.")

            # Przejście po każdej kolumnie w pliku csv
            header_count = 0
            for column_name in columns :
                # Sprawdzenie nazwy kolumny
                if headers[header_count] != columns[column_name].name:
                    error_messages.append(
                        f"Column name in CSV file ({headers[header_count]}) does not match the name in dictionary_file ({columns[column_name].name}).")
                header_count +=1
                # Sprawdzenie typu danych w kolumnie
                expected_type = columns[column_name].type
                next(csv_reader)  # pominięcie nagłówka
                column_count= 0
                for row in csv_reader:
                    cell = row[header_count+column_count]
                    print(f" type {expected_type}  a jest - {cell}")
                    column_count+=1
                    if expected_type == "INTEGER":
                        try:

                            int(cell)
                        except ValueError:
                            error_messages.append(f"Value in column {cell} is not an integer.")
                    elif expected_type == "DOUBLE":
                        try:
                            float(cell)
                        except ValueError:
                            error_messages.append(f"Value in column {cell} is not a float.")
                    elif expected_type == "bool":
                        if cell.lower() not in ["true", "false"]:
                            error_messages.append(f"Value in column {cell} is not a boolean.")
                    elif expected_type == "STRING":
                        pass  # wszystko jest dozwolone

                    # Sprawdzenie formatu czasu/daty
                    if columns[column_name].time_format is not None:
                        try:
                            datetime.datetime.strptime(cell, columns[column_name].time_format)
                        except ValueError:
                            error_messages.append(
                                f"Value in column {cell} does not match the time format in dictionary_file ({columns[column_name].time_format}).")

        if error_messages:  # jeśli lista błędów nie jest pusta, to rzuć wyjątek z listą błędów
            raise ValueError('\n'.join(error_messages))

