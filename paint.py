from tkinter import *
root=Tk()
root.title("My Paint")
root.geometry("450x400")
def paint(event):
    x1,y1,x2,y2=(event.x-3),(event.y-3),(event.x+3),(event.y+3)
    widget.create_line(x1,y1,x2,y2,fill= "red")
Button(root,text="Exit",bg="black",fg="red",command=quit,padx=13,pady=13).pack(anchor="se",side=BOTTOM,padx=12,pady=12)
widget=Canvas(root,width=450,height=300)
Button(root,text="File",fg="black",padx=1,pady=1).pack(anchor="nw",side=LEFT,padx=1,pady=3)
Button(root,text="Edit",fg="black",padx=1,pady=1).pack(anchor="nw",side=LEFT,padx=1,pady=3)
Button(root,text="Help",fg="black",padx=1,pady=1).pack(anchor="nw",side=LEFT,padx=3,pady=3)
widget.bind("<B1-Motion>",paint)
Label(root,text="Double click and drag to draw.",bg="black",fg="red",height=1,width=30).pack(anchor="nw",side=RIGHT,padx=15,pady=3)
widget.pack()
root.mainloop()