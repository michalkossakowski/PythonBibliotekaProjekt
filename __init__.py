'''
NAME
    library

DESCRIPTION
    This package allows user to add/remove books from .csv database
    and to add/remove customers from .csv database also this package
    allows user to rent/return books for customers


PACKAGE CONTAINS
    main.py (module) - interface to use whole package
    maintest.py (module) - test if other modules works right
    books.py (module) - operations on books.csv file
    customers.py (module) - operations on customers.csv and address.csv files
    rent.py (module) - operations of renting and returning books


DATA
    Library
        address.csv - database with customers adresses
        book.csv - database with books
        customer.csv - database with customers info
    DATABASE
        [id].csv - file for every single customer with rented books

'''

__all__ = ["main","maintest","books","customers","rent"]