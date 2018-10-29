# coding: utf-8

from tkinter import *
from library.command import set_filename
from tkinter.filedialog import askopenfilename


def choose_file():
    file_path = askopenfilename()
    paths = Text(path, width=90, height=2)
    paths.insert(INSERT, str(file_path))
    paths.pack(side=TOP, expand="no")


# windows
windows = Tk()
windows.title("Toolbox csv")
windows.geometry("900x500+300+0")
filename = StringVar(windows)
label = Label(windows, text=filename)
label.pack()

# choose file
fileselector = LabelFrame(windows)
fileselector.pack(side=TOP, fill="both", expand="no")

# Button
choosefile = Button(fileselector, text="choose file", command=choose_file)
choosefile.pack(side=LEFT)

# Path
path = LabelFrame(fileselector)
path.pack(side=TOP)


# openButton
FILETYPES = [("text files", "*.csv")]

'''
# menubar
menubar = Menu(windows)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="open", command=set_filename)
menu1.add_separator()
menu1.add_command(label="Quit", command=windows.destroy)
menubar.add_cascade(label="File", menu=menu1)
windows.config(menu=menubar)
'''

# result frame
result = LabelFrame(windows, text="Column in array")
result.pack(side=LEFT, fill="both", expand="yes", padx=10, pady=10)

# audit frame
audit = LabelFrame(windows, text="audit")
audit.pack(side=RIGHT, fill="both", expand="yes", padx=10, pady=10)




windows.mainloop()
