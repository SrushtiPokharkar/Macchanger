#===================================================================
#Author: 1. Srushti Pokharkar 2. S. Subhashree
#Project: MacChanger in Python with GUI
#===================================================================

import sys
import os
import time
from Tkinter import *
from tkMessageBox import *
from tkinter import messagebox
from PIL import ImageTk, Image
import psutil
from subprocess import Popen,PIPE,STDOUT,call

root = Tk()
root.configure(background="white")

command_show = ""
command_random = ""
command_reset = ""

def interface():
	iface=variable.get()
	interface.i=iface
	interface.command_show = 'macchanger -s ' + iface
	interface.command_random = 'macchanger -r ' + iface
	interface.command_reset = 'macchanger -p ' + iface
	
def show_current():
        proc=Popen(interface.command_show, shell=True, stdout=PIPE, )
	output=proc.communicate()[0]
	messagebox.showinfo("Result", output)	 

def randomly():
	proc=Popen('ifconfig ' + interface.i + ' down', shell=True, stdout=PIPE, )
	proc=Popen(interface.command_random, shell=True, stdout=PIPE, )
	output=proc.communicate()[0]
	messagebox.showinfo("Result", output)	
	proc=Popen('ifconfig ' + interface.i + ' up', shell=True, stdout=PIPE, )
                        
def manually():            
	def Change():
		custom = E1.get()
		proc=Popen('macchanger -m '+ (custom)+ ' ' + interface.i, shell=True, 			stdout=PIPE, )
		output=proc.communicate()[0]
		messagebox.showinfo("Result", output)	
		proc=Popen('ifconfig ' + interface.i + ' up', shell=True, stdout=PIPE, )
	proc=Popen('ifconfig ' + interface.i + ' down', shell=True, stdout=PIPE, )
	L2 = Label(root, text="Enter MAC address: ")
	L2.place(x=50,y=250)
	L2.configure(bg="white")
	E1 = Entry(root,bd=2)
	E1.place(x=190,y=245)
	submit = Button(root, text="OK", fg="BLACK", command=Change)
	submit.place(x=370,y=240)


def resetMAC():     
	proc=Popen('ifconfig ' + interface.i + ' down', shell=True, stdout=PIPE, )  
	proc=Popen(interface.command_reset, shell=True, stdout=PIPE, )
	output=proc.communicate()[0]
	messagebox.showinfo("Result", output)	
	proc=Popen('ifconfig ' + interface.i + ' up', shell=True, stdout=PIPE, )  
	
#---------CODING THE GUI-----------#
imagePath = PhotoImage(file="logomc.GIF")
widgetf = Label(root, image=imagePath).pack(side="top")

L1 = Label(root, text="Choose Interface: ")
L1.configure(background="white")
L1.place(x=130,y=160)

newlist=['Select']
addrs=psutil.net_if_addrs()
mylist=(addrs.keys())
for i in range (0,len(mylist)):
	if mylist[i]!='lo':
		newlist.append(mylist[i])

OPTIONS = newlist

variable = StringVar(root)
variable.set(OPTIONS[0])

O1 = OptionMenu(root,variable, *OPTIONS)
#O1.config(fg="BLUE",fg="WHITE")
O1.place(x=250,y=153)

ifacebutton = Button(root, text="Submit", command=interface)
ifacebutton.place(x=235,y=200)

currentbutton = Button(root, text="Show current", fg="blue",command=show_current)
currentbutton.pack()
currentbutton.place(x=58, y=350, anchor="c")

randombutton = Button(root, text="Random change", fg="blue",command=randomly)
randombutton.pack()
randombutton.place(x=185, y=350, anchor="c")

customlybutton = Button(root, text="Manual change", fg="blue",command=manually)
customlybutton.pack()
customlybutton.place(x= 319, y=350, anchor="c")

resetbutton = Button(root, text="Reset MAC", fg="blue",command=resetMAC)
resetbutton.pack()
resetbutton.place(x=436, y=350, anchor="c")

root.geometry('487x380')
root.title("Tkinter GUI")
root.mainloop()
	



#--------------------------------------------------------------
#EXTRA NOTES: References - #etherpad.net/p/mit-macchanger
#--------------------------------------------------------------






