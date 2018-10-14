from tkinter import *
from tkinter.filedialog import askopenfilename
import os, os.path
from header_to_csv import header_to_csv


def set_filename():
    file = askopenfilename()
    filename.set(file)
    array = header_to_csv(filename)
    results = Text(title)
    for line in array:
        results.insert(INSERT, line+'\n')
        results.pack()
    
        
# windows
windows = Tk()
windows.title("header of csv")
windows.geometry("300x500+300+0")
filename = StringVar(windows)
label = Label(windows, text=filename)
label.pack

# openButton
FILETYPES = [ ("text files", "*.csv") ]

# menubar
menubar = Menu(windows)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="open", command=set_filename)
menu1.add_separator()
menu1.add_command(label="Quit", command=windows.destroy)
menubar.add_cascade(label="File", menu=menu1)
windows.config(menu=menubar)

# title frame
title = LabelFrame(windows, text="Column in array")
title.pack(fill="both", expand="yes", padx=10, pady=10)


windows.mainloop

