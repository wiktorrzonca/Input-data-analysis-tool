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

        # Otwórz plik CSV i wczytaj zawartość
        with open(csv_path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            headers = next(csv_reader)  # wczytaj pierwszy wiersz, który zawiera nagłówki kolumn

            # Sprawdź czy liczba kolumn w pliku CSV jest taka sama jak w słowniku kolumn
            if len(headers) != len(columns):
                print("Number of columns in CSV file does not match the number of objects in dictionary_file.")

            # Iteruj po kolumnach i sprawdź czy ich nazwy zgadzają się z definicjami w słowniku kolumn
            for header_count, column_name in enumerate(columns):

                if header_count > len(headers) - 1:
                    return
                
                if headers[header_count] != columns[column_name].name:
                    print(f"Column name in CSV file ({headers[header_count]}) does not match the name in dictionary_file ({columns[column_name].name}).")
                    continue

                expected_type = columns[column_name].type

                row_count = 0
                # Iteruj po każdym wierszu w kolumnie i sprawdź typ wartości oraz poprawność formatu daty, jeśli dotyczy
                for row in csv_reader:
                    # Wyświetl typ oczekiwany oraz otrzymany dla danej kolumny i wiersza
                    #print(f" type {expected_type}  a jest - {row[header_count]}")

                    if expected_type == "INTEGER":
                        try:
                            int(row[header_count])
                        except ValueError:
                            print(f"Value row: {row_count} column: {header_count} is not an INTIGER.")
                    elif expected_type == "DOUBLE":
                        try:
                            float(row[header_count])
                        except ValueError:
                            print(f"Value row: {row_count} column: {header_count} is not a DOUBLE.")
                    elif expected_type == "STRING":
                        if row[header_count].isnumeric():
                            print(f"Value row: {row_count} column: {header_count} is not a STRING.")
                    #TU JEST ŹLE NIE DZIAŁA DLA DOBER DATY POKAZUJE ŻE JEST ZŁA DATA
                    if columns[column_name].time_format is not None:
                        try:
                            datetime.datetime.strptime(row[header_count], "%Y-%m-%d")
                        except ValueError:
                            print(
                                f"Value row: {row_count} column: {header_count} does not match the time format in dictionary_file ({columns[column_name].time_format}).")
                    row_count += 1

                csvfile.seek(0)
                next(csv_reader)  # pomiń nagłówek dla kolejnych kolumn


