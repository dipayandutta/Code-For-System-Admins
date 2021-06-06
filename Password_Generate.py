import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

#Password Generator Logic 
def generateLogic():
	entry.delete(0,END)

	#get the password length from the Combobox
	passLength = var1.get()
	print (passLength)
	lowerCaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
	upperCaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	numerics		  = "1234567890"
	specialChars	  = "!@#$%^&*()"
	
	
	if var.get() == 1:
		weekPassword = weekPass(lowerCaseAlphabet,numerics,passLength)
		print("Week Password -->",weekPassword)
		print(len(weekPassword))
		return weekPassword[0:passLength]

	if var.get() == 0:
		mediumPassword = mediumPass(lowerCaseAlphabet,numerics,specialChars,passLength)
		print("Medium Password -->",mediumPassword)
		print(len(mediumPassword))
		return mediumPassword[0:passLength]

	if var.get() == 3:
		strongPassword = strongPass(lowerCaseAlphabet,numerics,specialChars,upperCaseAlphabet,passLength)
		print("Strong Password -->",strongPassword)
		print(len(strongPassword))

		return strongPassword[0:passLength]

	else:
		print("Please Select The Password Length!")

'''
	function to calculate the Week Password
'''
	
def weekPass(lowerCaseAlphabet,numerics,passLength):
		password = ""
		for i in range(0,passLength):
			lowerCase = random.choice(lowerCaseAlphabet)
			digits    = random.choice(numerics)

			password += lowerCase+ digits

		return password
'''
	function to calculate the Medium Password
'''
def mediumPass(lowerCaseAlphabet,numerics,specialChars,passLength):
	password = ""
	for i in range(0,passLength):
		lowerCase = random.choice(lowerCaseAlphabet)
		digits    = random.choice(numerics)
		spChars   = random.choice(specialChars)

		password  += lowerCase+digits+spChars

	return password 

'''
	function to calculate the Strong Password
'''
def strongPass(lowerCaseAlphabet,numerics,specialChars,upperCaseAlphabet,passLength):
	password = ""
	for _ in range(0,passLength):
		lowerCase = random.choice(lowerCaseAlphabet)
		digits    = random.choice(numerics)
		spChars   = random.choice(specialChars)
		upperCase = random.choice(upperCaseAlphabet)

		password  += lowerCase+digits+spChars+upperCase

	return password
	
#Copy Function
def copyText():
	print ("Copy Clicked!" )
	toCopy = entry.get()
	pyperclip.copy(toCopy)
	

#generate Password function

def generatePassword():
	displayPassword = generateLogic()
	displayPassword = displayPassword
	print(displayPassword)
	entry.insert(10,displayPassword)

# Creat the GUI in the main() function

root = Tk()
var  = IntVar()
var1 = IntVar()	

#Window Title --> Password Generator
root.title("Password Generator")

#Create Label and Entry to show 
randomPassword = Label(root,text="Password")
randomPassword.grid(row=0)
entry = Entry(root)
entry.grid(row=0,column=1)

#create the label for length of password
cLabel = Label(root,text="Length")
cLabel.grid(row=1)

#Create the Buttons that Copy which will copy 
#password to clipboard and Generate
#Which will generate the password
copyButton = Button(root,text="Copy",command=copyText) # call the copyText function
copyButton.grid(row=0,column=2)

#generate Button
generateButton = Button(root,text='Generate',command=generatePassword) #call the generatePassword Function
generateButton.grid(row=0,column=3)

#Radio Buttons for deciding the password strength
radio_low = Radiobutton(root,text="week",variable=var,value=1)
radio_low.grid(row=1,column=2,sticky='E')

radio_middle = Radiobutton(root,text='Medium',variable=var,value=0)
radio_middle.grid(row=1,column=3,sticky='E')

radio_string = Radiobutton(root,text='Strong',variable=var,value=3)
radio_string.grid(row=1,column=4,sticky='E')

combo = Combobox(root,textvariable=var1)

#Combo Box for password length
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
			17, 18, 19, 20, 21, 22, 23, 24, 25,
			26, 27, 28, 29, 30, 31, 32, "Length")

combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1,row=1)


# GUI activation
root.mainloop()