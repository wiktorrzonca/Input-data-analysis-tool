import tarfile
import os

class Csv_file_reader:

    def __init__(self, path_to_tar):
        self.path_to_tar = path_to_tar

    def get_file_list(self):
        dir_path = self.path_to_tar + '/csv_files'
        return os.listdir(dir_path)

    def extract(self):
        with tarfile.open(self.path_to_tar, 'r:gz') as tar_ref:
            tar_ref.extractall('csv_files')

    def check_files(self):
        missing_files = []
        for file in os.listdir(self.path_to_tar + '/csv_files'): #otworzenie katalogu csv_files
                file_json = os.path.splitext(file)[0] + '.json' #zmiana rozszezenia na json
                if not os.path.isfile(self.path_to_tar + file_json):
                    missing_files.append(file) 
        return missing_files #zwracana jest lista plikow ktorych brakuje, jak są wszystkie to zwraca pusta liste