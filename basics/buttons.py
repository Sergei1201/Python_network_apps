from tkinter import *

count = 0


def click():
    global count
    count += 1
    print(f'You clicked the button {count} times')


# Create an instance of a window
window = Tk()

window.geometry('420x420')
window.title('Graphical User Interface in Python')
window.config(background='grey')

label = Label(window, text='Sample text', padx=15, pady=15,
              font=('Arial', 20, 'bold'), fg='black', relief=RAISED)
label.pack()


button = Button(window, text='Click', command=click,
                font=('Arial', 20, 'bold'), fg='blue', bg='white', state=ACTIVE)
button.pack()

# Display the window on the screen
window.mainloop()
