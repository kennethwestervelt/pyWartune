# Initial menu screen.  Creates or loads profile. Allows profile to be edited or ran.

from Tkinter import *
import subprocess, pickle, tkMessageBox, os

master = Tk()
MTitle = master.title("pyWartune: An MMO bot.")
master.minsize(600, 800)
master.maxsize(600, 800)

mainloop()
