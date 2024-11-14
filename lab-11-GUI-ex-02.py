import tkinter


moo = tkinter.Tk()
moo.geometry("300x300")

label_1 = tkinter.Label(moo, text = "A Label")
label_1.pack()


label_2 = tkinter.Label(moo, text = "B Label")
label_2.configure(font=("Georgia", 22, "bold"))
label_2.configure(bg = 'cyan', fg = 'magenta')
label_2.pack()


moo.mainloop()
