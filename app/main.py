from app.DDAFile import DDAFile
from app.DDAFileValidator import DDAFileValidator


class Main:
    def __init__(self, file_name, file_location):
        dda_file = DDAFile()
        self.files_location = dda_file.find_dda_file(file_name, file_location)
        self.dda_validator = DDAFileValidator(self.files_location)

    def run(self):
        # validate files
        print("Validating files...")
        file_list = self.dda_validator.validate_files(self.files_location)
        for file_name, exists in file_list:
            print(f"{file_name} exists: {exists}")


if __name__ == "__main__":
    main = Main("contoption", "C:\\Users\\micha\\Desktop\\Projekt grupowy")
    main.run()