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
    if part_question.get() == '' or part_answerA.get() == '' or part_answerB.get() == '' or part_answerC.get() == '' or part_answerD.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(part_question.get(), part_answerA.get(), part_answerB.get(), part_answerC.get(), part_answerD.get())
    question_list.delete(0, END)
    question_list.insert(END, (part_question.get(), part_answerA.get(), part_answerB.get(), part_answerC.get(), part_answerD.get()))
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

app= Tk()

# Questions
part_question = StringVar()
part_label = Label(app, text='MULTIPLE CHOICE', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_question)
part_entry.grid(row=0, column=1)

#Question fields

part_answerA = StringVar()
part_label = Label(app, text='A', font=('bold', 14), pady=10)
part_label.grid(row=1, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_answerA)
part_entry.grid(row=1, column=1)

part_answerB = StringVar()
part_label = Label(app, text='B', font=('bold', 14), pady=10)
part_label.grid(row=1, column=2, sticky=W)
part_entry = Entry(app, textvariable=part_answerB)
part_entry.grid(row=1, column=3)

part_answerC = StringVar()
part_label = Label(app, text='C', font=('bold', 14), pady=10)
part_label.grid(row=2, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_answerC)
part_entry.grid(row=2, column=1)

part_answerD = StringVar()
part_label = Label(app, text='D', font=('bold', 14), pady=10)
part_label.grid(row=2, column=2, sticky=W)
part_entry = Entry(app, textvariable=part_answerD)
part_entry.grid(row=2, column=3)

#list_box
question_list= Listbox(app, height=8, width=50, border=0)
question_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
#Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

#set scroll to listbox
question_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=question_list.yview)

#Buttons
add_btn = Button(app, text='Add Question', width=12, command=add_item)
add_btn.grid(row=21, column=0, pady=20)

#populate data
populate_list()

app.title('Multiple choice poll')
app.geometry('800x450')

#Start program
app.mainloop()
