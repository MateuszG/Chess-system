import tkinter as tk
from tkinter import *
from tkinter import ttk

def quitProgram():
    root.destroy()

root = tk.Tk()
root.withdraw()
root1 = Toplevel()
root2 = Toplevel()
root2.withdraw()
root3 = Toplevel()
root3.withdraw()

root.protocol('WM_DELETE_WINDOW', quitProgram)
root1.protocol('WM_DELETE_WINDOW', quitProgram)
root2.protocol('WM_DELETE_WINDOW', quitProgram)
root3.protocol('WM_DELETE_WINDOW', quitProgram)

root1.title("Turniej w systemie szwajcarskim - Zapisy")
root2.title("Turniej w systemie szwajcarskim - Turniej")
root3.title("Turniej w systemie szwajcarskim - Wyniki")