import tkinter as tk

if __name__ == "__main__" :
    start_window=tk.Tk()
    start_window.title('Starting window')
    start_window.geometry("500x500")

    canvas=tk.Canvas(start_window,width=400,height=150,bg='light blue')
    canvas.place(x=0,y=280)

    enl=tk.Label(start_window,text="ENTER THE TWO DIGIT OPERATION IN THE BOX GIVEN BELOW : ",background="yellow",relief="sunken",justify="left",width=65,font=('Arial',10,'bold'))
    enl.place(x=0,y=100)
    en=tk.Label(start_window,text="",background="yellow",relief="sunken",justify="right",width=33,font=('Arial',30,'bold'))
    en.place(x=0,y=150)

    def add_char(s) :
        if s!="clear" :
            en.configure(text=(en.cget("text")+s)) 
        else :
            en.configure(text="")
    
    def calculate(b,a,op) :
        if op=="+" :
            return a+b
        elif op=="-" :
            return a-b
        elif op=="*" :
            return a*b
        elif op=="/" :
            return a/b
        elif op=="^" :
            return a**b  
    
    def calculate_and_display() :
        s=(en.cget("text"))
        OPERATORS = set(['+', '-', '*', '/', '^'])
        for i in OPERATORS :
            if i in s :
                n=s.index(i)
                break
        result=calculate(int(s[n+1:]),int(s[:n]),i)
        en.configure(text=str(result))
    

    oneb=tk.Button(canvas,text="1",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("1"))
    oneb.grid(row=0,column=0)
    twob=tk.Button(canvas,text="2",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("2"))
    twob.grid(row=0,column=1)
    threeb=tk.Button(canvas,text="3",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("3"))
    threeb.grid(row=0,column=2)
    fourb=tk.Button(canvas,text="4",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("4"))
    fourb.grid(row=1,column=0)
    fiveb=tk.Button(canvas,text="5",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("5"))
    fiveb.grid(row=1,column=1)
    sixb=tk.Button(canvas,text="6",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("6"))
    sixb.grid(row=1,column=2)
    sevenb=tk.Button(canvas,text="7",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("7"))
    sevenb.grid(row=2,column=0)
    eightb=tk.Button(canvas,text="8",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("8"))
    eightb.grid(row=2,column=1)
    nineb=tk.Button(canvas,text="9",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("9"))
    nineb.grid(row=2,column=2)

    prod=tk.Button(canvas,text="*",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("*"))
    prod.grid(row=0,column=3)  
    div=tk.Button(canvas,text="/",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("/"))
    div.grid(row=0,column=4)
    subb=tk.Button(canvas,text="-",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("-"))
    subb.grid(row=2,column=3) 
    addb=tk.Button(canvas,text="+",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("+"))
    addb.grid(row=2,column=4)
    powerb=tk.Button(canvas,text="^",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=lambda :add_char("^"))
    powerb.grid(row=2,column=5)


    clear=tk.Button(canvas,text="clr",fg="black",bg="light blue",padx=28,pady=20,font=('Arial',10,'bold'),command=lambda :add_char("clear"))
    clear.grid(row=1,column=3) 

    equalb=tk.Button(canvas,text="=",fg="black",bg="light blue",padx=28,pady=15,font=('Arial',15,'bold'),command=calculate_and_display)
    equalb.grid(row=1,column=4)

    start_window.mainloop()