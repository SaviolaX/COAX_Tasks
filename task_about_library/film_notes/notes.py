import csv
import os
import pandas as pd

from random import randint
from services import create_csv_file, append_data_to_csv_file





class FilmNotes():

    def __init__(self, filename: str):
        self.filename = filename

    def create(self, headers=[]):
        """Create csv file with default headers"""
        create_csv_file(filename=self.filename, headers=headers)

    def add(self, name: str, note: str, rating: int):
        """Add a new film information to current csv file"""
        if rating in range(1, 6):
            film_data = [name, note, rating]
            append_data_to_csv_file(filename=self.filename, data=film_data)
        else:
            print('Incorrect rating number, it has to be integer from 1 to 5.')
    
    def read(self):
        df = pd.read_csv(f'{self.filename}.csv')
        print(df.head())
        # with open(f'{self.filename}.csv', 'r', encoding='utf-8') as file:
        #     reader = csv.reader(file)
        #     for row in reader:
        #         print(row)

    def delete(self, id:int):
        df = pd.read_csv(f'{self.filename}.csv')
        df.drop(df.index[id], axis=0, inplace=True)
        print(f'Row was deleted successfully.')

notes = FilmNotes('My_note')
# notes.create(['film_title', 'note', 'rating'])
# notes.add('Калина', 'Гарний', 4)
# notes.add('Ластівка', 'Слабкий', 2)
# notes.add('Сонце', 'Чудовий', 5)
# notes.add('Калина', 'Гівно', 1)
notes.delete(id=0)
notes.read()

