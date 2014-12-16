# Creates profile. Requires name, class, and server number.

from Tkinter import *
import subprocess, pickle, tkMessageBox, os

master = Tk()
MTitle = master.title("pyWartune: Create your character.")

def showChar():
	print char_var.get(), class_var.get(), server_var.get()

def saveChar():
	folder_name = 's' + str(server_var.get())
	if os.path.exists(folder_name):
		print folder_name
	else:
		os.makedirs(folder_name)

	file_name = char_var.get()+'_'+class_var.get()+'.txt'
	file_name = os.path.join(folder_name, file_name)

	char_info = {'name': char_name.get(),
	'class': class_var.get()}

	pickle.dump(char_info, open(file_name, 'w'))
	exit()

def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789':
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

text1 = Label(master, text = 'Name:')
text1.grid(row = 0, column = 0)

char_var = StringVar()
char_name = Entry(master, textvariable = char_var)
char_name.grid(row = 0, column = 1, columnspan = 3)

text2 = Label(master, text = 'Class:')
text2.grid(row = 1, column = 0)

class_var = StringVar()

b1 = Radiobutton(master, text = 'Archer', variable = class_var, value = 'Archer')
b1.grid (row = 1, column = 1)
b2 = Radiobutton(master, text = 'Knight', variable = class_var, value = 'Knight')
b2.grid (row = 1, column = 2)
b3 = Radiobutton(master, text = 'Mage', variable = class_var, value = 'Mage')
b3.grid (row = 1, column = 3)

text1 = Label(master, text = 'Server:')
text1.grid(row = 2, column = 0)

server_var = IntVar()
server_name = Entry(master, textvariable = server_var, validatecommand = validate)
server_name.grid(row = 2, column = 1, columnspan = 3)

verify = Button(master, text = "Get", command = showChar)
verify.grid()

save_it = Button(master, text = "Save", command = saveChar)
save_it.grid()

mainloop()
