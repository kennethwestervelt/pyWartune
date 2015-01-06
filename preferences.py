# preferences

from Tkinter import *
import sys, os, pickle, tkMessageBox, tkFileDialog, subprocess

SAVEFILE = sys.argv[1]
LOADED = pickle.load(open(SAVEFILE, 'r'))

master = Tk()
MTitle = master.title("pyWartune - Preferences.")


class BaseRow(object):
	def __init__ (self, rank, name, server):
		dump_it = 'Server ' + str(server) + ' - ' + rank + ' ' + name
		title_var = StringVar()
		title_var.set(dump_it)
		title = Label(master, textvariable = title_var)
		title.grid(columnspan = 3)

class ButtonRow(BaseRow):
	def __init__ (self, row_num, title):
		self.label = Label(master, text = str(title))
		self.label.grid(row = row_num, column = 0)

		self.button = Button(master, text="Get Coords", 
			command=lambda: self.callIt(title))
		self.button.grid(row = row_num, column = 1)

	def callIt(self, title):
		title_doc = title.lower() + '_coord_pointer.py'
		subprocess.call(['python', title_doc, SAVEFILE])
		

# header

header = BaseRow(LOADED['class'], LOADED['name'], LOADED['server'])

# character level (criteria to be determined later) (checkboxes? input? dropdown?)

# town preferences

town = ButtonRow(2, 'Town')

# # farm preferences

# farm = ButtonRow(3, 'Farm')

# # guild preferences

# guild = ButtonRow(4, 'Guild')

# # sylph preferences

# sylph = ButtonRow(5, 'Sylph')

# # minigame preferences

# minigame = ButtonRow(6, 'Minigames')

print LOADED 

mainloop()
