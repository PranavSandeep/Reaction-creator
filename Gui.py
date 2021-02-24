import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.title('Azure')

window_height = 530
window_width = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

style = ttk.Style(root)
root.tk.call('source', 'azure dark.tcl')
style.theme_use('azure')

button = Button(root, text="DELET", command=root.destroy)

button.pack()

root.mainloop()
