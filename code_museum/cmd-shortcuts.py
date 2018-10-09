from tkinter import *

import tkinter.messagebox
import os
import sys

class MainWindow:
    def __init__(self):
        self.frame = Tk()

        self.label_name = Label(self.frame, text="name:")
        self.label_age = Label(self.frame, text="age:")
        self.label_sex = Label(self.frame, text="sex:")

        self.text_name = Text(self.frame, height="1", width=30)
        self.text_age = Text(self.frame, height="1", width=30)
        self.text_sex = Text(self.frame, height="1", width=30)

        self.label_name.grid(row=0, column=0)
        self.label_age.grid(row=1, column=0)
        self.label_sex.grid(row=2, column=0)

        self.button_ok = Button(self.frame, text="ok", width=10)
        self.button_cancel = Button(self.frame, text="cancel", width=10)

        self.text_name.grid(row=0, column=1)
        self.text_age.grid(row=1, column=1)
        self.text_sex.grid(row=2, column=1)

        self.button_ok.grid(row=3, column=0)
        self.button_cancel.grid(row=3, column=1)



        self.button_ok.bind("<ButtonRelease-1>", self.buttonListener1)
        self.frame.mainloop()

    def buttonListener1(self, event):
        os.chdir("C:\\code")
        os.system('dir')
        os.system('netstat -ano')
        tkinter.messagebox.showinfo("messagebox", "this is button 1 dialog")



if __name__ == '__main__':
    # sys.path.append("C:\\Program Files\\Tecplot\\Tec360 2013R1\\bin")
    # print sys.path



    frame = MainWindow()
