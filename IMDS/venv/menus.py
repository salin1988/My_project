from tkinter import Menu
from tkinter import messagebox as mb
import sys

menus = { 'Tools'   : { ('IMDS Journal Difference','imds_jounal_difference'),
                        ('IMDS vs NXT Book Comparator','imds_nxt_book_comparator'),
                        ('Exit','Exit')
                      },
          'Servers' : { ('gqimdsinit01','gqimdsinit01_server'),
                        ('lqimdsinit01','lqimdsinit01_server')
                        },
          'Help' : { ('About','About') }
        }

msg_about = " IMDS tools \n Version 1.0"

def Exit():
    sys.exit(0)

def About():
    mb.showinfo('About', msg_about)

def imds_jounal_difference():
    mb.showinfo('imds_jounal_difference', 'Not Implemented')

def imds_nxt_book_comparator():
    mb.showinfo('imds_nxt_book_comparator', 'Not Implemented')

def gqimdsinit01_server():
    mb.showinfo('gqimdsinit01_server', 'Not Implemented')

def lqimdsinit01_server():
    mb.showinfo('lqimdsinit01_server', 'Not Implemented')

def addMenus(root):
    menu = Menu(root)
    root.config(menu=menu)

    for name, details in menus.items():
        nameMenu = Menu(menu)
        menu.add_cascade(label=name, menu=nameMenu)

        for item,command in details:
            nameMenu.add_command(label=item,command=eval(command))