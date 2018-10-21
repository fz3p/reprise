from tkinter import *
from tkinter.filedialog import askopenfilename
import os, os.path
from library.control_csv.header_to_csv import header_to_csv
from library.convert_csv.sheets_to_csv import *

def set_filename():
    file = askopenfilename()
    filename.set(file)
    array = header_to_csv(filename)
    results = Text(title)
    counter = 0
    for line in array[0]:
        results.insert(INSERT, line + " ex : " + array[1][counter]+'\n')
        results.pack()
        counter = counter + 1
    
        
# windows
windows = Tk()
windows.title("Toolbox csv")
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
