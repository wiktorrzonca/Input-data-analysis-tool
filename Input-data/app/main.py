from Main_DDA_File import Main_DDA_File
from DDA_file import DDA_file
import sys

if __name__ == "__main__":
    path = input("Podaj ścieżkę do plików: ")
    mainFile = input("Podaj nazwę głównego pliku: ")
    main_dda_file = Main_DDA_File(path, mainFile)

    dictonary_true = {}
    dda_mini_files = main_dda_file.get_individual_dda_files()
    for key in dda_mini_files:
        exists, path = dda_mini_files[key]
        print(key, exists)
        if (exists == True):
            obj = DDA_file(key, path)
            obj.dictonary()
            dictonary_true[key] = obj