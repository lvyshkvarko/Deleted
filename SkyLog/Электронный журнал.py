from tkinter import *
import getpass

root = Tk()
root.title("SkyLog | Электронный журнал")
root.geometry("1000x800")

label = Label(root, text='Добро пожаловать в систему электронного журнала, ' + getpass.getuser() + '!', font=("Arial Bold", 20), bg="lightgreen")
button = Button(root, text="Click me!", fg="red", bg="yellow")
button.pack()


label.pack()
root.mainloop()
