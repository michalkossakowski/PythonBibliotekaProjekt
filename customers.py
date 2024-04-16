import pandas as pd
import random
from datetime import *
import os

pd.set_option('display.max_columns', None)  # unlimited columns to print
pd.set_option('display.max_rows', None)  # unlimited rows to print

cfile = 'Library/customer.csv'
afile = 'Library/address.csv'


def displaycustomers():
    """
        This function print (as string) on screen dataframe from cfile and afile
    """
    print(pd.read_csv(cfile).to_string())  # convert to string to print in one line
    print(pd.read_csv(afile).to_string())  # convert to string to print in one line
def dfcustomers(): 
    return pd.read_csv(cfile)

def dfaddress():
    return pd.read_csv(afile)

def addcustomer(name, email, phone, street, city, country):
    customerfile = pd.read_csv(cfile)
    try:
        if len(customerfile) >= 900:
            raise ValueError('Database cant hold more than 900 customers')
        if phone > 999999999 or phone <100000000:
            raise ValueError('Phone number not exist')
    except ValueError as e:
        raise ValueError(e) # for showerror tkinter
        print('Add Error:', e)
        return
    while True:
        newid = random.randint(100, 1000)
        if newid in customerfile['ID'].values:
            continue
        else:
            break
    newcustomer = {'ID': newid,
                   'NAME': name,
                   'E-MAIL': email,
                   'PHONE': phone,
                   'CREATED': date.today(),
                   'UPDATED': date.today()
                   }
    newcustomersdataframe = pd.DataFrame([newcustomer])
    newcustomersdataframe.to_csv(cfile, mode='a', header=False, index=False)

    newaddress = {'ID': newid,
                  'STREET': street,
                  'CITY': city,
                  'COUNTRY': country
                  }
    newaddressdataframe = pd.DataFrame([newaddress])
    newaddressdataframe.to_csv(afile, mode='a', header=False, index=False)

    newfiledataframe = pd.DataFrame(columns=['ID', 'TITLE', 'RENT', 'RETURN'])
    filename = 'DATABASE/' + str(newid) + '.csv'
    newfiledataframe.to_csv(filename, index=False)


def removecustomer(idorname):
    def removefolder(name):
        os.remove('DATABASE/' + str(name) + '.csv')

    oldcustomerfile = pd.read_csv(cfile)
    oldaddressfile = pd.read_csv(afile)
    try:
        if isinstance(idorname, int):
            if oldcustomerfile[oldcustomerfile['ID'] == idorname].empty:
                raise NameError('Customer with id: "{}" not exist'.format(idorname))
            else:
                customerfile = oldcustomerfile[oldcustomerfile['ID'] != idorname]
                addressfile = oldaddressfile[oldcustomerfile['ID'] != idorname]
                removefolder(idorname)
        elif isinstance(idorname, str):
            if oldcustomerfile[oldcustomerfile['NAME'] == idorname].empty:
                raise NameError('Customer with name: "{}" not exist'.format(idorname))
            else:
                customerfile = oldcustomerfile[oldcustomerfile['NAME'] != idorname]
                addressfile = oldaddressfile[oldcustomerfile['NAME'] != idorname]
                id = oldcustomerfile[oldcustomerfile['NAME']==idorname]['ID'].values[0]
                removefolder(id)
        customerfile.to_csv(cfile, index=False)
        addressfile.to_csv(afile, index=False)
    except NameError as e:
        raise NameError(e)
        print('Remove Error:', e)

def customer(fun, **kwargs):
    fun(**kwargs)
