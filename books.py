'''
NAME
    books

DESCRIPTION
    This module allow user to add or remove book to the database saved in .csv file
    also this module can display full dataframe from .csv file and return dataframe
    to use it in tkinter

FUNCTIONS
    This module contains the following functuions

    *displaybooks() - this function print full dataframe form .csv file in console

    *dfbooks() - returns dataframe from .csv file to use it in tkinter

    *addbook(author, title, pages) - this function add new row(book) in .csv database
    file with columns author, title as string and amount of pages in int from arguments
    and created,updated as date from datetime

    *removebook(idortitle) - this function remove book (row) from .csv database file
    by id(if argument idortitle is int) or title(if argument idortitle is string)

EXAMPLES
    addbook('Sanah','Melodia',31)
    displaybooks()
    removebook('Melodia')
    displaybooks()
'''

import pandas as pd
import random
from datetime import *

pd.set_option('display.max_columns', None)  # unlimited columns to print
pd.set_option('display.max_rows', None)  # unlimited rows to print

bfile = 'Library/book.csv'

def addbook(author, title, pages):
    """
    This function add new book to .csv database file, with 'ID' as random 3 digital number,
    which is randomized until it is unique, 'AUTHOR','TITLE' and 'PAGES' as arguments,
    'CREATED' and 'UPDATED' as dates from datetime, if database have 900 books inside
    you can't add more books

    Args:
        author: string to write as 'AUTHOR' to database file
        title: string to wirte as 'TITLE' to database file
        pages: int to write as 'PAGES' to database file
    """
    bookfile = pd.read_csv(bfile)
    try:
        if len(bookfile) >= 900:
            raise ValueError('Database cant hold more than 900 books')
    except ValueError as e:
        print('Add Error:', e)
        return
    while True:
        newid = random.randint(100, 1000)
        if newid in bookfile['ID'].values:
            continue
        else:
            break
    newbook = {'ID': newid,
               'AUTHOR': author,
               'TITLE': title,
               'PAGES': pages,
               'CREATED': date.today(),
               'UPDATED': date.today()
               }
    newdataframe = pd.DataFrame([newbook])
    newdataframe.to_csv(bfile, mode='a', header=False, index=False)


def removebook(idortitle):
    oldbookfile = pd.read_csv(bfile)
    try:
        if isinstance(idortitle, int):
            if oldbookfile[oldbookfile['ID'] == idortitle].empty:
                raise NameError('Book with id: "{}" not exist'.format(idortitle))
            else:
                bookfile = oldbookfile[oldbookfile['ID'] != idortitle]
        elif isinstance(idortitle, str):
            if oldbookfile[oldbookfile['TITLE'] == idortitle].empty:
                raise NameError('Book with title: "{}" not exist'.format(idortitle))
            else:
                mask = oldbookfile['TITLE'] == idortitle
                bookfile = oldbookfile.drop(oldbookfile.index[mask][0])
        bookfile.to_csv(bfile, index=False)
    except NameError as e:
        raise NameError(e) # to showerror in tkinter
        print('Remove Error:', e)

def displaybooks():
    print(pd.read_csv(bfile).to_string())  # convert to string to print in one line

def dfbooks():
    return pd.read_csv(bfile) #to print dataframe in tkinter
