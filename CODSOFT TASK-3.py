import random
import string
import tkinter as tk

if __name__ == "__main__" :
    def generate():
        s=[]
        s.extend(list(string.ascii_lowercase))
        s.extend(list(string.ascii_uppercase))
        s.extend(list(string.digits))
        random.shuffle(s)
        t=n.get()
        p.set(s[0:t])

    def clear() : 
        n.set(0)
        p.set("")
        

    start_window=tk.Tk()
    start_window.title('Starting window')
    start_window.geometry("400x400")


    n=tk.IntVar()
    p=tk.StringVar()
    length=tk.Label(start_window,text="ENTER LENGTH : ")
    length.place(x=40,y=100)
    lengthe=tk.Entry(textvariable=n,width=50)
    lengthe.place(x=160,y=100,width=150)
    passworde=tk.Entry(textvariable=p,width=50)
    passworde.place(x=160,y=150,width=150)
    password=tk.Label(start_window,text="PASSWORD :")
    password.place(x=40,y=150)

    generateb=tk.Button(start_window,text="Generate",command=generate)
    generateb.place(x=80,y=250)
    clearb=tk.Button(start_window,text="Clear",command=clear)
    clearb.place(x=200,y=250)

    start_window.mainloop()