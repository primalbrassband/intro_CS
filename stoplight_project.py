# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 18:27:05 2025

@author: willt
"""
# traffic lights program
import tkinter as tk

# make the stoplight 
class Stop_Light:
    def __init__(self):
        # title space
        self.window = tk.Tk()
        self.window.title("Traffic light")
        self.label = tk.Label(self.window, text="Select Color")
        self.label.pack(side="bottom")
        self.canvas = tk.Canvas(self.window, width=240, height = 360,
                                bg="white")
        self.canvas.pack()
        
        # lights without light
        self.light_box = self.canvas.create_rectangle(70, 10, 165, 290, 
                                                      width=2)
        self.red_light = self.canvas.create_oval(79, 20, 155, 100, 
                                                 fill="white", width=3)
        self.yellow_light = self.canvas.create_oval(79, 110, 155, 190,
                                                    fill="white", width=3)
        self.green_light = self.canvas.create_oval(79, 200, 155, 280,
                                                   fill="white", width=3)
        
        self.var = tk.IntVar() # this will switch the light
        self.var.set(0) # lights start turned off
        
        # buttons across the bottom of the page
        self.red_light_button = tk.Radiobutton(self.window, text="Red", 
                                               variable=self.var, value=1, 
                                               command=self.update_lights)
        self.red_light_button.pack(side="left")
        self.yellow_light_button = tk.Radiobutton(self.window, text="Yellow",
                                                  variable=self.var, value=2,
                                                  command=self.update_lights)
        self.yellow_light_button.pack(side="left")
        self.green_light_button = tk.Radiobutton(self.window, text="Green",
                                                 variable=self.var, value=3,
                                                 command=self.update_lights)
        self.green_light_button.pack(side="left")
        self.off_button = tk.Radiobutton(self.window, text="Off", 
                                         variable=self.var, value=0,
                                         command=self.update_lights)
        self.off_button.pack(side="left")
        
        self.update_lights() #resets the light when user presses buttons
        
        self.window.mainloop() # cycles until user closes window
        

    def update_lights(self):
        # static state of circles should be "off"
        self.canvas.itemconfig(self.red_light, fill="white")
        self.canvas.itemconfig(self.yellow_light, fill="white")
        self.canvas.itemconfig(self.green_light, fill="white")
        
        # loop for user interaction with buttons
        if self.var.get() == 1:
            self.canvas.itemconfig(self.red_light, fill="red")
        elif self.var.get() == 2:
            self.canvas.itemconfig(self.yellow_light, fill="yellow")
        elif self.var.get() == 3:
            self.canvas.itemconfig(self.green_light, fill="green")
    
Stop_Light()