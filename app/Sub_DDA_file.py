import json
from DDA_column import DDA_column

#Class representing json files contating the description of individual files
class Sub_DDA_file:
    def __init__(self, dda_name, file_path):
        self.file_path = file_path
        self.dda_name = dda_name
        self.columns = {}

    #Creates a dictornary from a individual dda file with column names as keys and DDA_column objects as values
    def get_columns(self):
        with open(self.file_path, 'r') as sub_file:
            data = json.load(sub_file)

        for item in data:
            column_name = item['name']
            column_type = item['type']

            if 'description' in item:
                column_description = item['description']
                column_format = item['cid']
                if 'time_format' in item:
                    time_format = item['time_format']
                    obj = DDA_column(column_name, column_type, time_format, column_description, column_format)
                else:
                    obj = DDA_column(column_name, column_type,column_description = column_description, column_format = column_format)
            else:
                obj = DDA_column(column_name, column_type)
            self.columns[column_name] = obj
