
########################################## Tkinter modules ##########################################

import tkinter as tk 

from tkinter import ttk  # For more aesthetic buttons

########################################## Time/Datetime modules ##################################

import time

from datetime import datetime

########################################## Other modules ##########################################

import numpy as np

import random

import serial


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

	 	frame.grid_rowconfigure(0, weight=1)
	 	frame.grid_columnconfigure(0, weight=1)

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

		self.running_text_output = True

		self.controller = controller

		self.input_label = tk.Label(self, text="Enter command here", font=LARGE_FONT, height=5, width=30)

		self.input_label.grid(row=0, column=0)

		self.input_text = tk.Text(controller, height=2, width=30, borderwidth=2,relief='solid')

		self.input_text.bind("<Return>", self.send_command)

		self.input_text.bind("<Delete>", self.delete_output)

		self.input_text.grid(row=0, column=0)

		self.output_label = tk.Label(self, text="Output", font=LARGE_FONT, height=4, width=30)

		self.output_label.grid(row=2,  column=0)

		self.output_text = tk.Text(controller, height=2, width=30, borderwidth=2,relief='solid')

		self.output_text.grid(row=2,  column=0)

	def print_command(self, event):

		self.output_text.insert(tk.END,self.input_text.get(1.0,'end-1c'))

	def delete_output(self, event):

		self.output_text.delete('1.0', tk.END)

	def send_command(self, event):

		self.running_text_output = False

		ser = serial.Serial('/dev/ttyUSB0',9600,timeout=3)

		ser.write(self.input_text.get(1.0,'end-1c').encode())

		self.running_text_output = True

		self.print_output(self.controller)

	def print_output(self, controller):

		if self.running_text_output == True:

			ser = serial.Serial('/dev/ttyUSB0',9600,timeout=3)

			Output_strings = ser.readline().decode()

			self.output_text.insert(tk.END,Output_strings)

			controller.after(1000, self.print_output, controller)		
