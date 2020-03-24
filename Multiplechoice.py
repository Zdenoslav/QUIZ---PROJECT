from tkinter import *
from db2 import Database
from tkinter import messagebox

db = Database('questions2.db')

def populate_list():
    question_list.delete(0, END)
    for row in db.fetch():
        question_list.insert(END, row)

def add_item():
    #validation
    if question.get() == '' or answerA.get() == '' or answerB.get() == '' or answerC.get() == '' or answerD.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(question.get(), answerA.get(), answerB.get(), answerC.get(), answerD.get())
    question_list.delete(0, END)
    question_list.insert(END, (question.get(), answerA.get(), answerB.get(), answerC.get(), answerD.get()))
    populate_list()
    clear_text()

def select_item(event):
    try:
        global selected_item
        index = question_list.curselection()[0]
        selected_item = question_list.get(index)

        question_entry.delete(0, END)
        question_entry.insert(END, selected_item[1])
        answerA_entry.delete(0, END)
        answerA_entry.insert(END, selected_item[2])
        answerB_entry.delete(0, END)
        answerB_entry.insert(END, selected_item[3])
        answerC_entry.delete(0, END)
        answerC_entry.insert(END, selected_item[4])
        answerD_entry.delete(0, END)
        answerD_entry.insert(END, selected_item[5])

    except IndexError:
     pass

    print('lool')

def remove_item():
    db.remove(selected_item[0])
    populate_list()

def update_item():
    db.update(selected_item[0], question.get(), answerA.get(), answerB.get(), answerC.get(), answerD.get())
    populate_list()

def clear_text():
    question_entry.delete(0, END)
    answerA_entry.delete(0, END)
    answerB_entry.delete(0, END)
    answerC_entry.delete(0, END)
    answerD_entry.delete(0, END)

app= Tk()

# Questions
question = StringVar()
question_label = Label(app, text='MULTIPLE CHOICE', font=('bold', 14), pady=20)
question_label.grid(row=0, column=0, sticky=W)
question_entry = Entry(app, textvariable=question, width=30,)
question_entry.grid(row=0, column=1)

#Question fields

answerA = StringVar()
answerA_label = Label(app, text='A', font=('bold', 14), pady=10)
answerA_label.grid(row=1, column=0, sticky=W)
answerA_entry = Entry(app, textvariable=answerA)
answerA_entry.grid(row=1, column=1)

answerB = StringVar()
answerB_label = Label(app, text='B', font=('bold', 14), pady=10)
answerB_label.grid(row=1, column=2, sticky=W)
answerB_entry = Entry(app, textvariable=answerB)
answerB_entry.grid(row=1, column=3)

answerC = StringVar()
answerC_label = Label(app, text='C', font=('bold', 14), pady=10)
answerC_label.grid(row=2, column=0, sticky=W)
answerC_entry = Entry(app, textvariable=answerC)
answerC_entry.grid(row=2, column=1)

answerD = StringVar()
answerD_label = Label(app, text='D', font=('bold', 14), pady=10)
answerD_label.grid(row=2, column=2, sticky=W)
answerD_entry = Entry(app, textvariable=answerD)
answerD_entry.grid(row=2, column=3)

#list_box
question_list= Listbox(app, height=8, width=50, border=0)
question_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
#Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=5, column=2)

#set scroll to listbox
question_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=question_list.yview)

#Buttons
add_btn = Button(app, text='Add Question', width=14, command=add_item)
add_btn.grid(row=21, column=0, pady=20)

remove_btn = Button(app, text='Remove Question', width=14, command=remove_item)
remove_btn.grid(row=21, column=1, pady=20)

clear_btn = Button(app, text='Clear Fields', width=14, command=clear_text)
clear_btn.grid(row=21, column=2, pady=20)

update_btn = Button(app, text='Update Fields', width=14, command=update_item)
update_btn.grid(row=21, column=3, pady=30)

#bind select
question_list.bind('<<ListboxSelect>>', select_item)

#populate data
populate_list()

app.title('Multiple choice poll')
app.geometry('800x450')

#Start program
app.mainloop()
