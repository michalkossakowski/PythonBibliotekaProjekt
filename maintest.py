from books import *
from customers import *
from rent import *
from tkinter import *

def mainfun():
    print('--------------------- fun from __main__ ---------------------')

    ##books test
    #addbook('Sanah', 'Marcepan', '2115')
    #addbook('Eminem', 'Rap God', '888')
    #removebook('Marcepan')
    #removebook(371)
    #displaybooks()

    ##customers test
    #addcustomer('Cristiano Ronaldo','ronaldo@gmail.com','999888777','Bernabeu','Madrid','Spain')
    #removecustomer('Cristiano Ronaldo')
    #removecustomer(479)
    #displaycustomers()
    #customer(addcustomer,name='Cristiano Ronaldo',email='ronaldo@gmail.com',phone=999888777,street='Bernabeu',city='Madrid',country='Spain')
    #customer(removecustomer,idorname='Cristiano Ronaldo')
    #customer(removecustomer,idorname=721)

    ##rent test
    #rentbook(416,'Skyfall','Melodia')
    #returnbook(416,['Skyfall','Melodia'])
    #returnbook(416,['Melodia'])

if __name__ == '__main__':
    mainfun()

