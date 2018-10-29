# coding: utf-8
from tkinter.filedialog import askopenfilename
from engine.library.header import header
from engine.library.analyse import analyse



def set_filename():
    file = askopenfilename()
    filename = filename.set(file)
    print(filename)

    # result
    array = header(filename)
    results = Text(result, width=51)
    counter = 0
    for line in array[0]:
        example = array[1][counter]
        example = example[:20]
        results.insert(INSERT, line + " - ex : " + example + '\n')
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