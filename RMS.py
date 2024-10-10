from tkinter import *
root = Tk()
root.title("Restaurant Management System")
root.geometry("1000x500")
root.config(bg="#9A031E")
root.resizable(False,False)


#main Label
Label(root,text="Restaurant Management System",font=("Times New Roman",30),bg="#9A031E",fg="White" ).pack(pady=10)


#frame Left
f1 = Frame(root,bg="#E5F2C9",width="300",height="370")
f1.place(x=10,y=118)

#frame Middle
f2 = Frame(root,bg="#E5F2C9",width="300",height="370")
f2.place(x=340,y=118)

#frame Right
f3 = Frame(root,bg="#E5F2C9",width="300",height="370")
f3.place(x=670,y=118)

#label Work for frame Left f1
Label(f1,text="Menu",font=("times new roman",20,"bold"),bg="#E5F2C9",fg="Black").place(x=10,y=50)
Label(f1,text="Pizza-----------------700",font=("Times New Roman",15),bg="#E5F2C9",fg="Black").place(x=10,y=100)
Label(f1,text="Coffee-----------------200",font=("Times New Roman",15),bg="#E5F2C9",fg="Black").place(x=10,y=150)
Label(f1,text="Burger----------------250",font=("Times New Roman",15),bg="#E5F2C9",fg="Black").place(x=10,y=200)

#label Work for frame Middle f2
lb1_pizza=Label(f2,text="Pizza",font=("times 15 bold"),bg="#E5F2C9",fg="Black").place(x=10,y=50)
lb2_coffee=Label(f2,text="Coffee",font=("times 15 bold"),bg="#E5F2C9",fg="Black").place(x=10,y=100)
lb3_burger=Label(f2,text="Burger",font=("times 15 bold"),bg="#E5F2C9" ,fg="Black").place(x=10,y=150)

#entry work for middle Frame
pizza = StringVar()
Coffee = StringVar()
Burger = StringVar()
total_bill = StringVar()

entry_pizza=Entry(f2,textvariable=pizza,font=("times 15 bold"),bg="#E5F2C9",width=10,fg="Black")
entry_pizza.place(x=120,y=50)

entry_coffee=Entry(f2,textvariable=Coffee,font=("times 15 bold"),bg="#E5F2C9",width=10,fg="Black")
entry_coffee.place(x=120,y=100)

entry_burger=Entry(f2,textvariable=Burger,font=("times 15 bold"),bg="#E5F2C9" ,width=10,fg="Black")
entry_burger.place(x=120,y=150)


def calculate():
    try:
      a1=int(pizza.get())
    except:
        a1=0
    try:
      a2=int(Coffee.get())
    except:
      a2=0
    try:
      a3=int(Burger.get())
    except:
      a3=0
  
    a1=700*a1
    a2=200*a2
    a3=250*a3
  
    lb1_total=Label(f3, text="Total Bill : ",font=("times new roman", 20, "bold"), fg="black", bg="white")
    lb1_total.place(x=50,y=100)

    global lb2_total
    
    lb2_total=Label(f3, text=str(a1+a2+a3),font=("times new roman", 20, "bold"),fg="black",bg="white")
    lb2_total.place(x=50,y=200)
  

#buttons for middle frame
btn_calculate = Button(f2,text="Calculate",font=("times 15 bold"),bg="black",fg="white",command=calculate)
btn_calculate.place(x=20,y=200)

def reset():
  entry_pizza.delete(0,END) #DELETE DATA INSIDE ENTRY PIZZA
  entry_coffee.delete(0,END) #DELETE DATA INSIDE ENTRY COFFEE
  entry_burger.delete(0,END) #DELETE DATA INSIDE ENTRY BURGER
  lb2_total.configure(text="") #BILL LABEL SETTING IT TO EMPTY

btn_reset = Button(f2,text="Reset",font=("times 15 bold"),bg="black",fg="white",command=reset)
btn_reset.place(x=160,y=200)

#frame 3  right
#BIll-------------------------------------------------------------------

Bill=Label(f3,text="Total Bill",font=("times 15 bold"),bg="#E5F2C9",fg="Black")

Bill.place(x=90,y=50)


root.mainloop()