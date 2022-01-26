import tkinter
from util import database

screen = tkinter.Tk()

screen.title("Solar Boat Screen")

rpm_label = tkinter.Label(screen, text='RPM: 0')
rpm_label.pack()

def update_rpm():
    rpm = database.get_rpm()
    rpm_label['text'] = 'RPM : ' + str(rpm['RPM'])
    print(rpm)
    print(rpm_label)
    screen.after(1000, update_rpm)

update_rpm()

screen.mainloop()