from tkinter import *
from tkinter.filedialog import askopenfilename
import os, os.path
from header_to_csv import header_to_csv


def set_filename():
    file = askopenfilename()
    filename.set(file)
    header_to_csv(filename)



# windows
windows = Tk()

filename = StringVar(windows)
label = Label(windows, text=filename)
label.pack

# title frame
title = LabelFrame(windows, text="Voici la liste des colonnes de votre tableau")
title.pack(fill="both", expand="yes", padx=10, pady=10)

# result
result = Label(title, text="SEE RESULTS")
result.pack()

# openButton
FILETYPES = [ ("text files", "*.csv") ]
openButton = Button(windows, text='open', command=set_filename)
openButton.pack()

# quit button 
quitButton = Button(windows)
quitButton['text'] = 'Quit'
quitButton['command'] = windows.destroy
quitButton.pack(side=RIGHT, padx=10, pady=10)

windows.mainloop




