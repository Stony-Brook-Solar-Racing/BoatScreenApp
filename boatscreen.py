import tkinter
import numpy as np
from PIL import Image, ImageTk
import cv2
import os
from util import database
from util import calculations
import subprocess
import signal

screen=tkinter.Tk()
screen.title("Solar Boat Screen")
screen.geometry("1000x600")

frame=np.random.randint(0,255,[100,100,3],dtype='uint8')
img = ImageTk.PhotoImage(Image.fromarray(frame))

img_label=tkinter.Label(screen) #,image=img)
img_label.grid(row=0,column=0,columnspan=3,pady=1,padx=10)

speed_label = tkinter.Label(screen, text='Speed: 0 Knots')
speed_label.grid(row=2, column=1, pady=1, padx=10)

voltage_label = tkinter.Label(screen, text='State of Charge: 0%')
voltage_label.grid(row=3, column=1, pady=1, padx=10)

power_label = tkinter.Label(screen, text='Power: 0')
power_label.grid(row=4, column=1, pady=1, padx=10)


global cam
reading = True

p = subprocess.Popen(["python3", "readsensor.py"])

def camera():
    global frame
    global cam
    cam = cv2.VideoCapture(0)
    #cv2.namedWindow("Experience_in_AI camera")
    while True:
        ret, frame = cam.read()
        scanning()
        #Update the image to tkinter...
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        resize = cv2.resize(frame, (600,400))
        img_update = ImageTk.PhotoImage(Image.fromarray(resize)) # frame inside changing to resize
        img_label.configure(image=img_update)
        img_label.image=img_update
        img_label.update()

        if not ret:
            print("failed to grab frame")
            break

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")

            cam.release()
            cv2.destroyAllWindows()
            break

def stop_camera():
    global cam
    cam.release()
    cv2.destroyAllWindows()
    print("Stopped!")

def click_start_sensor():
    global reading
    global p
    if not reading:
        os.kill(p.pid, signal.SIGCONT)
        reading = True

def click_stop_sensor():
    global reading
    global p
    if reading:
        os.kill(p.pid, signal.SIGSTOP)
        reading = False

def update_speed():
    #speed = database.get_speed()
    speed = 25
    speed_label['text'] = 'Speed : ' + str(speed) 
 
def update_voltage():
    #battery_state = calculations.calculate_state_of_charge(database.get_v_res())
    battery_state = 25
    voltage_label['text'] = 'Battery Percentage : ' + str(battery_state)

def update_power():
    #s1plus = database.get_s1plus()
    #s1minus = database.get_s1minus()
    #power = calculations.calculate_power(s1plus, s1minus)
    power = 25
    power_label['text'] = 'Power : ' + str(power) 

def scanning():
    if reading:
        update_speed()
        update_voltage()
        update_power()
    else:
        print("Running stopped")

    screen.after(1000, scanning)
cam_button_size=5
cam_button=tkinter.Button(screen,text="Start",command=click_start_sensor,height=5,width=5)
cam_button.grid(row=1,column=0,pady=10,padx=10, rowspan=7)
cam_button.config(height=1*cam_button_size,width=5)

cam_button=tkinter.Button(screen,text="Stop",command=click_stop_sensor,height=5,width=5) # prob gonna have to check which is which dont remmeber
cam_button.grid(row=1,column=2,pady=10,padx=10, rowspan=7)
cam_button.config(height=1*cam_button_size,width=5)

camera()
screen.mainloop()
