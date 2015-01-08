from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time, random, pickle, sys, tkMessageBox

if __name__ == '__main__':
    tkMessageBox.showerror("WRONG ENTRY", "You should run\nlaunch.py")
    exit()

m = PyMouse()
k = PyKeyboard()
SAVEFILE = sys.argv[1]
SAVEFILE_PATH = SAVEFILE[0:-4] + '_coords/town.txt'
NEW_DIC = pickle.load(open(SAVEFILE_PATH, 'r'))

# All actions are either mouseclicks or keypresses. Some actions are time-dependent and require a cooldown.

class Clickable(object):

	def __init__(self, x, y):
		self.coord = (x, y)

	def click(self, var):
		m.press(var[0], var[1])
		time.sleep(.1)
		m.release(var[0], var[1])
		time.sleep(.25)

	def unselect(self):
		k.tap_key(k.escape_key)
		time.sleep(.5)
		

class HotKey(object):

	filler = "This is a wrapper class for now."

class BottomBarHotKey(HotKey):

	troops = 'a'
	inventory = 'b'
	friends = 'f'
	skills = 's'
	blacksmith = 't'
	shop = 'o'
	guild = 'g'
	Wilds = 'q'
	City = 'q'

class Building(Clickable):
	filler = "This is a wrapper class for now."

	def select(self):
		self.click(self.coord)

class UpgradeBuilding(Building):

	def __init__(self, click_it, upgrade_it):
		self.coord = click_it
		self.upgrade_coord = upgrade_it

	def upgrade(self):
		self.click(self.upgrade_coord)

	def all_actions(self):
		self.select()
		self.upgrade()
		self.unselect()
		
# NOTE: Create town hall levy function given time and time_zone.

if NEW_DIC['barracks'][0] and NEW_DIC['barracksUpgrade'][0] != '':
	barracks = UpgradeBuilding(NEW_DIC['barracks'], NEW_DIC['barracksUpgrade'])
	barracks.all_actions()
	time.sleep(1)
if NEW_DIC['townHall'][0] and NEW_DIC['townHallUpgrade'][0] != '':
	townhall = UpgradeBuilding(NEW_DIC['townHall'], NEW_DIC['townHallUpgrade'])
	townhall.all_actions()
	time.sleep(1)
if NEW_DIC['refinery'][0] and NEW_DIC['refineryUpgrade'][0] != '':
	refinery = UpgradeBuilding(NEW_DIC['refinery'], NEW_DIC['refineryUpgrade'])
	refinery.all_actions()
 	time.sleep(1)
if NEW_DIC['academy'][0] and NEW_DIC['academyUpgrade'][0] != '':
	academy = UpgradeBuilding(NEW_DIC['academy'], NEW_DIC['academyUpgrade'])
	academy.all_actions()
	time.sleep(1)
if NEW_DIC['cottage'][0] and NEW_DIC['cottageUpgrade'][0] != '':
	cottage = UpgradeBuilding(NEW_DIC['cottage'], NEW_DIC['cottageUpgrade'])
	cottage.all_actions()
	time.sleep(1)
if NEW_DIC['warehouse'][0] and NEW_DIC['warehouseUpgrade'][0] != '':
	warehouse = UpgradeBuilding(NEW_DIC['warehouse'], NEW_DIC['warehouseUpgrade'])
	warehouse.all_actions()
	time.sleep(1)
