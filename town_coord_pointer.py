from Tkinter import *
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import subprocess, pickle, tkMessageBox, sys, os

#"/path/to/savefile_town_coords.txt" 
SAVEFILE = sys.argv[1]
NEW_DIC = pickle.load(open(SAVEFILE, 'r'))

SAVEFILE_PATH = SAVEFILE[0:-4] + '_coords/town.txt'


if os.path.isfile(SAVEFILE_PATH) == False:
	NEW_DIC = ''
else:
	NEW_DIC = pickle.load(open(SAVEFILE_PATH, 'r'))

m = PyMouse()
k = PyKeyboard()

master = Tk()
MTitle = master.title("pyWartune: Town Coordinates")
master.minsize(250, 100)
master.maxsize(600, 800)

class Row(object):
	def __init__(self, building, row_num, save_name, save_name_upgrade):
		self.label = Label(master, text = str(building))
		self.label.grid(row = row_num, column = 0)

		self.x_text = StringVar()
		if type(NEW_DIC) == str:
			self.x_coord = ''
		else:
			self.x_coord = NEW_DIC[save_name][0]

		self.x_text.set('x = ' + str(self.x_coord))
		self.x = Label(master, textvariable = self.x_text)
		self.x.grid(row = row_num, column = 1)

		self.y_text = StringVar()
		if type(NEW_DIC) == str:
			self.y_coord = ''
		else:
			self.y_coord = NEW_DIC[save_name][1]

		self.y_text.set('y = ' + str(self.y_coord))
		self.y = Label(master, textvariable = self.y_text)
		self.y.grid(row = row_num, column = 2)

		self.button = Button(master, text="Get", 
			command=lambda: self.getCoord(self.x_text, self.y_text))
		self.button.grid(row = row_num, column = 3)

		self.label = Label(master, text = "Upgrade")
		self.label.grid(row = row_num, column = 4)

		self.x_upgrade_text = StringVar()
		if type(NEW_DIC) == str:
			self.x_upgrade_coord = ''
		else:
			self.x_upgrade_coord = NEW_DIC[save_name][0]

		self.x_upgrade_text.set('x = ' + str(self.x_upgrade_coord))
		self.x_upgrade = Label(master, textvariable = self.x_upgrade_text)
		self.x_upgrade.grid(row = row_num, column = 5)

		self.y_upgrade_text = StringVar()
		if type(NEW_DIC) == str:
			self.y_upgrade_coord = ''
		else:
			self.y_upgrade_coord = NEW_DIC[save_name][1]

		self.y_upgrade_text.set('y = ' + str(self.y_upgrade_coord))
		self.y_upgrade = Label(master, textvariable = self.y_upgrade_text)
		self.y_upgrade.grid(row = row_num, column = 6)

		self.button = Button(master, text="Get", 
			command=lambda: self.getUpgradeCoord(self.x_upgrade_text, self.y_upgrade_text))
		self.button.grid(row = row_num, column = 7)

	def getCoord(self, a, b):
		tkMessageBox.showinfo("Collecting coordinates.", "Hover over the item,\nthen press ENTER.")
		x_mouse, y_mouse = m.position()
		self.x_coord = x_mouse
		self.y_coord = y_mouse
		a.set('x = ' + str(self.x_coord))
		b.set('y = ' + str(self.y_coord))

	def getUpgradeCoord(self, a, b):
		tkMessageBox.showinfo("Collecting coordinates.", "Hover over the item,\nthen press ENTER.")
		x_mouse, y_mouse = m.position()
		self.x_upgrade_coord = x_mouse
		self.y_upgrade_coord = y_mouse
		a.set('x = ' + str(self.x_upgrade_coord))
		b.set('y = ' + str(self.y_upgrade_coord))

	def click(self, var):
		m.press(var[0], var[1])
		self.shortSleep()
		m.release(var[0], var[1])
		self.shortSleep()

# END OBJECTS

def saveCoords():
	coords = {'townHall': (townHall.x_coord, townHall.y_coord),
	'townHallUpgrade': (townHall.x_upgrade_coord, townHall.y_upgrade_coord),
	'barracks': (barracks.x_coord, barracks.y_coord),
	'barracksUpgrade': (barracks.x_upgrade_coord, barracks.y_upgrade_coord),
	'cottage': (cottage.x_coord, cottage.y_coord),
	'cottageUpgrade': (cottage.x_upgrade_coord, cottage.y_upgrade_coord),
	'warehouse': (warehouse.x_coord, warehouse.y_coord),
	'warehouseUpgrade': (warehouse.x_upgrade_coord, warehouse.y_upgrade_coord),
	'academy': (academy.x_coord, academy.y_coord),
	'academyUpgrade': (academy.x_upgrade_coord, academy.y_upgrade_coord),
	'refinery': (refinery.x_coord, refinery.y_coord),
	'refineryUpgrade': (refinery.x_upgrade_coord, refinery.y_upgrade_coord),
	}

	file_name = SAVEFILE_PATH
	if not os.path.exists(SAVEFILE_PATH):
		fileObject = open(file_name, 'w')
	else:
		fileObject = open(file_name, 'r + a')
	pickle.dump(coords, fileObject)
	fileObject.close



#BEGIN SETTING ROWS

townHall = Row('Town Hall', 0, 'townHall', 'townHallUpgrade')
barracks = Row('Barracks', 1, 'barracks', 'barracksUpgrade')
cottage = Row('Cottage', 2, 'cottage', 'cottageUpgrade')
warehouse = Row('Warehouse', 3, 'warehouse', 'warehouseUpgrade')
academy = Row('Academy', 4, 'academy', 'academyUpgrade')
refinery = Row('Refinery', 5, 'refinery', 'refineryUpgrade')

save_button = Button(master, text="Save", command=saveCoords)
save_button.grid(row = 6, column = 2, columnspan = 3)

mainloop()
