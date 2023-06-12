from Main_DDA_File import Main_DDA_File
from Sub_DDA_file import Sub_DDA_file
from Csv_file_reader import Csv_file_reader
import sys
import os

if __name__ == "__main__":
    ###THE PROGRAM MUST ASK USER FOR INPUT FILE LOCATION
    main_folder = sys.argv[1]    #Chcieli zeby mozna bylo moc podawac sciezke jako argument
    #main_dda_file = sys.argv[0]


    #main_folder = '/home/vboxuser/repos/data_analisys_tool'

    dda_files_path = main_folder + '\\test_files\\'
    main_file_path= main_folder + '\\test_files\\marketdata.json'
    csv_files_path = main_folder + '\\csv_files\\'

    #Tu trzeba spytac ich po czym rozpoznamy ten glowny plik : czy po nazwie czy trzeba do srodka zagladac

    ###PROGRAM SCANS THROUTH THE FILES FOR THE MAIN DDA .JSON FILE
    main_dda_file = Main_DDA_File(dda_files_path)

    dictonary_sub = {}

    ###PROGRAM GETS THE NAMES FOR THE EXPECTED DATASETS
    data_sets = main_dda_file.get_sub_dda_files()

    ###THE PROGRAM WILL LOOK FOR INDIVIDUAL DATASET JSONS TO GET EXPECTED SCHEMA
    for data_set in data_sets:
        exists, path = data_sets[data_set]
        if (exists == True):
            sub_file = Sub_DDA_file(data_set, path)
            sub_file.get_columns()
            dictonary_sub[data_set] = sub_file

    ###THE PROGRAM UNZIPS THE TAR FOLDER
    #Csv_file_reader.extract(main_folder + '/csv_files.tar.gz')

    ###GOES THROUGH EACH CSV FILE AND DETECS IF THERE ARE ANY POSSIBLE ERRORS
    errorLogs = {}
    for file in os.listdir(csv_files_path):
        errorLogs[file] = Csv_file_reader(csv_files_path + file).validate_file(dictonary_sub[file[:-4]].columns)

    ###THE PROGRAM OUTPUTS THE LOG
    for log in errorLogs:
        print("Raport for file: " + log)
        errorLogs[log].displayReport()
        errorLogs[log].saveToFile()