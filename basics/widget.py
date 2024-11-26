from tkinter import *

count = 0

# Click


def click():
    global count
    count += 1
    print(f'The button has been clicked {count} times')
# Submit


def submit():
    username = entry.get()
    print(f'{username} has submitted the input')
    entry.config(state=DISABLED)

# Delete


def delete():
    entry.delete(0, END)

# Backspace


def backspace():
    entry.delete(len(entry.get()) - 1, END)


# Instantiate a new window object
window = Tk()
window.geometry('760x480')
window.config(background='grey')
window.title('Graphical User Interface in Python')

# Instantiate a new label object
label = Label(window, text='Sample label', font=(
    'Arial', 20, 'bold'), fg='green', bg='white', padx=15, pady=15, relief=RAISED)
label.pack()

# Instantiate a new button object
button = Button(window, text='Click', command=click,
                font=('Arial', 20, 'bold'), fg='blue', bg='white', state=ACTIVE)
button.pack()

# Instantiate a new entry widget object
entry = Entry(window, font=('Arial', 30, 'bold'))
entry.insert(0, 'Type your message...')
entry.pack(side=LEFT)

submit_button = Button(window, text='Submit', font=(
    'Arial', 15, 'bold'), command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text='Delete', font=(
    'Arial', 15, 'bold'), command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text='Backspace', font=(
    'Arial', 15, 'bold'), command=backspace)
backspace_button.pack(side=RIGHT)

# Display the window on the screen for the user
window.mainloop()
