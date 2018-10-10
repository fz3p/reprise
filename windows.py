from tkinter import *


class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Quit'
        # Command to close the window (the destory method)
        self['command'] = parent.destroy
        self.pack(side=RIGHT, padx=10, pady=10)



# windows
windows = Tk()
#windows['bg']='white'

# title frame
title = LabelFrame(windows, text="Voici la liste des colonnes de votre tableau")
title.pack(fill="both", expand="yes", padx=10, pady=10)

# result
result = Label(title, text="SEE RESULTS")
result.pack()

quitButton(windows)

windows.mainloop




