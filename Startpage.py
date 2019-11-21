
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

import DPGT_graphics_page

import SCT_graphics_page

import CCT_graphics_page

########################################## Other modules ##########################################

import numpy as np

import random

import serial


matplotlib.use("TkAgg") 

style.use("ggplot")

LARGE_FONT = ("Verdana", 12)

class Startpage(tk.Frame):

	def __init__(self, parent, controller): #parent is container (Frame object), controller is the master (Window object) or root		

		Time_initial = datetime.now()

		tk.Frame.__init__(self, parent)

		label = ttk.Label(self, text="Graphics Window", font=LARGE_FONT)

		label.pack(pady=10,padx=10)

		button1 = ttk.Button(self, text="Plot DPG temperature", command=lambda: controller.show_frame(DPGT_graphics_page.DPG_temperature))

		button1.pack()

		button2 = ttk.Button(self, text="Plot SC temperature", command=lambda: controller.show_frame(SCT_graphics_page.SC_temperature))

		button2.pack()

		button3 = ttk.Button(self, text="Plot CC temperature", command=lambda: controller.show_frame(CCT_graphics_page.CC_temperature))

		button3.pack()