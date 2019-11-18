
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

########################################## Other modules ##########################################

import numpy as np

import random

matplotlib.use("TkAgg") 

style.use("ggplot")

LARGE_FONT = ("Verdana", 12)

Time = []

Time_in_seconds = []

Temperatures = []

f = Figure(figsize=(5,5), dpi=100) 

a = f.add_subplot(111) # 1 by 1 and this is plot number 1

def animate(i): 

	'''Function used to create live plot of Temperature vs Time in seconds '''

	a.clear()

	a.plot(Time_in_seconds, Temperatures)

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

	 	#for F in (Startpage, PageOne, PageTwo, PageThree): #Need this if you have multiple pages you want to navigate to

	 	frame = Startpage(container, self) #Passing the frame object and the window object

	 	self.frames[Startpage] = frame

	 	frame.grid() #sticky is alighnment plus stretch

	 	self.show_frame(Startpage) #Raise StartPage initally

	 def show_frame(self, cont): #cont means controller - frame object eg. Startpage

	 	frame = self.frames[cont]

	 	frame.tkraise()

class Startpage(tk.Frame):

	def __init__(self, parent, controller): #parent is container (Frame object), controller is the master (Window object) or root

		Time_initial = datetime.now()

		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text="Graphics Window", font=LARGE_FONT)

		label.pack(pady=10,padx=10)

		button1 = ttk.Button(self, text="Generate live data", command=lambda: Startpage.generate_data())

		button1.pack()

		canvas = FigureCanvasTkAgg(f, self)

		canvas.draw()

		toolbar = NavigationToolbar2Tk(canvas, self)

		toolbar.update()

		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True) # Oriented at top, fill it all over the space you've provided with pack, expand it to any additonal whitespace

	def generate_data():

		'''Used to generate data - adds a pair of Temp, Time data per click'''

		Time.append(datetime.now())

		Time_in_seconds.append((Time[-1]-Time[0]).seconds)

		Temperatures.append(30 + random.randint(-6, 8)/10.0)
