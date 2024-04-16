from books import *
from customers import *
from rent import *

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, showwarning
import pandas as pd

import requests
from PIL import Image, ImageTk


def maketree(tree,df):
    cleantree(tree)
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    for column in df.columns:
        tree.heading(column, text=column)
        tree.column(column)
    for id, data in df.iterrows():
        tree.insert("", "end", values=list(data))
    tree.pack()

def cleantree(tree):
    for item in tree.get_children():
        tree.delete(item)

def mainfun():
    ########################################## BOOKS ##########################################
    def openbooks():
        def addbookwindow():
            def additem():
                try:
                    if authorentry.get().strip() and titleentry.get().strip() and pagesentry.get().strip():
                        addbook(str(authorentry.get()), str(titleentry.get()), int(pagesentry.get()))
                        addbookwindow.destroy()
                        maketree(tree,dfbooks())
                    else:
                        raise ValueError('One or more fields are empty')
                except ValueError as e:
                    showerror("Add Error:", e)

            addbookwindow = Toplevel()
            addbookwindow.title("ADD BOOK")
            addbookwindow.geometry("400x90")

            addbookframe = Frame(addbookwindow)
            addbookframe.pack(side=TOP)
            # Label(addbookframe, text="ADD BOOK").grid(row=1, column=2)

            Label(addbookframe, text="AUTHOR:").grid(row=2, column=1)
            authorentry = Entry(addbookframe, fg='green')
            authorentry.grid(row=3, column=1)
            Label(addbookframe, text="TITLE:").grid(row=2, column=2)
            titleentry = Entry(addbookframe, fg='blue')
            titleentry.grid(row=3, column=2)
            Label(addbookframe, text="PAGES:").grid(row=2, column=3)
            pagesentry = Entry(addbookframe, fg='purple')
            pagesentry.grid(row=3, column=3)

            addbutton = Button(addbookframe, text="ADD", command=additem, bg='green', fg='white')
            addbutton.grid(row=4, column=1,pady=15, padx=15)
            exitbutton = Button(addbookframe, text="EXIT", command=addbookwindow.destroy, bg='red', fg='white')
            exitbutton.grid(row=4, column=3, pady=15, padx=15)
        def removebookwindow():
            def removeitem():
                try:
                    if choice.get() == 1:
                        removebook(int(idortitleentry.get()))
                    if choice.get() == 2:
                        removebook(str(idortitleentry.get()))
                    removebookwindow.destroy()
                    maketree(tree,dfbooks())
                except (NameError, ValueError) as e:
                    showerror('Remove Error:', e)

            removebookwindow = Toplevel()
            removebookwindow.title("REMOVE BOOK")
            removebookwindow.geometry("300x80")

            removebookframe = Frame(removebookwindow)
            removebookframe.pack(side=TOP)
            # Label(removebookframe, text="REMOVE BOOK").grid(row=1, column=2)

            choice = IntVar()
            choice.set(1)
            Radiobutton(removebookframe, text="ID", variable=choice, value=1).grid(row=2, column=1)
            Radiobutton(removebookframe, text="TITLE", variable=choice, value=2).grid(row=2, column=2)

            idortitleentry = Entry(removebookframe, fg='blue')
            idortitleentry.grid(row=2, column=3)

            removebutton = Button(removebookframe, text="REMOVE", command=removeitem, bg='purple', fg='white')
            removebutton.grid(row=3, column=1, pady=15, padx=15)
            exitbutton = Button(removebookframe, text="EXIT", command=removebookwindow.destroy, bg='red',fg='white')
            exitbutton.grid(row=3, column=3, pady=15, padx=15)

        def refresh():
            cleantree(tree)
            maketree(tree, dfbooks())

        bookwindow = Toplevel()

        bookwindow.title("BOOKS")
        bookwindow.geometry("1250x500")

        bookframe = Frame(bookwindow)
        bookframe.pack(side=TOP)

        Label(bookframe, text="Book options:").grid(row=1, column=1)

        addbutton = Button(bookframe, text="ADD", command=addbookwindow,bg='green', fg='white')
        addbutton.grid(row=1, column=2, pady=15, padx=15)
        removebutton = Button(bookframe, text="REMOVE", command=removebookwindow,bg='purple', fg='white')
        removebutton.grid(row=1, column=3, pady=15,padx=15)

        tree = ttk.Treeview(bookwindow, height=18)
        maketree(tree, dfbooks())
        refreshbutton = Button(bookframe, text="REFRESH", command=refresh, bg='yellow', fg='black')
        refreshbutton.grid(row=1, column=4, pady=15, padx=15)
        exitbutton = Button(bookframe, text="EXIT", command=bookwindow.destroy, bg='red', fg='white')
        exitbutton.grid(row=1, column=5, pady=15, padx=15)





    ########################################## CUSTOMERS ##########################################
    def opencustomers():
        def addcustomerwindow():
            def additem():
                try:
                    if nameentry.get().strip() and emailentry.get().strip() and phoneentry.get().strip() and streetentry.get().strip() and cityentry.get().strip() and countryentry.get().strip():
                        customer(addcustomer,name=str(nameentry.get()),email=str(emailentry.get()),phone=int(phoneentry.get()),street=str(streetentry.get()),city=str(cityentry.get()),country=str(countryentry.get()))
                        addcustomerwindow.destroy()
                        maketree(tree,dfcustomers())
                    else:
                        raise ValueError('One or more fields are empty')
                except ValueError as e:
                    showerror("Add Error:", e)

            addcustomerwindow = Toplevel()
            addcustomerwindow.title("ADD CUSTOMER")
            addcustomerwindow.geometry("800x90")

            addcustomerframe = Frame(addcustomerwindow)
            addcustomerframe.pack(side=TOP)
            # Label(addcustomerframe, text="ADD").grid(row=1, column=3)
            # Label(addcustomerframe, text="CUSTOMER").grid(row=1, column=4)

            Label(addcustomerframe, text="NAME:").grid(row=2, column=1)
            nameentry = Entry(addcustomerframe, fg='green')
            nameentry.grid(row=3, column=1)
            Label(addcustomerframe, text="E-MAIL:").grid(row=2, column=2)
            emailentry = Entry(addcustomerframe, fg='blue')
            emailentry.grid(row=3, column=2)
            Label(addcustomerframe, text="PHONE:").grid(row=2, column=3)
            phoneentry = Entry(addcustomerframe, fg='purple')
            phoneentry.grid(row=3, column=3)
            Label(addcustomerframe, text="STREET:").grid(row=2, column=4)
            streetentry = Entry(addcustomerframe, fg='red')
            streetentry.grid(row=3, column=4)
            Label(addcustomerframe, text="CITY:").grid(row=2, column=5)
            cityentry = Entry(addcustomerframe, fg='black')
            cityentry.grid(row=3, column=5)
            Label(addcustomerframe, text="COUNTRY:").grid(row=2, column=6)
            countryentry = Entry(addcustomerframe, fg='magenta')
            countryentry.grid(row=3, column=6)

            addbutton = Button(addcustomerframe, text="ADD", command=additem, bg='green', fg='white')
            addbutton.grid(row=4, column=1, pady=15, padx=15)
            exitbutton = Button(addcustomerframe, text="EXIT", command=addcustomerwindow.destroy, bg='red', fg='white')
            exitbutton.grid(row=4, column=6, pady=15, padx=15)

        def removecustomerwindow():
            def removeitem():
                try:
                    if choice.get() == 1:
                        customer(removecustomer,idorname=int(idortitleentry.get()))
                    if choice.get() == 2:
                        customer(removecustomer,idorname=str(idortitleentry.get()))
                    removecustomerwindow.destroy()
                    maketree(tree,dfcustomers())
                except (NameError, ValueError) as e:
                    showerror('Remove Error:', e)

            removecustomerwindow = Toplevel()
            removecustomerwindow.title("REMOVE CUSTOMER")
            removecustomerwindow.geometry("300x80")

            removecustomerframe = Frame(removecustomerwindow)
            removecustomerframe.pack(side=TOP)
            # Label( removecustomerframe, text="REMOVE CUSTOMER").grid(row=1, column=2)

            choice = IntVar()
            choice.set(1)
            Radiobutton( removecustomerframe, text="ID", variable=choice, value=1).grid(row=2, column=1)
            Radiobutton( removecustomerframe, text="NAME", variable=choice, value=2).grid(row=2, column=2)

            idortitleentry = Entry(removecustomerframe, fg='blue')
            idortitleentry.grid(row=2, column=3)

            removebutton = Button( removecustomerframe, text="REMOVE", command=removeitem, bg='purple', fg='white')
            removebutton.grid(row=3, column=1, pady=15, padx=15)
            exitbutton = Button( removecustomerframe, text="EXIT", command= removecustomerwindow.destroy, bg='red', fg='white')
            exitbutton.grid(row=3, column=3, pady=15, padx=15)

        def addresswindow():

            addresswindow = Toplevel()
            addresswindow.title("CUSTOMER ADDRESS")
            addresswindow.geometry("850x500")

            adressframe = Frame(addresswindow)
            adressframe.pack(side=TOP)
            Label(adressframe, text="Address options:").grid(row=1, column=1)
            exitbutton = Button(adressframe, text="EXIT", command=addresswindow.destroy, bg='red', fg='white')
            exitbutton.grid(row=1, column=2, pady=15, padx=15)
            tree = ttk.Treeview(addresswindow, height=18)
            maketree(tree,dfaddress())


        customerwindow = Toplevel()
        customerwindow.title("CUSTOMERS")
        customerwindow.geometry("1250x500")

        customerframe = Frame(customerwindow)
        customerframe.pack(side=TOP)

        Label(customerframe, text="Customer options:").grid(row=1, column=1)

        addbutton = Button(customerframe, text="ADD", command=addcustomerwindow,fg='white',bg='green')
        addbutton.grid(row=1, column=2, pady=15, padx=15)
        removebutton = Button(customerframe, text="REMOVE", command=removecustomerwindow,fg='white',bg='purple')
        removebutton.grid(row=1, column=3, pady=15,padx=15)
        adressbutton = Button(customerframe, text="ADRESS", command=addresswindow, bg='orange', fg='white')
        adressbutton.grid(row=1, column=4, pady=15, padx=15)
        exitbutton = Button(customerframe, text="EXIT", command=customerwindow.destroy, bg='red', fg='white')
        exitbutton.grid(row=1, column=5, pady=15, padx=15)
        tree = ttk.Treeview(customerwindow, height=18)
        maketree(tree,dfcustomers())



    ########################################## RENT ##########################################
    def openrent():

        def rentbookwindow():
            def rentitem():
                try:
                    if choice.get()==1:
                        rentbook(int(idoption.get()),str(titleentry.get()))
                        rentbookwindow.destroy()
                    elif choice.get()==2:
                        titles = str(titlesbox.get('1.0',END))
                        titleslist=titles.splitlines()
                        for tt in titleslist:
                            rentbook(int(idoption.get()), tt)
                        rentbookwindow.destroy()
                except NameError as e:
                    showerror('Rent Error:', e)

            rentbookwindow = Toplevel()
            rentbookwindow.title("RENT BOOK")
            rentbookwindow.geometry("420x140")

            rentbookframe = Frame(rentbookwindow)
            rentbookframe.pack(side=TOP)
            # Label(rentbookframe, text="RENT BOOK").grid(row=1, column=1)

            Label(rentbookframe, text="CUSTOMER ID:").grid(row=2, column=1)
            # identry = Entry(rentbookframe, fg='purple')
            # identry.grid(row=3, column=1)
            customerfile = pd.read_csv(cfile)
            idlist = customerfile['ID'].values
            idoption = IntVar(rentbookframe)
            idoption.set(idlist[0])  # default value
            optionmenu = OptionMenu(rentbookframe, idoption, *idlist)
            optionmenu.grid(row=3,column=1)

            choice = IntVar()
            choice.set(1)
            Radiobutton(rentbookframe, text="BOOK TITLE:", variable=choice, value=1).grid(row=2, column=2)
            Radiobutton(rentbookframe, text="BOOKS TITLES:", variable=choice, value=2).grid(row=2, column=3)

            # Label(rentbookframe, text="BOOK TITLE:").grid(row=2, column=2)
            titleentry = Entry(rentbookframe, fg='magenta')
            titleentry.grid(row=3, column=2)

            titlesbox = Text(rentbookframe, fg='purple',width=17,height=3)
            titlesbox.grid(row=3, column=3,padx=5)

            rentitembutton = Button(rentbookframe, text="RENT", command=rentitem, bg='green', fg='white')
            rentitembutton.grid(row=4, column=1, pady=15, padx=15)
            exitbutton = Button(rentbookframe, text="EXIT", command=rentbookwindow.destroy, bg='red', fg='white')
            exitbutton.grid(row=4, column=3, pady=15, padx=15)

        def returnbookwindow():
            def returnitem():
                try:
                    if choice.get()==1:
                        returnbook(int(idoption.get()), [str(titleentry.get())])
                        returnbookwindow.destroy()
                    if choice.get()==2:
                        titles = str(titlesbox.get('1.0', END))
                        titleslist = titles.splitlines()
                        returnbook(int(idoption.get()),titleslist)
                        returnbookwindow.destroy()

                except NameError as e:
                    showerror('Return Error:', e)

            returnbookwindow = Toplevel()
            returnbookwindow.title("RETURN BOOK")
            returnbookwindow.geometry("420x140")

            returnbookframe = Frame(returnbookwindow)
            returnbookframe.pack(side=TOP)
            # Label(returnbookframe, text="RETURN BOOK").grid(row=1, column=1)

            Label(returnbookframe, text="CUSTOMER ID:").grid(row=2, column=1)
            # identry = Entry(returnbookframe, fg='purple')
            # identry.grid(row=3, column=1)
            customerfile = pd.read_csv(cfile)
            idlist = customerfile['ID'].values
            idoption = IntVar(returnbookframe)
            idoption.set(idlist[0])  # default value
            optionmenu = OptionMenu(returnbookframe, idoption, *idlist)
            optionmenu.grid(row=3,column=1)

            choice = IntVar()
            choice.set(1)
            Radiobutton(returnbookframe, text="BOOK TITLE:", variable=choice, value=1).grid(row=2, column=2)
            Radiobutton(returnbookframe, text="BOOKS TITLES:", variable=choice, value=2).grid(row=2, column=3)

            # Label(rentbookframe, text="BOOK TITLE:").grid(row=2, column=2)
            titleentry = Entry(returnbookframe, fg='magenta')
            titleentry.grid(row=3, column=2)

            titlesbox = Text(returnbookframe, fg='purple',width=17,height=3)
            titlesbox.grid(row=3, column=3,padx=5)

            rentitembutton = Button(returnbookframe, text="RETURN", command=returnitem, bg='blue', fg='white')
            rentitembutton.grid(row=4, column=1, pady=15, padx=15)
            exitbutton = Button(returnbookframe, text="EXIT", command=returnbookwindow.destroy, bg='red', fg='white')
            exitbutton.grid(row=4, column=3, pady=15, padx=15)
        def showcustomercard():


            def show():
                try:
                    customerfile = pd.read_csv(cfile)
                    if customerfile[customerfile['ID'] == int(idoption.get())].empty:
                        raise ValueError('Customer with id: {} not exist'.format(int(idoption.get())))
                    rfile = 'DATABASE/' + str(idoption.get()) + '.csv'
                    maketree(tree,pd.read_csv(rfile))

                except (ValueError,FileNotFoundError) as e:
                    showerror('Show Error:',e)

            showcardwindow = Toplevel()

            showcardwindow.title("SHOW CUSTOMER CARD")
            showcardwindow.geometry("900x500")

            showcardframe = Frame(showcardwindow)
            showcardframe.pack(side=TOP)

            Label(showcardframe, text="CUSTOMER ID:").grid(row=1, column=1)
            # identry = Entry(showcardframe, fg='purple')
            # identry.grid(row=1, column=2)
            rentbookbutton = Button(showcardframe, text="SHOW", command=show, bg='green', fg='white')
            rentbookbutton.grid(row=1, column=3, pady=15, padx=15)
            exitbutton = Button( showcardframe, text="EXIT", command=showcardwindow.destroy, bg='red', fg='white')
            exitbutton.grid(row=1, column=4, pady=15, padx=15)
            tree = ttk.Treeview(showcardwindow, height=18)

            customerfile = pd.read_csv(cfile)
            idlist = customerfile['ID'].values
            idoption = IntVar(showcardframe)
            idoption.set(idlist[0])  # default value
            optionmenu = OptionMenu(showcardframe, idoption, *idlist)
            optionmenu.grid(row=1,column=2)


        rentwindow = Toplevel()

        rentwindow.title("RENT")
        rentwindow.geometry("550x75")

        rentframe = Frame(rentwindow)
        rentframe.pack(side=TOP)

        Label(rentframe, text="Options:").grid(row=1, column=1)
        rentbookbutton = Button(rentframe, text="RENT BOOK", command=rentbookwindow, bg='green', fg='white')
        rentbookbutton.grid(row=1, column=2, pady=15, padx=15)
        returnbookbutton = Button(rentframe, text="RETURN BOOK", command=returnbookwindow, bg='blue', fg='white')
        returnbookbutton.grid(row=1, column=3, pady=15, padx=15)
        showcardbutton = Button(rentframe, text="SHOW CUSTOMER CARD", command=showcustomercard, bg='magenta', fg='white')
        showcardbutton.grid(row=1, column=4, pady=15, padx=15)
        exitbutton = Button(rentframe, text="EXIT", command=rentwindow.destroy, bg='red', fg='white')
        exitbutton.grid(row=1,column=5,pady=15,padx=15)

    ########################################## MENU ##########################################
    menuwindow = Tk()
    menuwindow.title("LIBRARY")
    menuwindow.geometry("400x140")

    menuframe = Frame(menuwindow)
    menuframe.pack(side=TOP)

    Label(menuframe, text="Select option:").grid(row=1, column=2)
    bookbutton = Button(menuframe, text="   BOOKS   ", command=openbooks,fg='purple',borderwidth=8)
    bookbutton.grid(row=2, column=1, pady=5, padx=5,ipadx=15,ipady=3)
    customerbutton = Button(menuframe, text="CUSTOMERS", command=opencustomers,fg='green',borderwidth=8)
    customerbutton.grid(row=2, column=2, pady=5, padx=5,ipadx=10,ipady=3)
    rentbutton = Button(menuframe, text="RENT/RETRUN", command=openrent, fg='blue',borderwidth=8)
    rentbutton.grid(row=2, column=3, pady=5, padx=5,ipadx=5,ipady=3)
    exitbutton = Button(menuframe, text="EXIT", command=menuwindow.destroy, bg='red', fg='white',borderwidth=8)
    exitbutton.grid(row=3, column=2,pady=5, padx=5,ipadx=5,ipady=1)

    menuwindow.mainloop()


########################################## MAIN ##########################################
if __name__ == '__main__':
    mainfun()
