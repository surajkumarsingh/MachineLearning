from tkinter import *
from BarScannerCam import Bar
class GUI(Bar):
    def ui(self):
        #global obj, GUI
        root = Tk()
        # one = Label(root, text="One", bg="red", fg="white")
        # C = Canvas(root, bg="blue", height=250, width=300)
        filename = PhotoImage(file="Persistent_logo.png")
        filename = filename.zoom(2)
        background_label = Label(root, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        b = Button(root, text="RUN", command=obj.sc)
        b.pack()
        # C.pack()
        background_label.pack()
        root.mainloop()
obj = GUI()
obj.ui()
#print(Bar.sc.text)
