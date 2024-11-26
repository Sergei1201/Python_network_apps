from tkinter import *

window = Tk()
window.geometry('420x420')
window.title('Graphical User Interface in Python')

label = Label(window, text='Sample text',
              font=('Arial', 20, 'bold'), fg='blue', bg='grey', relief=RAISED, bd=10, padx=15, pady=15)
label.pack()


window.mainloop()
