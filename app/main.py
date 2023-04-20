from Main_DDA_File import Main_DDA_File
from Sub_DDA_file import Sub_DDA_file
import sys

if __name__ == "__main__":
    #dda_files_path = sys.argv[0]    #Chcieli zeby mozna bylo moc podawac sciezke jako argument
    #main_dda_file = sys.argv[1]
    #dda_files_path = input("Podaj ścieżkę do plików: ")          #path to the folder with data files
    #main_file_path = input("Podaj sciezke do głównego pliku: ")  #path to the main json file
    dda_files_path = '/home/vboxuser/repos/data_analisys_tool/test_files'
    main_file_path = '/home/vboxuser/repos/data_analisys_tool/test_files/marketdata.json'
    main_dda_file = Main_DDA_File(dda_files_path, main_file_path)

    dictonary_true = {}
    sub_dda_files = main_dda_file.get_sub_dda_files()
    for key in sub_dda_files:
        exists, path = sub_dda_files[key]
        print(key, exists)
        if (exists == True):
            sub_file = Sub_DDA_file(key, path)
            sub_file.get_columns()
            dictonary_true[key] = sub_file