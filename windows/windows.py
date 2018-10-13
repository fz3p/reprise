from tkinter import *
from tkinter.filedialog import askopenfilename
import os, os.path

def set_filename():
    file = askopenfilename()
    file = file.name
    filename.set(file)
    print(filename)


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
openButton = Button(windows, text='open', command=set_filename)
openButton.pack()

# quit button 
quitButton = Button(windows)
quitButton['text'] = 'Quit'
quitButton['command'] = windows.destroy
quitButton.pack(side=RIGHT, padx=10, pady=10)

windows.mainloop




