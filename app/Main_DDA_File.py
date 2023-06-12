import os
import json
#Trzeba dopytac po czym bedziemy rozpoznawac ten glowny plik

#Main DDA file is being serched for while initializing Main_DDA_File object
class Main_DDA_File:
    def __init__(self, dda_files_path,):
        self.file_path = dda_files_path + '\\marketdata.json'
        self.dda_files_path = dda_files_path

    #Mam wrazenie ze aktualnie ta funkcja nie ma sensu bo bierze sciezke do folderu i pliku i zwraca to samo
    #ewentualnie wyrzuca blad jak nie znajdzie, ale mozemy ja zostawic bo w przyszlosciu mozemu tu wrzucic jakis 
    #madry sposob na rozpoznawanie tego pliku glownego bez znania jego nazwy
    #Scanning for a main DDA file
    def find_dda_file(self, folder_path, file_name):
        dda_file = None
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".json") and file_name in file:
                    dda_file = os.path.join(root, file)
                    break
            if dda_file:
                break
        if not dda_file:
            raise FileNotFoundError(f"{file_name} file not found in the specified directory")
        
        return dda_file
    

    #Iterates through datasets in main DDA file and checks if they exists for now in the same folder as main file
    #Returns a dictonary with dda names as keys and values with boolean values equal to true if the files exists and path to the file
    def get_sub_dda_files(self):
        with open(self.file_path, 'r') as main_file:
            dda_file = json.load(main_file)

        dda_sub_files = {}
        for file in dda_file['datasets']:
            file_name = file['name']
            file_path = os.path.join(self.dda_files_path, f"{file_name}.json")
            exists = os.path.isfile(file_path)
            dda_sub_files[file_name] = (exists, file_path)
        return dda_sub_files

    
    