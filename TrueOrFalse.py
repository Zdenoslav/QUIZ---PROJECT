from tkinter import *
from db import Database
from tkinter import messagebox

db = Database('store.db')

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

def setIncorrect():
    correct2 = correct.get()
    if correct2 == 'TRUE':
        incorrect = 'FALSE'
        add_item(correct2, incorrect)
    else:
        incorrect = 'TRUE'
        add_item(correct2, incorrect)

def add_item(correct3, incorrect):
    #validationvarQ1
    if part_text.get() == '' or correct.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(part_text.get(), correct3, incorrect)
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), correct3, incorrect))
    populate_list()

def select_item(event):
    global selected_item
    index = parts_list.curselection()[0]
    selected_item = parts_list.get(index)

    part_entry.delete(0, END)
    part_entry.insert(END, selected_item[0])
    print('lol')

def remove_item():
    db.remove(selected_item[0])
    populate_list()

def update_item():
    db.update(selected_item[0], part_text.get(), R1Q1.get(), R2Q1.get())
    populate_list()

# create window object
app= Tk()

#corect answer
correct = StringVar()
incorrect = ''

#radiobuttons

lblR1Q1 = Label(app, text="True", font=('bold', 14), padx=10, pady= 10)
lblR1Q1.grid(row=0, column=4,sticky=E)
R1Q1 = Radiobutton(variable=correct, value='TRUE', padx=20, pady=10)
R1Q1.grid(row=1, column=4, sticky=E)

lblR2Q1 = Label(app, text="False", font=('bold', 14), padx=20, pady=10)
lblR2Q1.grid(row=0, column=5, sticky=E)
R2Q1 = Radiobutton(variable=correct, value='FALSE', padx=20, pady=10)
R2Q1.grid(row=1, column=5, sticky=E)

# Part
part_text = StringVar()
part_label = Label(app, text='TRUE OR FALSE', font=('bold', 14), padx=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text, width=30)
part_entry.grid(row=1, column=0, sticky=W, padx=20)

#Buttons
add_btn = Button(app, text='Add Question', width=20, command=setIncorrect)
add_btn.grid(row=21, column=0, padx=20, pady=20)
#Buttons
remove_btn = Button(app, text='Remove Question', width=20, command=remove_item)
remove_btn.grid(row=21, column=1, padx=20, pady=20)
#list_box
parts_list= Listbox(app, height=10, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=4, rowspan=4, pady=20, padx=20)
#Create scrollbar
scrollbar = Scrollbar(app,)
scrollbar.grid(row=4, column=3, pady=10)

#set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

#bind select
parts_list.bind('<<ListboxSelect>>', select_item)

#populate data
populate_list()

app.title('True or False')
app.geometry('800x450')

#Start program
app.mainloop()
