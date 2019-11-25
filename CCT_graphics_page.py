
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

import Startpage

import numpy as np

import random

import serial

matplotlib.use("TkAgg") 

style.use("ggplot")

LARGE_FONT = ("Verdana", 12)

Time_CC = []

Time_in_seconds_CC = []

Time_in_minutes_CC = []

Temperatures_CC = []

LARGE_FONT = ("Verdana", 12)

f_CC = Figure(figsize=(5,5), dpi=100) 

a_CC = f_CC.add_subplot(111) # 1 by 1 and this is plot number 1

ser = serial.Serial('/dev/ttyUSB0',9600,timeout=3)

def animate_CC(i): 

	'''Function used to create live plot of Temperature vs Time in seconds '''

	a_CC.clear()

	a_CC.plot(Time_in_minutes_CC, Temperatures_CC)


class CC_temperature(tk.Frame):

	def __init__(self, parent, controller): #parent is container, controller is the master 

		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="Sample Chamber Temperature", font=LARGE_FONT)

		label.pack(pady=10,padx=10)

		button1 = ttk.Button(self, text="Back to home", command=lambda: controller.show_frame(Startpage.Startpage))

		button1.pack()

		button2 = ttk.Button(self, text="Plot live data", command=lambda: plot_live_CC_data(controller, True, False))

		button2.pack()

		button3 = ttk.Button(self, text="Reset", command=lambda: reset_CC_data(controller))

		button3.pack()

		button4 = ttk.Button(self, text="Stop plotting", command=lambda: stop_plotting_CC(controller))

		button4.pack()

		button5 = ttk.Button(self, text="Resume plotting", command=lambda: resume_plotting_CC(controller))

		button5.pack()

		button6 = ttk.Button(self, text="log data", command=lambda: log_CC_data(controller))

		button6.pack()

		canvas = FigureCanvasTkAgg(f_CC, self)

		canvas.draw()

		toolbar = NavigationToolbar2Tk(canvas, self)

		toolbar.update()

		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True) # Oriented at top, fill it all over the space you've provided with pack, expand it to any additonal whitespace

def plot_live_CC_data(controller, start, log): 

	global running_CC

	if start == True: #start is only true when plot live data is triggered

		running_CC = True

		global Time_CC, Time_in_seconds_CC, Temperatures_CC, Time_in_minutes_CC

		Time_CC = []

		Time_in_seconds_CC = []

		Temperatures_CC = []

		Time_in_minutes_CC = []

	if running_CC == True:

		ser.reset_input_buffer()

		ser.reset_output_buffer()

		ser.write('g-CC_T1\n'.encode())

		Output_strings = ser.readline().decode()

		Split_strings = Output_strings.split('---')

		Time_CC_temp = Split_strings[1].split('\r')[0]

		Time_CC.append(datetime.strptime(Time_CC_temp, '%Y-%m-%d %H:%M:%S'))

		Time_in_seconds_CC_temp = (Time_CC[-1]-Time_CC[0]).seconds

		Time_in_seconds_CC.append(Time_in_seconds_CC_temp)

		Time_in_minutes_CC.append(Time_in_minutes_CC_temp)

		Time_in_minutes_CC_temp = (Time_CC[-1]-Time_CC[0]).minutes

		Temperatures_CC_temp = float(Split_strings[0])

		Temperatures_CC.append(Temperatures_CC_temp)

		controller.after(1000, plot_live_CC_data, controller, False, False)		

def stop_plotting_CC(controller):

	global running_CC 

	running_CC = False

def resume_plotting_CC(controller):

	global running_CC 

	running_CC = True

	plot_live_CC_data(controller, False, False)

def reset_CC_data(controller):

	global Time_CC, Time_in_seconds_CC, Temperatures_CC, running_CC

	Time_CC = []

	Time_in_seconds_CC = []

	Temperatures_CC = []

	running_CC = False

def log_CC_data(controller):

	print('Logging started')

	file = open('Data_CC.csv','w+')

	file.write('Time,Time in seconds,Temperature')

	for i in range(len(Time_CC)):
		file.write(str(Time_CC[i]) +','+str(Time_in_seconds_CC[i])+','+str(Temperatures_CC[i]))
		file.write('\n')

	file.close()

	print('Logging finished')
