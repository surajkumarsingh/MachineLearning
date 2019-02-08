from tkinter import *
from QRScannerAndSmile import QRScannerAndSmile


class GUI(QRScannerAndSmile):

    def ui(self):
        root = Tk()
        # one = Label(root, text="One", bg="red", fg="white")
        # C = Canvas(root, bg="blue", height=250, width=300)
        filename = PhotoImage(file="Persistent_logo.png")
        filename = filename.zoom(1)
        # background_label = Label(root, image=filename)
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)
        b = Button(root, activebackground="Green", bd=4, text="RUN", image=filename, command=obj.call)
        b.pack()
        # C.pack()
        # background_label.pack()
        root.mainloop()


obj = GUI()
obj.ui()






