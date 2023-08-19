import os
import tkinter
import customtkinter
from customtkinter import filedialog as fd
import time

start = time.time()


def selectDir():
    return fd.askdirectory() + '/'


def startRename(directory):
    directory1 = directory.replace('/', '\\')
    files = sorted([path for path in os.listdir(directory) if os.path.isfile(directory + path)])
    i = 0

    start = time.time()

    while files:
        file = files[0]
        ext = file.split('.')[-1]
        if not os.path.isfile(f'{directory}{i}.{ext}'):
            name = f'{i}.{ext}'
            os.rename(directory1 + file, directory1 + name)
            del files[0]
        i += 1

    end = time.time() - start

    tkinter.messagebox.showinfo(title="Информация", message=f"Время выполнения: {end} сек.")

    # labelSpeedDef = customtkinter.CTkLabel(app, text=f"Время выполнения: {end} сек.", fg_color="transparent")
    # labelSpeedDef.grid(row=1, column=1)


app = customtkinter.CTk()
app.title("PyFileName")
app.geometry('260x50')
x = (app.winfo_screenwidth() - app.winfo_reqwidth()) / 2
y = (app.winfo_screenheight() - app.winfo_reqheight()) / 2
app.wm_geometry("+%d+%d" % (x, y))
app.resizable(width=False, height=False)

end = time.time() - start

labelSpeedLoad = customtkinter.CTkLabel(app, text=f"Время загрузки: {end} сек.", fg_color="transparent")
labelSpeedLoad.grid(row=2, column=1)

b1 = customtkinter.CTkButton(master=app, text='Запустить', command=lambda: startRename(selectDir()))
b1.grid(row=0, column=1)


app.mainloop()
