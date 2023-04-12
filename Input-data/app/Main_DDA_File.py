import os
import json

#Trzeba dopytac po czym bedziemy rozpoznawac ten glowny plik

#Main DDA file is being serched for while initializing Main_DDA_File object
class Main_DDA_File:
    def __init__(self,folder_path, file_name):
        self.dda_file_path = self.find_dda_file(folder_path, file_name)

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
    

    #Iterates through datasets is main DDA file and checks if they exists for now in the same folder as main file
    def get_individual_dda_files(self):
        with open(self.dda_file_path, 'r') as main_file:
            dda_file = json.load(main_file)
        dda_mini_files = {}
        for file in dda_file['datasets']:
            file_name = file['name']
            file_path = os.path.join(os.path.dirname(self.dda_file_path), f"{file_name}.json")
            exists = os.path.isfile(file_path)
            dda_mini_files[file_name] = (exists, f"{file_name}.json")
        return dda_mini_files

    
    