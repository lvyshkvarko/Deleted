from tkinter import *
import getpass
from tkinter import filedialog as fd
import time
name = False


root = Tk()
root.title("SkyConverter | Конвертор файловых форматов")
root.geometry("1000x800")
root["bg"] = "gray22"

greeting = Label(root, text='Добро пожаловать, ' + getpass.getuser() + '!', font=("Arial Bold", 20), bg="lightgreen")
greeting.pack()

status = Label(root, text='Статус: ', font=("Arial Bold", 20), bg="#FFFF99")
status.place(x=0, y=100)

status_expectation = Label(root, text='Ожидание загрузки файла', font=("Arial Bold", 20), bg="#FF9999")
status_expectation.place(x=110, y=100)

def callback():
    name = fd.askopenfilename() # выбор файла
    name = fd.asksaveasfile(defaultextension=".txt") # сохранение файла
    # будет убарана закачка из tkinter. Вместо него, будет модуль os, который меняет тип файла по кнопке и сохраняет результат в отдельной папке
    print(name)
    name = True
    print('Файл выбран')
    if name == True:
        print('Файл загружен в ' + time.strftime("%H:%M:%S", time.localtime()))
        status_expectation = Label(root, text='Файл загружен [' + time.strftime("%H:%M:%S", time.localtime()) + ']', font=("Arial Bold", 20), bg="#CCFFFF")
        status_expectation.place(x=450, y=100)

button = Button(root, text="Загрузить файл", font=("Arial Bold", 20), bg="lightgreen", command=callback)
button.place(relx=0.5, rely=0.5, anchor="c")

root.mainloop()