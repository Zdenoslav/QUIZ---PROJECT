from tkinter import *
from db import Database
from tkinter import messagebox

db = Database('store.db')

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    #validation
    if part_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(part_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(),))
    populate_list()

def select_item(event):
    global selected_item
    index = parts_list.curselection()[0]
    selected_item = parts_list.get(index)

    part_entry.delete(0, END)
    part_entry.insert(END, selected_item[0])


def remove_item():
    db.remove(selected_item[0])
    populate_list()

#def update_item():
#    db.update(selected_item[0], part_text.get())
#    populate_list()

# create window object
app= Tk()

# Part
part_text = StringVar()
part_label = Label(app, text='TRUE OR FALSE', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)


#Buttons
add_btn = Button(app, text='Add Question', width=12, command=add_item)
add_btn.grid(row=21, column=0, pady=20)

#Buttons
remove_btn = Button(app, text='Remove Question', width=12, command=remove_item)
remove_btn.grid(row=21, column=1, pady=20)

#Buttons
#update_btn = Button(app, text='Update Question', width=12, command=update_item)
#update_btn.grid(row=21, column=2, pady=20)



#list_box
parts_list= Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
#Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

#set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

#bind select
parts_list.bind('<<ListboxSelect>>', select_item)

#populate data
populate_list()


app.title('Pool')
app.geometry('700x350')

#Start program
app.mainloop()
