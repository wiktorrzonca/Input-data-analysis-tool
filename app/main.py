from Main_DDA_File import Main_DDA_File
import sys



if __name__ == "__main__":
    #path = sys.argv[1]
    path = '/home/vboxuser/repos/data_analisys_tool/Input-data-analysis-tool/test_files'
    main_dda_file = Main_DDA_File(path,'marketdata.json')
    
    dda_mini_files = main_dda_file.get_individual_dda_files() 
    for key,val in dda_mini_files.items():
        print(key,val)