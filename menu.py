'''
Menu.py contains all the code for running the main menu's GU-interface.
The global variables below store all the content on the main menu, whilst
all the functions stores the commands for the menu's buttons. Through
these functions we can access the library's processes.
'''

import tkinter as tk
from tkinter import *
from database import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

##Button Commands for the Menu to connect to database.py .

def innit_Output():
    BLANK="  " * 50                                                               
    for i in range(10):
        blank_lbl =Label(ResultsFrame, text=BLANK)
        blank_lbl.grid(column=0,row=i)

def OutputToMenu(Results):
    ycoord = 0
    for result in Results:
        
        Result_lbl =Label(ResultsFrame, text=result)
        Result_lbl.grid(column=0,row=ycoord)
        ycoord=ycoord+1

def SearchBook_Input():
    innit_Output()

    bookTitle=BookTitle_entry.get()
    OutputResult=Search_Book(bookTitle)
    BookTitle_entry.delete(0,len(bookTitle))

    OutputToMenu(OutputResult)

def CheckoutBook_Input():
    innit_Output()
    
    BookID=BookID_entry.get()
    MemberID=MemberID_entry.get()
    day=day_entry.get()
    month=month_entry.get()
    year=year_entry.get()
    
    OutputResults=Checkout_A_Book(BookID,MemberID,day,month,year)
    
    BookID_entry.delete(0,len(BookID))
    MemberID_entry.delete(0,len(MemberID))
    day_entry.delete(0,END)
    month_entry.delete(0,END)
    year_entry.delete(0,END)

    OutputToMenu(OutputResults)  
    
def ReturnBook_Input():
    innit_Output()
    
    BookID=BookID_entry.get()
    OutputResults=Return_A_Book(BookID)
    BookID_entry.delete(0,len(BookID))

    OutputToMenu(OutputResults)

    

def Weeding_Input():
    innit_Output()
    Database_list=DatabaseInfo()
    Logfile_list=LogFileInfo()
    
    WeedingResults=Weed_A_Book(Logfile_list,Database_list)
    print(WeedingResults[1])

    fig = Figure(figsize=(10, 4), dpi=95)
    fig.add_subplot(1,1,1).bar(WeedingResults[2], WeedingResults[1])
    fig.add_subplot(1,1,1).plot((-0.5,11.5),(5,5),'r--')
    fig.suptitle("Book Titles Checkout Count:")
    
    canvas = FigureCanvasTkAgg(fig, master=Menu)
    canvas.draw()
    canvas.get_tk_widget().place(relx = 0.4,rely = 0.1)

    x_label = Label(Menu, text="Book Titles", font ="Verdana 10 bold")
    y_label = Label(Menu, text="No.of Withdrawns ", font ="Verdana 10 bold")
    x_label.place(relx = 0.7,rely = 0.85)
    y_label.place(relx = 0.37,rely = 0.48)
    
    OutputResults=["-----WEED LIBRARY-----","Poor Condition:",
                   list(set(WeedingResults[0])),"Low Checkout Books:",
                   list(set(WeedingResults[3])),"WEED BOOKS:", WeedingResults[4]] 

    OutputToMenu(OutputResults)


## Menu configuration stored as global variables
Menu = Tk()

Menu.title("LIBRARY MANAGEMENT SYSTEM")
Menu.geometry("1500x500")

#Declaring and assigning widgets.

ResultsFrame = LabelFrame(Menu,text="OUTPUT:")
ResultsFrame.place(relx = 0.15,rely = 0.2)
Menu.pack_propagate(0)

Process_lbl = Label(Menu, text="Processes:->", font ="Verdana 10 bold")
MemberID_lbl = Label(Menu, text="Member ID:", font ="Verdana 10 bold")
BookID_lbl = Label(Menu, text="Book ID:", font ="Verdana 10 bold")

Date_lbl =Label(Menu,text="Date: (dd/mm/yyyy)", font="Verdana 10 bold")

MemberID_entry = Entry(Menu,width =15)
BookID_entry = Entry(Menu,width=15)
day_entry=Entry(Menu,width=2)
month_entry=Entry(Menu,width=2)
year_entry=Entry(Menu,width=4)

BookTitle_lbl = Label(Menu, text="Book Title:", font ="Verdana 10 bold")
BookTitle_entry = Entry(Menu,width=15)

btn_1 = Button(Menu, text="  SEARCH BOOK"  , command=SearchBook_Input)
btn_2 = Button(Menu, text="CHECKOUT BOOK", command=CheckoutBook_Input)
btn_3 = Button(Menu, text="RETURN BOOK", command=ReturnBook_Input)
btn_4 = Button(Menu, text="WEED LIBRARY", command=Weeding_Input)


#assigning positions for the widgets.

Process_lbl.place(relx = 0,rely = 0 ,anchor = 'nw')
MemberID_lbl.place(relx = 0,rely = 0.1 ,anchor = 'w')
MemberID_entry.place(relx = 0,rely = 0.15 ,anchor = 'w')
BookID_lbl.place(relx = 0,rely = 0.2 ,anchor = 'w')
BookID_entry.place(relx = 0,rely = 0.25 ,anchor = 'w')
BookTitle_lbl.place(relx = 0,rely = 0.3 ,anchor = 'w')
BookTitle_entry.place(relx = 0,rely = 0.35 ,anchor = 'w')

Date_lbl.place(relx = 0,rely = 0.4 ,anchor = 'w')

day_entry.place(relx = 0,rely = 0.45 ,anchor = 'w')
month_entry.place(relx = 0.05,rely = 0.45 ,anchor = 'w')
year_entry.place(relx = 0.1,rely = 0.45 ,anchor = 'w')

btn_1.place(relx = 0.25,rely = 0 ,anchor = 'n')
btn_2.place(relx = 0.45,rely = 0 ,anchor = 'n')
btn_3.place(relx = 0.65,rely = 0 ,anchor = 'n')
btn_4.place(relx = 0.85,rely = 0 ,anchor = 'n')


Menu.mainloop()


