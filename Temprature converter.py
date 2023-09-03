from tkinter import *
root = Tk()
root.title("Temprature Converter")
cLabel = Label(root, text="Please write a number here to convert it")
cLabel.pack()
cTemp = Entry(root)
cTemp.pack()
def convertor():
    cString = int(cTemp.get())
    fTemp = cString*1.8+32
    fLabel = Label(root, text=fTemp)
    fLabel.pack()
    print(fTemp)
btn = Button(root, text="Convert", command=convertor)
btn.pack()
#main loop
root.mainloop()