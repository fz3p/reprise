# coding: utf-8

from tkinter import *
from tkinter.filedialog import askopenfilename
from library.header import header
from library.analyse import analyse


def choose_file():
    global paths
    global file_path
    file_path = askopenfilename()
    paths = Text(path, width=90, height=1)
    paths.insert(INSERT, str(file_path))
    paths.pack(side=TOP, expand="yes")


def execute_treatement():
    global results
    global audits
    # header
    array = header(file_path)
    results = Text(result, width=51)
    counter = 0
    for line in array[0]:
        example = array[1][counter]
        example = example[:20]
        results.insert(INSERT, line + " - ex : " + example + '\n')
        counter = counter + 1
    results.pack()

    # audit
    audit_array = analyse(file_path)
    audits = Text(audit, width=51)
    counter = 0
    for line in audit_array:
        audits.insert(INSERT, str(counter) + ' - ' + line + '\n')
        counter = counter + 1
    audits.pack()


def reset_all_frame():
    paths.destroy()
    audits.destroy()
    results.destroy()


# windows
windows = Tk()
windows.title("Toolbox csv")
windows.geometry("900x550+300+0")
filename = StringVar(windows)
label = Label(windows, text=filename)
label.pack()

# menubar
menubar = Menu(windows)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Quit", command=windows.destroy)
menubar.add_cascade(label="File", menu=menu1)
windows.config(menu=menubar)

# frame launcher
fileselector = Frame(windows)
fileselector.pack(side=TOP, fill="both", expand="no")

# Button choosefile
choosefile = Button(fileselector, text="choose file", command=choose_file)
choosefile.pack(side=LEFT, padx=10, pady=10)

# Path file
path = LabelFrame(fileselector)
path.pack(side=RIGHT, padx=5)

# Button launch
execute = Button(fileselector, text="execute", command=execute_treatement)
execute.pack(side=LEFT, padx=10, pady=10)

# openButton
FILETYPES = [("text files", "*.csv")]

# all results
all_result = Frame(windows)
all_result.pack()

# result frame
result = LabelFrame(all_result, text="Column in array")
result.pack(side=LEFT, fill="both", expand="yes", padx=10, pady=10)

# audit frame
audit = LabelFrame(all_result, text="audit")
audit.pack(side=RIGHT, fill="both", expand="yes", padx=10, pady=10)

# Reset frame
reset_frame = Frame(windows)
reset_frame.pack(side=BOTTOM, fill="both")

# Reset button
reset = Button(reset_frame, text="reset", command=reset_all_frame)
reset.pack(side=RIGHT, padx=10, pady=10)

windows.mainloop()
