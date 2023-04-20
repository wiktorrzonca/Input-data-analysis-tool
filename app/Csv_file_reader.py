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