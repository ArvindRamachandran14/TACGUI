import tkinter as tk 

import Graphics_window 

import Command_window

import matplotlib.animation as animation

import DPGT_graphics_page

import SCT_graphics_page

import CCT_graphics_page


LARGE_FONT = ("Verdana", 12)

class TAC_GUI(tk.Tk): # An object of class TAC_GUI is also an object of class Tk, which is basiclaly a window object

	#Init is comparable to what application you want to start on booting 

	 def __init__(self, *args, **kwargs): ## args here means arguments, open ended number of parameters to be passed, ## kwargs is Keyboard arguments - passing arbitatry number of dictionaries
	 	
	 	tk.Tk.__init__(self, *args, **kwargs)

	 	tk.Tk.wm_title(self, "TAC GUI" )

	 	container = tk.Frame(self) #Creating the container or the frame of the window

	 	container.grid() #fill fills the entire space. expand - expands to any white space there is left

	 	container.grid_rowconfigure(0, weight=1) #0 is minimum size. weight is a priortity metric, in this case rows and columns have equal priority

	 	container.grid_columnconfigure(0, weight=1)

	 	self.frames = {}

	 	#for F in (Startpage, PageOne, PageTwo):

	 	frame = Startpage(container, self) #Passing the frame object and the window object

	 	self.frames[Startpage] = frame

	 	frame.grid(row=0,column=0,sticky="nesw") #sticky is alighnment plus stretch

	 	frame.grid_rowconfigure(0, weight=1)
	 	frame.grid_columnconfigure(0, weight=1)

	 	self.show_frame(Startpage) #Raise StartPage initally

	 def show_frame(self, cont): #cont means controller - eg. Startpage

	 	frame = self.frames[cont]

	 	frame.tkraise()

class Startpage(tk.Frame): #Only one page for the main window for right now

	def __init__(self, parent, controller): #parent is container, controller is the master 

		tk.Frame.__init__(self, parent)

		label = tk.Label(self, text="TACUI Application", font=LARGE_FONT)

		label.grid(row=0)

		button1 = tk.Button(self, text="Open Command Window", command=open_command_window)

		button1.grid(row=2)

		button2 = tk.Button(self, text="Open Graphics Window", command=open_graphics_window)

		button2.grid(row=3)

def open_graphics_window():

	graphic_window_app = Graphics_window.Graphics_window()

	graphic_window_app.geometry("500x500+720+100")

	ani_DPG = animation.FuncAnimation(DPGT_graphics_page.f_DPG, DPGT_graphics_page.animate_DPG, interval=1000)

	ani_SC = animation.FuncAnimation(SCT_graphics_page.f_SC, SCT_graphics_page.animate_SC, interval=1000)

	ani_CC = animation.FuncAnimation(CCT_graphics_page.f_CC, CCT_graphics_page.animate_CC, interval=1000)

	graphic_window_app.mainloop()

def open_command_window():

	command_window_app = Command_window.Command_window()

	command_window_app.geometry("600x200+100+500")

	command_window_app.grid_rowconfigure(0, weight=1)

	command_window_app.grid_columnconfigure(0, weight=1)

	command_window_app.mainloop()

main_app = TAC_GUI() 

main_app.geometry("500x100+200+300") # Window is 500 x 100 in size, 400 pixels to the right and 300 pixels down from the top left corner of the screen

main_app.grid_rowconfigure(0, weight=1)

main_app.grid_columnconfigure(0, weight=1)

main_app.mainloop() 