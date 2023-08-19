import os
from tkinter import *
from tkinter import filedialog as fd

def selectDir():
    return fd.askdirectory()+'/'

def startRename(directory):
    directory1=directory.replace('/', '\\')
    files=sorted([path for path in os.listdir(directory) if os.path.isfile(directory+path)])
    i=0

    while files:
        file=files[0]
        ext=file.split('.')[-1]
        if not os.path.isfile(f'{directory}{i}.{ext}'):
            name = f'{i}.{ext}'
            os.rename(directory1+file, directory1+name)
            del files[0]
        i+=1


root = Tk()
root.title("PyFileName")
root.geometry('50x50')

b1 = Button(text='Запустить', command=lambda: startRename(selectDir()))
b1.grid(row=0,column=1)

root.mainloop()