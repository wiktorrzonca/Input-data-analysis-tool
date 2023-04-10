import os
import json
from DDA_column import DDA_column

class DDA_file:
    def __init__(self, dda_name, dda_file_path):
        self.dda_file_path = dda_file_path
        self.file_name = dda_name
        self.columns = {}

    def dictonary(self):
        with open (self.dda_file_path) as f:
            data = json.load(f)

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
                        obj = DDA_column(column_name, column_type, None, column_description, column_format)
                else: 
                    obj = DDA_column(column_name, column_type, None, None, None)
                self.columns[column_name] = obj