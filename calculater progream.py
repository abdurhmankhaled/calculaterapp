from tkinter import *
from tkinter import messagebox
calculater = Tk()
calculater.title("Calculater")
calculater.geometry("400x400")
the_text = Label(calculater , text="Write Your numbers", height=4,
                  font=("Arial", 20))
the_text.pack()
num1=StringVar()
operator=StringVar()
num2=StringVar()
result1=StringVar()


number1=Entry(calculater,font=('Arial',20),width=7,textvariable=num1)
number1.pack()
operatoin=Entry(calculater,font=('Arial',20),width=7,textvariable=operator)
operatoin.pack()
number2=Entry(calculater,font=('Arial',20),width=7,textvariable=num2)
number2.pack()
def calc():
    n1=num1.get()
    n2=num2.get()
    op=operator.get()
    if op=='+':
     result=int(n1)+int(n2)
     print(result)
    elif op=='-':
     result=int(n1)-int(n2)
     print(result)
    elif op=='*':
     result=int(n1)*int(n2)
     print(result)
    else :
     result=int(n1)/int(n2)
     print(result)
    result1.get()
    result1.set(result)
    return result
     
    
    
btn=Button(calculater,font=('Arial',20),width=10,text='result',command=calc)
btn.pack()
resulttext = Label(calculater , text='result', height=4,textvariable=result1,
                  font=("Arial", 20))
resulttext.pack()




calculater.mainloop()
