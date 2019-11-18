
########################################## Tkinter modules ##########################################

import tkinter as tk 

from tkinter import ttk  # For more aesthetic buttons

########################################## Time/Datetime modules ##################################

import time

from datetime import datetime

########################################## Other modules ##########################################

import numpy as np

import random


LARGE_FONT = ("Verdana", 12)

class Command_window(tk.Tk): # An object of class SeaofBTCapp is also an object of class Tk, which is basiclaly a window object

	#Init is comparable to what application you want to start on booting 

	 def __init__(self, *args, **kwargs): ## args here means arguments, open ended number of parameters to be passed, ## kwargs is Keyboard arguments - passing arbitatry number of dictionaries
	 	
	 	tk.Tk.__init__(self, *args, **kwargs)

	 	tk.Tk.wm_title(self, "Command_window" )

	 	container = tk.Frame(self) #Creating the container of the window

	 	container.grid() #fill fills the entire space. expand - expands to any white space there is left

	 	container.grid_rowconfigure(0, weight=1) #0 is minimum size. weight is a priortity metric, in this case rows and columns have equal priority

	 	container.grid_columnconfigure(0, weight=1)

	 	self.frames = {}

	 	#for F in (Startpage, PageOne, PageTwo, PageThree): #Need this if you have multiple pages you want to navigate to

	 	frame = Startpage(container, self) #Passing the frame object and the window object

	 	self.frames[Startpage] = frame

	 	frame.grid(row=0,column=0,sticky="nsew") #sticky is alighnment plus stretch

	 	self.show_frame(Startpage) #Raise StartPage initally

	 def show_frame(self, cont): #cont means controller - frame object eg. Startpage

	 	frame = self.frames[cont]

	 	frame.tkraise()

class Startpage(tk.Frame):

	def __init__(self, parent, controller): #parent is container (Frame object), controller is the master (Window object) or root

		Time_initial = datetime.now()

		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text="Enter command here", font=LARGE_FONT)

		label.grid(row=0)

		self.entry = tk.Text(controller)

		self.entry.bind("<Return>", self.print_command)

		self.entry.grid(row=1)


	def print_command(self, event):

		print(self.entry.get(1.0,'end-1c'))

