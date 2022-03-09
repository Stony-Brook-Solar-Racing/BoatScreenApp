import tkinter
from util import database

screen = tkinter.Tk()

screen.title("Solar Boat Screen")

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

def update_rpm():
    rpm = database.get_rpm()
    rpm_label['text'] = 'RPM : ' + str(rpm['RPM'])
    print(rpm)
    print(rpm_label)
    screen.after(1000, update_rpm)

def update_voltage():
    voltage = database.get_voltage()
    voltage_label['text'] = 'Voltage : ' + str(voltage['voltage'])
    s1minus_label['text'] = 'S1- : ' + str(voltage['s1minus'])
    s1plus_label['text'] = 'S1+ : ' + str(voltage['s1plus'])
    s2plus_label['text'] = 'S2+ : ' + str(voltage['s2plus'])
    s2minus_label['text'] = 'S2- ' + str(voltage['s2minus'])
    print(voltage)
    print(voltage_label)
    screen.after(1000, update_voltage)

update_rpm()
update_voltage()

screen.mainloop()
