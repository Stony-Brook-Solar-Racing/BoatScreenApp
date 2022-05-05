import tkinter
from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import Image, ImageTk
import cv2

ikkuna=tkinter.Tk()
ikkuna.title("Solar Boat Screen")

frame=np.random.randint(0,255,[100,100,3],dtype='uint8')
img = ImageTk.PhotoImage(Image.fromarray(frame))

paneeli_image=tkinter.Label(ikkuna) #,image=img)
paneeli_image.grid(row=0,column=0,columnspan=3,pady=1,padx=10)

rpm_label = tkinter.Label(ikkuna, text='RPM: 0')
rpm_label.grid(row=2, column=1, pady=1, padx=10)

voltage_label = tkinter.Label(ikkuna, text='Voltage: 0')
voltage_label.grid(row=3, column=1, pady=1, padx=10)

s1minus_label = tkinter.Label(ikkuna, text='Voltage: 0')
s1minus_label.grid(row=4, column=1, pady=1, padx=10)

s1plus_label = tkinter.Label(ikkuna, text='Voltage: 0')
s1plus_label.grid(row=5, column=1, pady=1, padx=10)

s2minus_label = tkinter.Label(ikkuna, text='Voltage: 0')
s2minus_label.grid(row=6, column=1, pady=1, padx=10)

s2plus_label = tkinter.Label(ikkuna, text='Voltage: 0')
s2plus_label.grid(row=7, column=1, pady=1, padx=10)

global cam
running = True
reading = True

#p = subprocess.Popen(["python3", "readsensor.py"])

def otakuva():
    global frame
    global cam
    cam = cv2.VideoCapture(0)
    #cv2.namedWindow("Experience_in_AI camera")
    while True:
        ret, frame = cam.read()
        scanning()
        #Update the image to tkinter...
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        resize = cv2.resize(frame, (320,240))
        img_update = ImageTk.PhotoImage(Image.fromarray(resize)) # frame inside changing to resize
        paneeli_image.configure(image=img_update)
        paneeli_image.image=img_update
        paneeli_image.update()

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

def lopeta():
    global cam
    cam.release()
    cv2.destroyAllWindows()
    print("Stopped!")

def clickStartStopButton():
    global running
    if running:
        running = False
    else: 
        running = True

def clickStartStopSensor():
    global reading
    global p
    if reading:
        os.kill(p.pid, signal.SIGSTOP)
        reading = False
    else:
        os.kill(p.pid, signal.SIGCONT)
        reading = True

def update_rpm():
    rpm = {'RPM':1}#database.get_rpm()
    rpm_label['text'] = 'RPM : ' + str(rpm['RPM'])

def calculate_voltage(v_res):
    return v_res
 
def update_voltage():
    voltage = {'voltage':1, 's1minus':1, 's1plus':2, 's2plus':3, 's2minus':3}#database.get_voltage()
    voltage_label['text'] = 'Voltage : ' + str(voltage['voltage'])
    s1minus_label['text'] = 'S1- : ' + str(voltage['s1minus'])
    s1plus_label['text'] = 'S1+ : ' + str(voltage['s1plus'])
    s2plus_label['text'] = 'S2+ : ' + str(voltage['s2plus'])
    s2minus_label['text'] = 'S2- ' + str(voltage['s2minus'])

def scanning():
    if running:
        update_rpm()
        update_voltage()
    else:
        print("Running stopped")

    ikkuna.after(1000, scanning)
painike_korkeus=5
painike_1=tkinter.Button(ikkuna,text="Start",command=clickStartStopButton,height=5,width=5)
painike_1.grid(row=1,column=0,pady=10,padx=10, rowspan=7)
painike_1.config(height=1*painike_korkeus,width=5)

painike_1=tkinter.Button(ikkuna,text="Stop",command=clickStartStopSensor,height=5,width=5) # prob gonna have to check which is which dont remmeber
painike_1.grid(row=1,column=2,pady=10,padx=10, rowspan=7)
painike_1.config(height=1*painike_korkeus,width=5)

otakuva()
ikkuna.mainloop()
