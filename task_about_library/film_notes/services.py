import csv

def create_csv_file(filename, headers):
    with open(f'{filename}.csv', 'w', encoding='utf-8', newline='') as file:
        wrirer = csv.writer(file)
        wrirer.writerow(headers)
        
def append_data_to_csv_file(filename:str, data:list):
    with open(f'{filename}.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)