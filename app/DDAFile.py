import os


class DDAFile:
    def __init__(self):
        self.file_location = None
        self.file_name = None

    def find_dda_file(self, file_name,file_location):
        dda_file = None
        for root, dirs, files in os.walk(file_location):
            for file in files:
                if file.endswith(".json") and file_name in file:
                    dda_file = os.path.join(root, file)
                    break
            if dda_file:
                break
        if not dda_file:
            raise FileNotFoundError(f"{file_name} file not found in the specified directory")
        return dda_file
