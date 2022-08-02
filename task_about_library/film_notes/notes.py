from operator import itemgetter
from services import write_csv_file, append_data_to_csv_file, read_csv_file


class FilmNotes():

    def __init__(self, filename: str):
        self.filename = filename

    def create_headers(self, headers: list = []):
        """
            headers: list of column names for csv file
        Create empty csv file with headers 
        """
        write_csv_file(filename=self.filename, headers=headers)

    def add_row(self, name: str, note: str, rating: int):
        """
            name: Name of the film
            note: Resume about the film
            rating: Number from 1 to 5
        
        Add a new film information to current csv file
        """
        if rating in range(1, 6):
            film_data = [name, note, rating]
            append_data_to_csv_file(filename=self.filename,
                                    film_data=film_data)
        else:
            print('Incorrect rating number, it has to be integer from 1 to 5.')

    def read_all_rows(self):
        """
        Read csv file and print in console
        all rows with indexes
        """
        notes_lst = read_csv_file(self.filename)
        for index, row in enumerate(notes_lst):
            print(index, row)

    def read_single_row(self, id: int):
        """
            id: row's index in list
        Iterate list of rows and append the in list
        Print in console list item by index id
        """
        notes_lst = read_csv_file(self.filename)

        print(notes_lst[0])  # print headers
        if id != 0:
            print(notes_lst[id])
        else:
            print('[INFO] Wrong id, id starts from 1.')

    def delete_row(self, id: int):
        """
            id: row's index in list
        Append all rows in list,
        Delete list item by index id,
        Rewrite csv file without deleted item.
        """
        notes_lst = read_csv_file(self.filename)

        if id != 0:
            # delete item from the list
            del notes_lst[id]
            # recreate csv file with headers
            write_csv_file(filename=self.filename, headers=notes_lst[0])
            # append the rest of items from list to the recreated csv file
            for row in notes_lst[1:]:
                append_data_to_csv_file(filename=self.filename, film_data=row)
        else:
            print('[INFO] Wrong id, id starts from 1.')
            
    def sort_by_rate(self, asc:bool=None, desc:bool=None):
        """
            asc: Boolean value
            desc: Boolean value
            asc: => sorting list from min to max
            desc: => sorting lost from max to min
            default: => asc
        """
        # check how to sort list
        if asc:
            blean = False 
        elif desc:
            blean = True
        else:
            blean = False 
        
        # list with sorted items
        result = []
        notes_lst = read_csv_file(self.filename)
        sorting_lst = notes_lst[1:]
        sorted_lst = sorted(sorting_lst, key=itemgetter(2), reverse=blean)
        result.append(notes_lst[0])
        for i in sorted_lst:
            result.append(i)
        print(result)
        



notes = FilmNotes('My_note')
# notes.create_headers(['film_title', 'note', 'rating'])
# notes.add_row('Калина', 'Гарний', 4)
# notes.add_row('Ластівка', 'Слабкий', 2)
# notes.add_row('Сонце', 'Чудовий', 5)
# notes.add_row('Калина', 'Гівно', 1)
# notes.delete_row(id=2)
# notes.read_all_rows()
# notes.read_single_row(id=1)
# notes.delete_row(id=1)
# notes.sort_by_rate()
