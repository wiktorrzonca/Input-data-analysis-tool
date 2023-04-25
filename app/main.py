from Main_DDA_File import Main_DDA_File
from Sub_DDA_file import Sub_DDA_file
from Csv_file_reader import Csv_file_reader
import sys

if __name__ == "__main__":
    ###THE PROGRAM MUST ASK USER FOR INPUT FILE LOCATION
    #dda_files_path = sys.argv[0]    #Chcieli zeby mozna bylo moc podawac sciezke jako argument
    #main_dda_file = sys.argv[1]


    #dda_files_path = input("Podaj ścieżkę do plików: ")          #path to the folder with data files
    #main_file_path = input("Podaj sciezke do głównego pliku: ")  #path to the main json file

    dda_files_path ="C:/Users/micha/PycharmProjects/inputDataAnalysysTool/Input-data-analysis-tool/test_files"
    main_file_path="C:/Users/micha/PycharmProjects/inputDataAnalysysTool/Input-data-analysis-tool/test_files/marketdata.json"

    #Tu trzeba spytac ich po czym rozpoznamy ten glowny plik : czy po nazwie czy trzeba do srodka zagladac

    ###PROGRAM SCANS THROUTH THE FILES FOR THE MAIN DDA .JSON FILE
    main_dda_file = Main_DDA_File(dda_files_path, main_file_path)

    dictonary_sub = {}

    ###PROGRAM GETS THE NAMES FOR THE EXPECTED DATASETS
    sub_dda_files = main_dda_file.get_sub_dda_files()

    ###THE PROGRAM WILL LOOK FOR INDIVIDUAL DATASSET JSONS TO GET EXPECTED SCHEMA
    for sub_name in sub_dda_files:
        exists, path = sub_dda_files[sub_name]
        #print(key, exists)
        if (exists == True):
            sub_file = Sub_DDA_file(sub_name, path)
            sub_file.get_columns()
            dictonary_sub[sub_name] = sub_file

    ###THE PROGRAM UNZIPS THE TAR FOLDER
    csv_reader = Csv_file_reader("C:/Users/micha/PycharmProjects/inputDataAnalysysTool/Input-data-analysis-tool")
    csv_reader.extract()
    #for file in csv_reader.check_files():
        #print(file)
    #csv_path = input("Podaj ścieżkę do pliku csv: ")
    csv_path = "C:/Users/micha/PycharmProjects/inputDataAnalysysTool/Input-data-analysis-tool/csv_files\contoption.csv"
    ###GOES THROUGH EACH CSV FILE AND DETECS IF THERE ARE ANY POSSIBLE ERRORS
    #for sub_key_name in dictonary_sub:

    csv_reader.validate_file(dictonary_sub["contoption"].columns,csv_path)

    ###THE PROGRAM OUTPUTS THE LOG
    #TODO