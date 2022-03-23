from tkinter import *
from tkinter import messagebox
from tracemalloc import start
from turtle import down
from numpy import dtype
import pandas as pd
import seaborn as sns
import os

root = Tk()
titleFont = ("Minion Pro Cond", 20)

#Labels
titleLabel = Label(root, text = 'NFL FANTASY FOOTBALL STAT TRACKER')
titleLabel.config(font=titleFont)
yearLabel = Label(root, text = 'Year')
nameLabel = Label(root, text = 'Player Name')
    
def getURL():
    url_template = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'
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

    #Foramts the URL with the correct year in it
    url= url_template.format(yearString)
    html = pd.read_html(url, header = 0)
    dfCurrent = html[0]

    #cleans Data by removing the headers by finding where Age text occurs
    rawData = dfCurrent.drop(dfCurrent[dfCurrent.Age == 'Age'].index)
    df = rawData.fillna(0)  #Fills the empty/NA frames with 0
    
    #Removes the columns ORB AND DRB (offensive and defensive Rebounds)
    df = df.drop(['ORB'], axis = 1)
    df = df.drop(['DRB'], axis = 1)
    df = df.drop(['GS'], axis = 1)
    df = df.drop(['FTA'], axis = 1)
    pd.set_option('display.max_rows', None)
    mainEntry.insert(END,df)

    #Reads it to a csv file named by year and reads it
    fileName = 'NBA{}Stats'
    dataFolderPath = os.path.join(os.getcwd(), "Data_Sheets")
    df.to_csv(os.path.join(dataFolderPath,fileName.format(yearString)), index = False)
    #df = pd.read_csv(dataFolderPath, fileName.format(year))
    

#Entries
year = Entry(root)
name = Entry(root)
mainEntry = Text(root, height=50, width=200)
#Buttons
downloadDataButton = Button(text = "Download Data", command = getURL)

def createGUI():
    #Grids
    titleLabel.grid(row = 0, column = 0, columnspan=3)
    mainEntry.grid(row=1,rowspan=3, column = 0, columnspan=5)
    yearLabel.grid(row = 4, column = 0)
    nameLabel.grid(row = 4, column = 2)
    year.grid(row = 5, column = 0)
    name.grid(row = 5, column = 2)
    downloadDataButton.grid(row = 6, column= 0)
    root.geometry("1500x1500")
    root.mainloop()
