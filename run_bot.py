from Tkinter import *
from pykeyboard import PyKeyboard
import subprocess, time, sys

k = PyKeyboard()
SAVEFILE = sys.argv[1]

def altTab():
	k.press_key(k.alt_key)
	k.tap_key(k.tab_key)
	k.release_key(k.alt_key)
	time.sleep(1)

def runTown():
	listbox.insert(END, "Upgrading the town.")
	subprocess.call(['python', 'town.py', SAVEFILE])

def runAcademy():
	listbox.insert(END, "Upgrading academy skills.")
	subprocess.call(['python', 'academy.py', SAVEFILE])

def runFarm():
	listbox.insert(END, "Working the farm.")
	subprocess.call(['python', 'farm.py', SAVEFILE])

def runAstral(param):
	listbox.insert(END, "Buying astrals.")
	subprocess.call(['python', 'astral.py', SAVEFILE, param])

def runGuild(param):
	listbox.insert(END, "Supporting the guild.")
	subprocess.call(['python', 'guild.py', SAVEFILE, param])

def runReset():
	listbox.insert(END, "It's 0530 server time. Daily quests activate!")
	subprocess.call(['python', 'reset.py', SAVEFILE])	

def runCrypt(param):
	listbox.insert(END, "Running the crypt.")
	subprocess.call(['python', 'crypt.py', SAVEFILE, param])

def runCloudCity(param):
	listbox.insert(END, "Going to Cloud City.")
	subprocess.call(['python', 'cloud.py', SAVEFILE, param])

def runCampaign(dungeon, runs):
	listbox.insert(END, "Fighting PvE.")
	subprocess.call(['python', 'campaign.py', SAVEFILE, dungeon, runs])

def runWorldBoss():
	listbox.insert(END, "Fighting the world boss.")
	subprocess.call(['python', 'boss.py', SAVEFILE])

def runArena():
	listbox.insert(END, "Upgrading academy skills.")
	subprocess.call(['python', 'arena.py', SAVEFILE])

def runSylphBoss():
	listbox.insert(END, "Fighting the sylph boss.")
	subprocess.call(['python', 'atollBoss.py', SAVEFILE])

def startBot():
	global startBotID, runs

	count = "Run #" + str(runs)

	# Counts the number of runs

	listbox.insert(END, count)
	listbox.insert(END, '-------------')
	
	#This is a placeholder
	altTab()
	runTown()

	#bot logic goes here

	#increase the counter
	altTab()
	runs = runs + 1
	listbox.insert(END, '')
	startBotID = master.after(5000, startBot)

def stopBot():
	if startBotID != None:
		master.after_cancel(startBotID)

# popup window
master = Tk()
MTitle = master.title("pyWartune: Running.")

listbox = Listbox(master)
listbox.pack()

start_button = Button(master, text = "Start", command = lambda: startBot())
start_button.pack()

stop_button = Button(master, text = 'Stop', command = lambda: stopBot())
stop_button.pack()

startBotID = None
runs = 1
mainloop()

