from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.title("Radio Button")
root.geometry("450x450")
var=StringVar()
quantity=IntVar()
var.set("er")
def sub():
    val=tmsg.askquestion("Your Food",f"You have selected {quantity.get()} plates {var.get()} ,Thank you!")
    if val=="yes":
        msg="Thank You Enjoy your meal"
    else:
        msg="If you need help Contact us!"
    tmsg.showinfo("Your Confirmation",msg)

Label(root,text="What would you like to eat ?",font="lucida 19 bold").pack(anchor="nw",padx=9,pady=5)
radio=Radiobutton(root,text="Dosha",variable=var,value="Dosha").pack(anchor="nw",padx=11)
radio=Radiobutton(root,text="Fish",variable=var,value="Fish").pack(anchor="nw",padx=11)
radio=Radiobutton(root,text="Sweets",variable=var,value="Sweets").pack(anchor="nw",padx=11)
radio=Radiobutton(root,text="Drinks",variable=var,value="Drinks").pack(anchor="nw",padx=11)
Label(root,text="How many plates you want").pack()
Scale(root,from_=1,to=10,variable=quantity,orient=HORIZONTAL).pack()
Button(root,text="Order Now",command=sub).pack(pady=3)
root.mainloop()