import pandas as pd
from datetime import *

bfile = 'Library/book.csv'
cfile = 'Library/customer.csv'

def rentbook(customerid, *args):
    customerfile = pd.read_csv(cfile)
    try:
        if customerfile[customerfile['ID']==customerid].empty:
            raise ValueError('Customer with id: {} not exist'.format(customerid))
    except ValueError as e:
        raise NameError(e) # for tkinter showerror
        print('Rent Error:', e)
        return
    rfile = 'DATABASE/' + str(customerid) + '.csv'
    bookfile = pd.read_csv(bfile)

    def insertrent(bookid):
        newrent = {'ID': bookid,
                   'TITLE': bookfile[bookfile['ID']==bookid]['TITLE'].values[0],
                   'RENT': date.today(),
                   'RETURN': 'RENTED'
                   }
        newrentdataframe = pd.DataFrame([newrent])
        newrentdataframe.to_csv(rfile, mode='a', header=False, index=False)

    for booktitle in args:
        try:
            if bookfile[bookfile['TITLE'] == booktitle].empty:
                raise NameError('Book with title: "{}" not exist'.format(booktitle))
            else:
                samebooks = bookfile[bookfile['TITLE'] == booktitle]
                for i in range(0, len(samebooks)):
                    if samebooks['UPDATED'].values[i] == 'RENTED':
                        i += 1
                    else:
                        break
                if i == len(samebooks):
                    raise ValueError('All books with title: "{}" are rented'.format(booktitle))
                rentbookid = bookfile[bookfile['TITLE'] == booktitle]['ID'].values[i]
                insertrent(rentbookid)
                bookfile.loc[bookfile['ID'] == rentbookid, 'UPDATED'] = 'RENTED'
                bookfile.to_csv(bfile, index=False)
        except (NameError, ValueError) as e:
            raise NameError(e) # for tkinter showerror
            print('Rent Error:', e)


def decormorebooks(returnbook):
    def returnmorebooks(customerid, booktitlelist):
        for booktitle in booktitlelist:
            returnbook(customerid,booktitle)
    return returnmorebooks

@decormorebooks
def returnbook(customerid,booktitle):
    bookfile = pd.read_csv(bfile)
    customerfile = pd.read_csv(cfile)
    try:
        if customerfile[customerfile['ID'] == customerid].empty:
            raise ValueError('Customer with id: {} not exist'.format(customerid))
        rfile = 'DATABASE/' + str(customerid) + '.csv'
        rentfile = pd.read_csv(rfile)
        if rentfile[rentfile['TITLE'] == booktitle].empty:
            raise NameError('Customer: "{}" never rented book with title: "{}" '.format(customerfile[customerfile['ID']==customerid]['NAME'].values[0],booktitle))
        else:
            rentbook = rentfile[rentfile['TITLE'] == booktitle]
            for bk in rentbook.values:
                if (bk[3] == 'RENTED'):
                    rentfile.loc[rentfile['ID'] == bk[0], 'RETURN'] = date.today()
                    bookfile.loc[bookfile['ID'] == bk[0], 'UPDATED'] = date.today()
                    rentfile.to_csv(rfile, index=False)
                    bookfile.to_csv(bfile, index=False)
                    return
            raise NameError('Customer: "{}" didn\'t rented book with title: "{}" '.format(customerfile[customerfile['ID'] == customerid]['NAME'].values[0], booktitle))

    except (ValueError,NameError) as e:
        raise NameError(e) # for tkinter showerror
        print('Return Error:', e)
