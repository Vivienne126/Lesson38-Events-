from tkinter import*
from tkinter import messagebox
window=Tk()
window.title("Message box")
window.geometry("200x200")

def message():
    messagebox.showwarning("Alerert , Stop virus found")
btn=Button(window,text="Scan for virus" , command=message)
btn.place(x=40,y=80)

window.mainloop()