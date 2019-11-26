
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

Time_DPG = []

Time_in_seconds_DPG = []

Temperatures_DPG = []

LARGE_FONT = ("Verdana", 12)

f_DPG = Figure(figsize=(5,5), dpi=100) 

a_DPG = f_DPG.add_subplot(111) # 1 by 1 and this is plot number 1

ser = serial.Serial('/dev/ttyUSB0',9600,timeout=3)

def animate_DPG(i): 

	'''Function used to create live plot of Temperature vs Time in seconds '''

	a_DPG.clear()

	a_DPG.plot(Time_in_seconds_DPG, Temperatures_DPG)


class DPG_temperature(tk.Frame):

	def __init__(self, parent, controller): #parent is container, controller is the master 

		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="Dew Point Generator Temperature", font=LARGE_FONT)

		label.pack(pady=10,padx=10)

		button1 = ttk.Button(self, text="Back to home", command=lambda: controller.show_frame(Startpage))

		button1.pack()

		button2 = ttk.Button(self, text="Plot live data", command=lambda: plot_live_DPG_data(controller, True, False))

		button2.pack()

		button3 = ttk.Button(self, text="Reset", command=lambda: reset_DPG_data(controller))

		button3.pack()

		button4 = ttk.Button(self, text="Stop plotting", command=lambda: stop_plotting_DPG(controller))

		button4.pack()

		button5 = ttk.Button(self, text="Resume plotting", command=lambda: resume_plotting_DPG(controller))

		button5.pack()

		button6 = ttk.Button(self, text="log data", command=lambda: log_DPG_data(controller))

		button6.pack()

		canvas = FigureCanvasTkAgg(f_DPG, self)

		canvas.draw()

		toolbar = NavigationToolbar2Tk(canvas, self)

		toolbar.update()

		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True) # Oriented at top, fill it all over the space you've provided with pack, expand it to any additonal whitespace

def plot_live_DPG_data(controller, start, log): 

	global running_DPG

	if start == True: #start is only true when plot live data is triggered

		running_DPG = True

		global Time_DPG, Time_in_seconds_DPG, Temperatures_DPG

		Time_DPG = []

		Time_in_seconds_DPG = []

		Temperatures_DPG = []

	if running_DPG == True:

		ser.reset_input_buffer()

		ser.reset_output_buffer()

		ser.write('g-DPG_T1\n'.encode())

		Output_strings = ser.readline().decode()

		#print(Output_strings)

		Split_strings = Output_strings.split('---')

		Time_DPG_temp = Split_strings[1].split('\r')[0]

		Time_DPG.append(datetime.strptime(Time_DPG_temp, '%Y-%m-%d %H:%M:%S'))

		Time_in_seconds_DPG_temp = (Time_DPG[-1]-Time_DPG[0]).seconds

		Time_in_seconds_DPG.append(Time_in_seconds_DPG_temp)

		Temperatures_DPG_temp = float(Split_strings[0])

		Temperatures_DPG.append(Temperatures_DPG_temp)

		controller.after(1000, plot_live_DPG_data, controller, False, False)		

def stop_plotting_DPG(controller):

	global running_DPG 

	running_DPG = False

def resume_plotting_DPG(controller):

	global running_DPG 

	running_DPG = True

	plot_live_DPG_data(controller, False, False)

def reset_DPG_data(controller):

	global Time_DPG, Time_in_seconds_DPG, Temperatures_DPG, running_DPG

	Time_DPG = []

	Time_in_seconds_DPG = []

	Temperatures_DPG = []

	running_DPG = False

def log_DPG_data(controller):

	print('Logging started')

	ser.write('g-DPG_P'.encode())

	P =	(ser.readline().decode()).split('\r')[0].split('---')[0]

	ser.write('g-DPG_I'.encode())

	I =	(ser.readline().decode()).split('\r')[0].split('---')[0]

	ser.write('g-DPG_D'.encode())

	D =	(ser.readline().decode()).split('\r')[0].split('---')[0]

	print('Logging started')

	file = open('Data_DPG_'+Time_DPG[0]+'.csv','w+')

	file.write('P='+str(P)+' I='+str(I) +'D='+str(D)+'\n')

	file.write('Time,Time in seconds,Temperature\n')

	for i in range(len(Time_DPG)):
		file.write(str(Time_DPG[i]) +','+str(Time_in_seconds_DPG[i])+','+str(Temperatures_DPG[i]))
		file.write('\n')

	file.close()

	print('Logging finished')
