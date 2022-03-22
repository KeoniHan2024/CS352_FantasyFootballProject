from tkinter import *
from tkinter import messagebox
from tracemalloc import start
from numpy import dtype
import pandas as pd
import seaborn as sns

root = Tk()
titleFont = ("Minion Pro Cond", 20)

#Labels
titleLabel = Label(root, text = 'NFL FANTASY FOOTBALL STAT TRACKER')
titleLabel.config(font=titleFont)
yearLabel = Label(root, text = 'Year')
firstNameLabel = Label(root, text = 'First Name')
lastNameLabel = Label(root, text = 'Last Name')
    
def getURL():
    url_format = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'
    yearString = year.get()
    if len(year.get()) == 0:
        messagebox.showerror("ERROR", "Year is not Entered")
        return
    elif int(yearString) >= 2022:
        messagebox.showerror("ERROR", "Year is greater than 2021")
        return
    elif int(yearString) < 1970:
        messagebox.showerror("ERROR", "Year is less than 1970")
        return

    if int(yearString):
        ##Have it format the HTMLS and get the max of every statistic

#Entries
year = Entry(root)
firstName = Entry(root)
lastName = Entry(root)
mainEntry = Text(root, height=20, width=200)
#Buttons
getInfoButton = Button(text = "Get Info", command = getURL)

def createGUI():
    #Grids
    titleLabel.grid(row = 0, column = 1, columnspan=2)
    mainEntry.grid(row=1,rowspan=3, column = 0, columnspan=5)
    yearLabel.grid(row = 4, column = 0)
    firstNameLabel.grid(row = 4, column = 2)
    lastNameLabel.grid(row = 4, column = 3)
    year.grid(row = 5, column = 0)
    firstName.grid(row = 5, column = 2)
    lastName.grid(row = 5, column = 3)
    getInfoButton.grid(row = 6, column= 3)
    root.geometry("1500x1500")

    root.mainloop()
