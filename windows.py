from tkinter import *

# windows
windows = Tk()

# title frame
title = LabelFrame(windows, text="Voici la liste des colonnes de votre tableau")
title.pack(fill="both", expand="yes", padx=10, pady=10)

# result
result = Label(title, text="SEE RESULTS")
result.pack()

# quit button 
quitButton = Button(windows)
quitButton['text'] = 'Quit'
quitButton['command'] = windows.destroy
quitButton.pack(side=RIGHT, padx=10, pady=10)

windows.mainloop




