from tkinter import *
from tkinter import messagebox


root = Tk()

root.title("zetor插件")
root.geometry("600x400+400+400")

btn01 = Button(root)
btn01["text"] = "点我就送你一朵好看的玫瑰花花"

btn01.pack()

def songhua(e):
    messagebox.showinfo("Message","送你一朵花哈哈哈哈哈哈哈哈哈")
    print("送你99朵花")

btn01.bind("<Button-1>", songhua)

root.mainloop()
