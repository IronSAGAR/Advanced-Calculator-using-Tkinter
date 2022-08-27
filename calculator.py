import tkinter


expression = ""
def equal():
    try:
        exp =eval( e1.get())
        equation.set(exp)
        global expression
        expression = str(exp)
    except:
        equation.set("error")
        expression = ""
        
def press(num):
    global expression
    expression += num
    equation.set(expression)

def back():
    global expression
    if len(expression) >0:
        expression = expression[:-1]
    else:
        expression = ""
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set(expression)

obj = tkinter.Tk()
obj.title("Calculator")
obj.geometry("450x320")

equation = tkinter.StringVar()

e1 = tkinter.Entry(obj,textvariable=equation)

e1.grid(row=1, column=0,columnspan=4,ipadx=100)

bt1 = tkinter.Button(text='clear',width=10 , height= 1,command = lambda:clear())
bt1.grid(row = 2 , column= 0)

bt2 = tkinter.Button(text="back",width=10 , height= 1,command=lambda:back())
bt2.grid(row = 2 , column = 1)

bt3 = tkinter.Button(text = "%",width=10 , height= 1,command=lambda:press("%"))
bt3.grid(row = 2 , column= 2)

bt4 = tkinter.Button(text="/",width=10 , height= 1,command=lambda:press("/"))
bt4.grid(row=2 , column=3)

bt5 = tkinter.Button(text = "7",width=10 , height= 1,command=lambda:press("7"))
bt5.grid(row = 3 , column= 0)

bt6 = tkinter.Button(text = "8",width=10 , height= 1,command=lambda:press("8"))
bt6.grid(row = 3 , column= 1)

bt7 = tkinter.Button(text= "9",width=10 , height= 1,command=lambda:press("9"))
bt7.grid(row=3 , column=2)

bt8 = tkinter.Button(text = "*",width=10 , height= 1,command=lambda:press("*"))
bt8.grid(row = 3 , column=3)

bt9 = tkinter.Button(text = "4",width=10 , height= 1,command=lambda:press("4"))
bt9.grid(row = 4 , column=0)

bt10 = tkinter.Button(text = "5",width=10 , height= 1,command=lambda:press("5"))
bt10.grid(row = 4 , column=1)

bt11 = tkinter.Button(text = "6",width=10 , height= 1,command=lambda:press("6"))
bt11.grid(row = 4 , column=2)

bt12 = tkinter.Button(text = "-",width=10 , height= 1,command=lambda:press("-"))
bt12.grid(row = 4 , column=3)

bt13 = tkinter.Button(text = "1",width=10 , height= 1,command=lambda:press("1"))
bt13.grid(row = 5 , column=0)

bt14 = tkinter.Button(text = "2",width=10 , height= 1,command=lambda:press("2"))
bt14.grid(row = 5 , column=1)

bt15 = tkinter.Button(text = "3",width=10 , height= 1,command=lambda:press("3"))
bt15.grid(row = 5 , column=2)

bt16 = tkinter.Button(text = "+",width=10 , height= 1,command=lambda:press("+"))
bt16.grid(row = 5 , column=3)

bt17 = tkinter.Button(text = "0",width=10 , height= 1,command=lambda:press("0"))
bt17.grid(row = 6 , column=1)

bt18 = tkinter.Button(text = ".",width=10, height= 1,command=lambda:press("."))
bt18.grid(row = 6 , column=2)

bt19 = tkinter.Button(text = "=",width=10, height= 1,command=equal)
bt19.grid(row = 6 , column=3)

obj.mainloop()


