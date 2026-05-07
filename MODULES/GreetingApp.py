import tkinter as tk
from tkinter import messagebox
def greet():
    name = entry.get()
    if name==" ":
        messagebox.showwarning("Error","Kindly enter your name")
    else:
        result.config(text="Hello "+name+"!")
root=tk.Tk()
root.title("Greeting App")
root.geometry("350x200")
tk.Label(root,text="Entet your nmae").pack(pady=5)
entry=tk.Entry(root)
entry.pack(pady=5)
tk.Button(root,text="Greet",command=greet).pack(pady=10)
result=tk.Label(root)
result.pack()
root.mainloop()