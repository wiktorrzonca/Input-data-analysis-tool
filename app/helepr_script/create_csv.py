import csv
import json
import random


def get_correct_data(obj):
    if obj["type"] == "STRING":
        return "example"
    elif obj["type"] == "INTEGER":
        return 1
    elif obj["type"] == "DATE":
        return "2022-01-01"
    elif obj["type"] == "DOUBLE":
        return 1.0
    elif obj["type"] == "TIMESTAMP":
        pass #TODO
    else:
        return None
    
def get_incorrect_data(obj):
    if obj["type"] == "STRING":
        return 1
    elif obj["type"] == "INTEGER":
        return 1.0
    elif obj["type"] == "DATE":
        return "01-2022-02"
    elif obj["type"] == "DOUBLE":
        return "NOT DOUBLE"
    else:
        return None
    

#Podajesz sciezke do pliku dla ktroego chcesz wytworzyc przykladowe dane
json_path = "/home/vboxuser/repos/data_analisys_tool/test_files/trader_cds_price.json"

#Podajesz gdzie sie ma zapisac
output_file = "trader_cds_price.csv"

with open(json_path, "r") as f:
    data = json.load(f)

with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    header = [obj["name"] for obj in data]
    writer.writerow(header)
    
    if len(data) > 0:
        for i in range(20):
            if random.randint(0,10) == 1:
                row = [get_incorrect_data(obj) for obj in data]
            elif random.randint(0,10) == 2:
                continue
            else:
                row = [get_correct_data(obj) for obj in data]
            writer.writerow(row)
