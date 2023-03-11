from tkinter import *
window = Tk()

window.title("ENCRYPTION WITH ASCII CODE")
window.geometry("500x500")

lb = Label(window, text="ASCII Code Numbers: ")
lb2 = Label(window, text="Encryption: ")

input = Entry(window)

def con():
    lb["text"]=""
    name = input.get()
    for letter in name:
        lb["text"]+= str(ord(letter))+ " "
        number =int(ord(letter))
        new = number-1
        lb2["text"] += str(chr(new))

button = Button(window, text="Show Name In ASCII and encryption", command=con)

lb.place(relx=0.5, rely=0.6, anchor=CENTER)
lb2.place(relx=0.5, rely=0.7, anchor=CENTER)
input.place(relx=0.5, rely=0.3, anchor=CENTER)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()