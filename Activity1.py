from tkinter import*
window=Tk()
window.title("Event Handeler")
window.geometry("100x100")

def handel_keypress(event):
    print(event.char)
window.bind("<Key>" , handel_keypress)

def handle_click(event):
    print("The button was clicked")
btn=Button(text="Click me")
btn.pack()
btn.bind("<Button-1>" , handle_click)
window.mainloop()
