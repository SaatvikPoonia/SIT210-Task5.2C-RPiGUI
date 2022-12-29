from tkinter import *   #Library That used to build graphical user interface
from gpiozero import LED  #library that used to ininitalise gpio pins
import RPi.GPIO

# Initialisation of leds
led1 = LED(11)
led2 = LED(10)
led3 = LED(9)


root = Tk()  #root is the variable for gui that used to access functions of tkinter

root.geometry("300x400")   # it will open 400x400 window for gui

root.configure(bg="white")   # it will set the background of gui

label2 = Label(root, text=" Which Led you want to Blink? ")   # it used to write text on gui
label2.pack(pady=30)   # pack is variable to display thisngs 

#condition for red
def red():
   if led1.is_lit:  #if led is off  
      selection = "red is off"  # than display red is off
      label.config(text = selection)
      led1.off()     #it will set the light status off
   else:
      selection = "red is on"  #else it will display red is on
      label.config(text = selection)
      led1.on()
      #light status off
      led2.off()
      led3.off()

#condition for yellow

def blue():
   if led2.is_lit:
      selection = "blue is off"
      label.config(text = selection)
      led2.off()
   else:
      selection = "blue is on"
      label.config(text = selection)
      led2.on()
      led1.off()
      led3.off()

#condition for green

def green():
   if led3.is_lit:
      selection = "green is off"
      label.config(text = selection)
      led3.off()
   else:
      selection = "green is on"
      label.config(text = selection)
      led3.on()
      led1.off()
      led2.off()

def close():
    RPi.GPIO.cleanup()
    root.destroy()
    
button1 = Radiobutton( text="Red", foreground="white", background="red" ,command=red) 
# making radio button 
button1.pack(pady=20) 
#it will display radio button and pady provide some padding space to the button


button2 = Radiobutton( text="Blue",foreground="white", background="blue",command=blue)
button2.pack(pady=20)

button3 = Radiobutton( text="Green", foreground="white", background="green",command=green)
button3.pack(pady=20)

label = Label(root)
label.pack(pady=20)

exit_button = Button(root, text="Exit", command= close) 
exit_button.pack(pady=20)

root.mainloop()
# it is an infinite loop that used to run application for infinite time