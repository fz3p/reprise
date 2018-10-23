from tkinter import *
from tkinter.filedialog import askopenfilename
import os, os.path
from library.control_csv.header import *
from library.control_csv.analysis import *

def set_filename():
    file = askopenfilename()
    filename.set(file)

    # result
    array = header(filename)
    results = Text(result)
    counter = 0
    for line in array[0]:
        results.insert(INSERT, line + " ex : " + array[1][counter]+'\n')
        results.pack()
        counter = counter + 1
    
    # audit
    audit_array = analyse(filename)
    audits = Text(audit)
    counter = 0
    for line in audit_array:
        audits.insert(INSERT,'column : '+ str(counter)+': ' + line +'\n')
        audits.pack()
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

# result frame
result = LabelFrame(windows, text="Column in array")
result.pack(fill="both", expand="yes", padx=10, pady=10)

# audit frame
audit = LabelFrame(windows, text="audit")
audit.pack(fill="both", expand="yes", padx=10, pady=10)


windows.mainloop()
