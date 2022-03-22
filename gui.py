from tkinter import *
from tkinter import messagebox
from tracemalloc import start
import pandas as pd
import seaborn as sns

root = Tk()
titleFont = ("Minion Pro Cond", 20)

#Labels
titleLabel = Label(root, text = 'NFL FANTASY FOOTBALL STAT TRACKER')
titleLabel.config(font=titleFont)
startYearLabel = Label(root, text = 'Start Year')
endYearLabel = Label(root, text = 'End Year')
firstNameLabel = Label(root, text = 'First Name')
lastNameLabel = Label(root, text = 'Last Name')
    
def getURL():
    url_format = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'
    startString = startYear.get()
    endString = endYear.get()
    if len(startYear.get()) == 0 or len(endYear.get()) == 0:
        messagebox.showerror("ERROR", "One or both years are not entered")
        return
    elif int(endString) >= 2022:
        messagebox.showerror("ERROR", "Ending year is greater than 2021")
        return
    elif int(startString) < 1950:
        messagebox.showerror("ERROR", "Starting year is less than 1950")
        return
    elif len(startString) == 0:
        messagebox.showerror("ERROR", "One or both years are entered")
        return

    if int(startString) == int(endString):
        # Creates the URL into a string with given year and reads it
        url = url_format.format(startString)
        table = pd.read_html(url, header = 0)
        #Gets rid of headers
        df = table[0]
        df[df.Age == 'Age']
        df = df.drop(df[df.Age == 'Age'].index)
        print(df)
        sns.displot(data = df.PTS)
        
    else:
        years = list(range(int(startString),int(endString) + 1))
        for year in years:
            url = url_format.format(year)
            table = pd.read_html(url, header = 0)
            #Gets rid of headers
            df = table[0]
            df[df.Age == 'Age']
            df = df.drop(df[df.Age == 'Age'].index)
            print(table)
            sns.displot(df.PTS)

#Entries
startYear = Entry(root)
endYear = Entry(root)
firstName = Entry(root)
lastName = Entry(root)
mainEntry = Text(root)
#Buttons
getInfoButton = Button(text = "Get Info", command = getURL)


def createGUI():
    #Grids
    titleLabel.grid(row = 0, column = 1, columnspan=2)
    mainEntry.grid(row=1,rowspan=3, column = 0, columnspan=4)
    startYearLabel.grid(row = 4, column = 0)
    endYearLabel.grid(row = 4, column = 1)
    firstNameLabel.grid(row = 4, column = 2)
    lastNameLabel.grid(row = 4, column = 3)
    startYear.grid(row = 5, column = 0)
    endYear.grid(row = 5, column = 1)
    firstName.grid(row = 5, column = 2)
    lastName.grid(row = 5, column = 3)
    getInfoButton.grid(row = 6, column= 3)
    root.geometry("1000x1000")

    root.mainloop()
