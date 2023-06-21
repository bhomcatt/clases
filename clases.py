from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.geometry("900x600")
root.title("clases")

class createElements():
    def __init__(self):
        print("BALDAND BAWRL")
    def createNewElement(self):
        label = Label(root, text="nueva etiqueta", fg="red", bg="blue")
        label.pack()
        class_btn = Button(root, text="boton", command=self.message)
        class_btn.pack(padx=20, pady=10)
        value = [1,2,3,4]
        class_dropdown = ttk.Combobox(root, state = "readonly", values = value)
        class_dropdown.pack()
        
    def message(self):
        messagebox.showinfo("showinfo", "hola")

obj_of_createElements = createElements()

btn = Button(root, text = "hola", command = obj_of_createElements.createNewElement)
btn.pack(padx=20, pady=10)



root.mainloop()