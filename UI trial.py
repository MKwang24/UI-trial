def Cal():
    C=input+10
    print(C)
import tkinter
root = tkinter.Tk()
root.title("tempconverter")
root.geometry("750x500")
instructions = tkinter.Label(root, text= "Please enter your number in degrees Celcius",font=('Times New Roman',12))
instructions.pack()
e = tkinter.Entry(root)
root.bind('<Return>', Cal)
e.pack()
e.focus_set()




root.mainloop()