import numpy as np
import cv2
import Tkinter as tk
from PIL import Image, ImageTk
from Tkinter import *

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Digital Microscope")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames

capLeft = cv2.VideoCapture(0)
capRight = cv2.VideoCapture(1)

def show_frame():
    ret, frameLeft = capLeft.read()
    frameLeft = cv2.flip(frameLeft, 1)
    cv2imageLeft = cv2.cvtColor(frameLeft, cv2.COLOR_BGR2RGBA)
    ret, frameRight = capRight.read()
    frameRight = cv2.flip(frameRight, 1)
    cv2imageRight = cv2.cvtColor(frameRight, cv2.COLOR_BGR2RGBA)
    imgLeft = Image.fromarray(cv2imageLeft)
    imgRight = Image.fromarray(cv2imageRight)
    imgtkl = ImageTk.PhotoImage(image=imgLeft)
    imgtkr = ImageTk.PhotoImage(image=imgRight)
    displayLeft.imgtkl = imgtkl  # Shows frame for display 1
    displayLeft.configure(image=imgtkl)
    displayRight.imgtkr = imgtkr  # Shows frame for display 2
    displayRight.configure(image=imgtkr)
    window.after(10, show_frame)

displayLeft = tk.Label(imageFrame)
displayLeft.grid(row=0, column=1, padx=10, pady=2)  #Display 1
displayRight = tk.Label(imageFrame)
displayRight.grid(row=0, column=0) #Display 2

#Slider window (slider controls stage position)
sliderFrame = tk.Frame(window, width=600, height=100)
sliderFrame.grid(row = 0, column=600, padx=2, pady=10)

show_frame() #Display
window.mainloop()  #Starts GUI