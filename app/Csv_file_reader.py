import tarfile
import os

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
    

    def validate_files(self):
         pass
         #TODO