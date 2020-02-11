
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

Time_SC = []

Time_in_seconds_SC = []

Time_in_minutes_SC = []

Temperatures_SC = []

LARGE_FONT = ("Verdana", 12)

f_SC = Figure(figsize=(5,5), dpi=100) 

a_SC = f_SC.add_subplot(111) # 1 by 1 and this is plot number 1

ser = serial.Serial('/dev/ttyUSB0',9600,timeout=3)

def animate_SC(i): 

	'''Function used to create live plot of Temperature vs Time in seconds '''

	a_SC.clear()

	a_SC.plot(Time_in_minutes_SC, Temperatures_SC)


class SC_temperature(tk.Frame):

	def __init__(self, parent, controller): #parent is container, controller is the master 

		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="Sample Chamber Temperature", font=LARGE_FONT)

		label.pack(pady=10,padx=10)

		button1 = ttk.Button(self, text="Back to home", command=lambda: controller.show_frame(Startpage.Startpage))

		button1.pack()

		button2 = ttk.Button(self, text="Plot live data", command=lambda: plot_live_SC_data(controller, True, False))

		button2.pack()

		button3 = ttk.Button(self, text="Reset", command=lambda: reset_SC_data(controller))

		button3.pack()

		button4 = ttk.Button(self, text="Stop plotting", command=lambda: stop_plotting_SC(controller))

		button4.pack()

		button5 = ttk.Button(self, text="Resume plotting", command=lambda: resume_plotting_SC(controller))

		button5.pack()

		button6 = ttk.Button(self, text="log data", command=lambda: log_SC_data(controller))

		button6.pack()

		canvas = FigureCanvasTkAgg(f_SC, self)

		canvas.draw()

		toolbar = NavigationToolbar2Tk(canvas, self)

		toolbar.update()

		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True) # Oriented at top, fill it all over the space you've provided with pack, expand it to any additonal whitespace

def plot_live_SC_data(controller, start, log): 

	global running_SC

	if start == True: #start is only true when plot live data is triggered

		running_SC = True

		global Time_SC, Time_in_seconds_SC, Temperatures_SC, Time_in_minutes_SC

		Time_SC = []

		Time_in_seconds_SC = []

		Temperatures_SC = []

		Time_in_minutes_SC = []

	if running_SC == True:

		ser.reset_input_buffer()

		ser.reset_output_buffer()

		ser.write('g-SC_T1\n'.encode())

		Output_strings = ser.readline().decode()

		Split_strings = Output_strings.split('---')

		Time_SC_temp = Split_strings[1].split('\r')[0]

		Time_SC.append(datetime.strptime(Time_SC_temp, '%Y-%m-%d %H:%M:%S.%f'))

		Time_in_seconds_SC_temp = (Time_SC[-1]-Time_SC[0]).seconds

		Time_in_seconds_SC.append(Time_in_seconds_SC_temp)

		Time_in_minutes_SC_temp = Time_in_seconds_SC_temp/60.0

		Time_in_minutes_SC.append(Time_in_minutes_SC_temp)

		Temperatures_SC_temp = float(Split_strings[0])

		Temperatures_SC.append(Temperatures_SC_temp)

		controller.after(1000, plot_live_SC_data, controller, False, False)		

def stop_plotting_SC(controller):

	global running_SC 

	running_SC = False

def resume_plotting_SC(controller):

	global running_SC 

	running_SC = True

	plot_live_SC_data(controller, False, False)

def reset_SC_data(controller):

	global Time_SC, Time_in_seconds_SC, Temperatures_SC, running_SC

	Time_SC = []

	Time_in_seconds_SC = []

	Temperatures_SC = []

	running_SC = False

def log_SC_data(controller):

	ser.write('g-SC_P\n'.encode())

	P =	(ser.readline().decode()).split('\r')[0].split('---')[0]

	ser.write('g-SC_I\n'.encode())

	I =	(ser.readline().decode()).split('\r')[0].split('---')[0]

	ser.write('g-SC_D\n'.encode())

	D =	(ser.readline().decode()).split('\r')[0].split('---')[0]

	print('Logging started')

	file = open('Data_SC_'+str(Time_SC[0])+'.csv','w+')

	file.write('P='+str(P)+' I='+str(I) +' D='+str(D)+'\n')

	file.write('Time,Temperature\n')

	for i in range(len(Time_SC)):
		file.write(str(Time_SC[i]) +','+str(Temperatures_SC[i]))
		file.write('\n')

	file.close()

	print('Logging finished')
