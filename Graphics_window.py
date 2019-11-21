
########################################## Tkinter modules ##########################################

import tkinter as tk 

from tkinter import ttk # For more aesthetic buttons

########################################## Matplotlib modules ##########################################

import matplotlib 

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from matplotlib.figure import Figure

import matplotlib.animation as animation

from matplotlib import style

########################################## Time/Datetime modules ##################################

import time

from datetime import datetime

########################################## Other Pages ##########################################

import Startpage

import DPGT_graphics_page

import SCT_graphics_page

import CCT_graphics_page

########################################## Other modules ##########################################

import numpy as np

import random

import serial


#ser = serial.Serial('/dev/tty.usbserial-FTY3UOSS',9600,timeout=3)

matplotlib.use("TkAgg") 

style.use("ggplot")

LARGE_FONT = ("Verdana", 12)

class Graphics_window(tk.Tk): # An object of class Graphics_window is also an object of class Tk, which is basiclaly a window object

	#Init is comparable to what application you want to start on booting 

	 def __init__(self, *args, **kwargs): ## args here means arguments, open ended number of parameters to be passed, ## kwargs is Keyboard arguments - passing arbitatry number of dictionaries
	 	
	 	tk.Tk.__init__(self, *args, **kwargs)

	 	tk.Tk.wm_title(self, "Graphics_window" )

	 	container = tk.Frame(self) #Creating the container of the window

	 	container.pack(side="top", fill="both", expand=True) #fill fills the entire space. expand - expands to any white space there is left

	 	container.grid_rowconfigure(0, weight=1) #0 is minimum size. weight is a priortity metric, in this case rows and columns have equal priority

	 	container.grid_columnconfigure(0, weight=1)

	 	self.frames = {}

	 	for F in (Startpage.Startpage, DPGT_graphics_page.DPG_temperature, SCT_graphics_page.SC_temperature, CCT_graphics_page.CC_temperature):

	 	    frame = F(container, self) #Passing the frame object and the window object

	 	    self.frames[F] = frame

	 	    frame.grid(row=0, column=0, sticky="nsew") #sticky is alighnment plus stretch

	 	self.show_frame(Startpage.Startpage) #Raise StartPage initally

	 def show_frame(self, cont): #cont means controller - frame object eg. Startpage

	 	frame = self.frames[cont]

	 	frame.tkraise()
