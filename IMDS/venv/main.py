import tkinter as tk
from tkinter import Menu
from menus import *

## Main
root = tk.Tk()
root.geometry("1000x500+30+30")

logo = tk.PhotoImage(file='/Users/skdb/Desktop/imds.png')
p = tk.Label(root, image=logo, justify=tk.CENTER, pady=150).pack()

addMenus(root)
from tkinter import Menu
root.mainloop()