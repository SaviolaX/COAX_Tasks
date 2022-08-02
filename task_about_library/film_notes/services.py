import csv


def write_csv_file(filename: str, headers:list) -> object:
    with open(f'{filename}.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)


def append_data_to_csv_file(filename: str, film_data:list) -> object:
    with open(f'{filename}.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(film_data)


def read_csv_file(filename: str) -> list:
    with open(f'{filename}.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        lst = []
        for row in reader:
            lst.append(row)
    return lst
