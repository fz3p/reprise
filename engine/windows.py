# coding: utf-8

from tkinter import *
from tkinter.filedialog import askopenfilename
from library.header import header
from library.analyse import analyse


def choose_file():
    one_file = askopenfilename()
    print(one_file)


def set_filename():
    file = askopenfilename()
    filename.set(file)

    # result
    array = header(filename)
    results = Text(result, width=51)
    counter = 0
    for line in array[0]:
        example = array[1][counter]
        example = example[:20]
        results.insert(INSERT, line + " - ex : " + example +'\n')
        counter = counter + 1
    results.pack()
    
    # audit
    audit_array = analyse(filename)
    audits = Text(audit, width=51)
    counter = 0
    for line in audit_array:
        audits.insert(INSERT, str(counter) + ' - ' + line + '\n')
        counter = counter + 1
    audits.pack()
    
        
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
choosefile = Button(fileselector, text="choose file", command=choose_file)
choosefile.pack(side=LEFT)
pathfile = Text(fileselector)

# openButton
FILETYPES = [("text files", "*.csv")]

# menubar
menubar = Menu(windows)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="open", command=set_filename)
menu1.add_separator()
menu1.add_command(label="Quit", command=windows.destroy)
menubar.add_cascade(label="File", menu=menu1)
windows.config(menu=menubar)

# result frame
result = LabelFrame(windows, text="Column in array")
result.pack(side=LEFT, fill="both", expand="yes", padx=10, pady=10)

# audit frame
audit = LabelFrame(windows, text="audit")
audit.pack(side=RIGHT, fill="both", expand="yes", padx=10, pady=10)


windows.mainloop()
