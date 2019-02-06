from tkinter import *
from PIL import Image
from PIL import ImageTk
from BarScannerCam import sc
root = Tk()
#one = Label(root, text="One", bg="red", fg="white")
#C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file="Persistent_logo.png")
filename = filename.zoom(3)
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
b = Button(root, text="RUN", command=sc)
b.pack()
#C.pack()
background_label.pack()

root.mainloop()
