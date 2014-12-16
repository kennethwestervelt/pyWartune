# Initial menu screen.  Creates or loads profile. Allows profile to be edited or ran.

from Tkinter import *
import subprocess, pickle, tkMessageBox, tkFileDialog

LOADED = ''

master = Tk()
MTitle = master.title("pyWartune: An MMO bot.")

def createBot():
	#subprocess.call(['python', 'create_bot.py'])
	pass

def loadBot():
	global LOADED
	LOADED = tkFileDialog.askopenfilename()

	if len(str(LOADED)) > 0:
		file_data = ''

		#WILL UNCOMMENT THIS BLOCK WHEN CREATEBOT.PY IS READY
		#import_dic = open(LOADED, 'r')
		#file_data = str(import_dic['name']) + " - " + str(import_dic['server'])

		file_name_filled = StringVar(master, file_data) 
		file_name = Label(master, textvariable = file_name_filled)
		file_name.grid(row = 2, columnspan = 4)

		edit = Button(master, text = "Edit", command = editBot)
		edit.grid(row = 3, column = 2)

		run_it = Button(master, text = "Run", command = lambda: runBot)
		run_it.grid(row = 3, column = 3)

def editBot():
	location = Button(master, text = "Locations", command = editLocation)
	location.grid(row = 4, column = 0, columnspan = 2)

	preferences = Button(master, text = "Preferences", command = editPreferences)
	preferences.grid(row = 4, column = 2, columnspan = 2)

def runBot():
#	subprocess.call(['python', 'run_bot.py', LOADED])
	pass

def editLocation():
#	subprocess.call(['python', 'location.py', LOADED])
	pass

def editPreferences():
#	subprocess.call(['python', 'preferences.py', LOADED])
	pass
	
splash = Label(master, text = "pyWartune\n A Wartune bot\n")
splash.grid(row = 0, column = 0, columnspan = 4)

create = Button(master, text = "Create Bot", command = createBot)
create.grid(row = 1, column = 0, columnspan = 2)

load_it = Button(master, text = "Load Bot", command = loadBot)
load_it.grid(row = 1, column = 2, columnspan = 2)






mainloop()
