import tarfile
import os
import re
import csv
import datetime
from ErrorLogger import ErrorLogger
class Csv_file_reader:

    #to tak pogladowo narazie potem do posprzatania
    def __init__(self, filePath):
        self.filePath = filePath
        self.errorLog = ErrorLogger(filePath)

    @staticmethod
    def extract(path_to_tar):
        with tarfile.open(path_to_tar, 'r:gz') as tar_ref:
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

    def validate_file(self, ddaFile):

        # Otwórz plik CSV i wczytaj zawartość
        with open(self.filePath, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            headers = next(csv_reader)  # wczytaj pierwszy wiersz, który zawiera nagłówki kolumn
            # Sprawdź czy liczba kolumn w pliku CSV jest taka sama jak w słowniku kolumn
            if len(headers) != len(ddaFile):
                self.errorLog.addWarning(f"File contains: {len(headers)} columns, expected: {len(ddaFile)}")
                #print("Number of columns in CSV file does not match the number of objects in dictionary_file.")

            # Iteruj po kolumnach i sprawdź czy ich nazwy zgadzają się z definicjami w słowniku kolumn
            for header_count, column_name in enumerate(ddaFile):
                print('2')
                if header_count > len(headers) - 1:
                    return
                
                if headers[header_count] != ddaFile[column_name].name:
                    self.errorLog.addError(f"Column name({headers[header_count]}) in CSV file does not match the name ({ddaFile[column_name].name}) in DDA file .")
                    #print(f"Column name in CSV file ({headers[header_count]}) does not match the name in dictionary_file ({columns[column_name].name}).")
                    continue

                expected_type = ddaFile[column_name].type

                row_count = 0
                # Iteruj po każdym wierszu w kolumnie i sprawdź typ wartości oraz poprawność formatu daty, jeśli dotyczy
                for row in csv_reader:
                    # Wyświetl typ oczekiwany oraz otrzymany dla danej kolumny i wiersza

                    if expected_type == "INTEGER":
                        try:
                            int(row[header_count])
                        except ValueError:
                            self.errorLog.addError(f"Value row: {row_count} column: {header_count} is not an INTIGER.")
                            #print(f"Value row: {row_count} column: {header_count} is not an INTIGER.")
                    elif expected_type == "DOUBLE":
                        try:
                            float(row[header_count])
                        except ValueError:
                            self.errorLog.addError(f"Value row: {row_count} column: {header_count} is not an INTIGER.")
                            #print(f"Value row: {row_count} column: {header_count} is not a DOUBLE.")
                    elif expected_type == "STRING":
                        if row[header_count].isnumeric():
                            self.errorLog.addError(f"Value row: {row_count} column: {header_count} is not an INTIGER.")
                            #print(f"Value row: {row_count} column: {header_count} is not a STRING.")
                    #TU JEST ŹLE NIE DZIAŁA DLA DOBER DATY POKAZUJE ŻE JEST ZŁA DATA
                    elif expected_type == "DATE" or expected_type == "TIMESTAMP":
                        if ddaFile[column_name].time_format is None:
                            self.errorLog.addWarning(f"In column: {column_name} of the type DATE, time format is not specified")
                            continue
                        time_format = ddaFile[column_name].time_format.upper()
                        pattern = ''
                        if time_format == "YYYY-MM-DDTHH:MM:SS" or time_format == "YYYY-MM-DD'T'HH:MM:SS":
                            pattern = '^(?!0000)(?:\d{4}|[1-9]\d{0,3})-(?:(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8]))|(?:0[13-9]|1[0-2])-30|(?:0[13578]|1[02])-31)(?:T| (?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d)$'
                        elif time_format == "MM/DD/YYYY":
                            pattern = '^(0[1-9]|1[0-2])/(0[1-9]|1\d|2[0-9]|3[01])/([12]\d{3})$'
                        elif time_format == "MM-DD-YYYY":
                            pattern = '^(0[1-9]|1[0-2])-(0[1-9]|1\d|2[0-9]|3[01])-([12]\d{3})$'
                        elif time_format == "Month DD, YYYY":
                            pattern = '^(January|February|March|April|May|June|July|August|September|October|November|December)\s(0[1-9]|[12]\d|3[01]),\s([12]\d{3})$'
                        elif time_format == "DD-MM-YYYY":
                            pattern = '^(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(\d{4})$'
                        elif time_format == "DD/MM/YYYY":
                            pattern = '^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/(\d{4})$'
                        elif time_format == "YYYY-MM-DD":
                            pattern = '^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
                        elif time_format == "YYYY/MM/DD":
                            pattern = '^(\d{4})/(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])$'
                        elif time_format == "DD-MMM-YYYY":
                            pattern = '^\d{2}-(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{4}$'
                        else:
                            self.errorLog.addWarning("Unrecognised time format")
                        if not re.match(pattern, row[header_count]):
                            self.errorLog.addError(f"Value row: {row_count} column: {header_count} does not match the time format ({time_format}) in DDA file .")
                    row_count += 1

                csvfile.seek(0)
                next(csv_reader)  # pomiń nagłówek dla kolejnych kolumn

        return self.errorLog


