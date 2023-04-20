import csv
import json


def get_example_value(obj):
    if obj["type"] == "STRING":
        return "example"
    elif obj["type"] == "INTEGER":
        return 1
    elif obj["type"] == "DATE":
        return "2022-01-01"
    

#Podajesz sciezke do pliku dla ktroego chcesz wytworzyc przykladowe dane
json_path = "/home/vboxuser/repos/data_analisys_tool/test_files/contoption.json"

#Podajesz gdzie sie ma zapisac
output_file = "contoption.csv"

with open(json_path, "r") as f:
    data = json.load(f)

with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    header = [obj["name"] for obj in data]
    writer.writerow(header)
    
    if len(data) > 0:
        for i in range(3):
            row = [get_example_value(obj) for obj in data]
            writer.writerow(row)
            i += 1
