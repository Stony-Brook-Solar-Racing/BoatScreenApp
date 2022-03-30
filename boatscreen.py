import tkinter
from util import database
import subprocess
import signal
import os

screen = tkinter.Tk()

screen.title("Solar Boat Screen")
screen.geometry("500x500")

rpm_label = tkinter.Label(screen, text='RPM: 0')
rpm_label.pack()

voltage_label = tkinter.Label(screen, text='Voltage: 0')
voltage_label.pack()

s1minus_label = tkinter.Label(screen, text='Voltage: 0')
s1minus_label.pack()

s1plus_label = tkinter.Label(screen, text='Voltage: 0')
s1plus_label.pack()

s2minus_label = tkinter.Label(screen, text='Voltage: 0')
s2minus_label.pack()

s2plus_label = tkinter.Label(screen, text='Voltage: 0')
s2plus_label.pack()

running = True
reading = True

p = subprocess.Popen(["python3", "readsensor.py"])

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

startStopButton = tkinter.Button(text="Start/Stop", command=clickStartStopButton)
startStopButton.place(x=100, y=100)

startStopSensor = tkinter.Button(text="Start/Stop Sensor", command=clickStartStopSensor)
startStopSensor.place(x=100, y=300)

def update_rpm():
    rpm = database.get_rpm()
    rpm_label['text'] = 'RPM : ' + str(rpm['RPM'])

def calculate_voltage(v_res):
    return v_res
 
def update_voltage():
    voltage = database.get_voltage()
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

    screen.after(1000, scanning)

screen.after(1000, scanning)
screen.mainloop()
