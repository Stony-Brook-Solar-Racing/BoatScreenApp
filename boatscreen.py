import tkinter
from util import database
from subprocess import Popen

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
process = Popen("python ./readsensor.py")

def clickStartStopButton():
    global running
    if running:
        running = False
        #print(running)
    else: 
        running = True
        #print(running)

def clickStartStopSensor():
    global reading
    global process
    if reading:
        reading = False
        process.terminate()
    else:
        process = Popen("python /readsensor.py")
        reading = True

startStopButton = tkinter.Button(text="Start/Stop", command=clickStartStopButton)
startStopButton.place(x=100, y=100)

startStopSensor = tkinter.Button(text="Start/Stop Sensor", command=clickStartStopSensor)
startStopSensor.place(x=100, y=300)

def update_rpm():
    rpm = database.get_rpm()
    rpm_label['text'] = 'RPM : ' + str(rpm['RPM'])
    print(rpm)
    print(rpm_label)

def update_voltage():
    voltage = database.get_voltage()
    voltage_label['text'] = 'Voltage : ' + str(voltage['voltage'])
    s1minus_label['text'] = 'S1- : ' + str(voltage['s1minus'])
    s1plus_label['text'] = 'S1+ : ' + str(voltage['s1plus'])
    s2plus_label['text'] = 'S2+ : ' + str(voltage['s2plus'])
    s2minus_label['text'] = 'S2- ' + str(voltage['s2minus'])
    print(voltage)
    print(voltage_label)

def scanning():
    if running:
        update_rpm()
        update_voltage()
    else:
        print("Stopped")

    screen.after(1000, scanning)

screen.after(1000, scanning)
screen.mainloop()
