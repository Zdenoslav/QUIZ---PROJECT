from tkinter import *
import tkinter as tk
from db import Database
from tkinter import messagebox

db = Database('store.db')

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('True Or False')
        #width height
        master.geometry('700x350')
        #create widgets
        self.create_widgets()
        #Init selected item variable
        self.selected_item = 0
        self.populate_list()

    def create_widgets(self):

            #radiobuttons
            self.answer = tk.StringVar()
            self.lblR1Q1 = tk.Label(self.master, text="True", font=('bold', 14), pady=20)
            self.lblR1Q1.grid(row=0, column=3,sticky=tk.E)
            R1Q1 = tk.Radiobutton(value='TRUE', variable=self.answer)
            R1Q1.grid(row=1, column=3, sticky=tk.E)

            self.lblR2Q1 = tk.Label(self.master, text="False", font=('bold', 14), pady=20)
            self.lblR2Q1.grid(row=0, column=4, sticky=tk.E)
            R2Q1 = tk.Radiobutton(value='FALSE', variable=self.answer)
            R2Q1.grid(row=1, column=4, sticky=tk.E)

            # Part
            self.part_text = tk.StringVar()
            self.part_label = tk.Label(self.master, text='TRUE OR FALSE', font=('bold', 14), pady=20)
            self.part_label.grid(row=0, column=0, sticky=tk.W)
            self.part_entry = tk.Entry(self.master, textvariable=self.part_text)
            self.part_entry.grid(row=0, column=1)

            #Buttons
            self.add_btn = tk.Button(self.master, text='Add Question', width=12, command=self.add_item)
            self.add_btn.grid(row=21, column=0, pady=20)

            #Buttons
            self.remove_btn = tk.Button(self.master, text='Remove Question', width=12, command=self.remove_item)
            self.remove_btn.grid(row=21, column=1, pady=20)

            #Buttons
            self.update_btn = tk.Button(self.master, text='Update Question', width=12,command=self.update_item)
            self.update_btn.grid(row=21, column=2, pady=20)

            #list_box
            self.parts_list= tk.Listbox(self.master, height=8, width=50, border=0)
            self.parts_list.grid(row=3, column=0, columnspan=3, rowspan=4, pady=20, padx=20)
            #Create scrollbar
            self.scrollbar = tk.Scrollbar(self.master)
            self.scrollbar.grid(row=3, column=3)

            #set scroll to listbox
            self.parts_list.configure(yscrollcommand=self.scrollbar.set)
            self.scrollbar.configure(command=self.parts_list.yview)

            #bind select
            self.parts_list.bind('<<ListboxSelect>>', )

    def populate_list(self):
        self.parts_list.delete(0, tk.END)
        for row in db.fetch():
            self.parts_list.insert(tk.END, row)

    def add_item(self):
        #validationvarQ1
        if self.part_text.get() == '' or self.answer.get() == '':
            messagebox.showerror('Required Fields', 'Please include all fields')
            return
        db.insert(self.part_text.get(), self.answer.get())
        self.parts_list.delete(0, tk.END)
        self.parts_list.insert(tk.END, (self.part_text.get(), self.answer.get()))
        self.populate_list()
        print('hello')

    def select_item(self, event):
        try:
        #Get Index
            index = self.parts_list.curselection()[0]
        #Get selected item
            self.selected_item = self.parts_list.get(index)
        # Add text to entries
            self.part_entry.delete(0, tk.END)
            self.part_entry.insert(tk.END, self.selected_item[0])
            self.lblR1Q1.delete(0, tk.END)
            self.lblR1Q1.insert(tk.END, self.selected_item[1])
            self.lblR2Q1.delete(0, tk.END)
            self.lblR2Q1.insert(tk.END, self.selected_item[2])
        except IndexError:
            pass
        print('lol')

    def remove_item(self):
        db.remove(self.selected_item[0])
        self.populate_list()
        print('ol')

    def update_item(self):
        db.update(self.selected_item[0], self.part_text.get(), self.answer.get())
        self.populate_list()

root = tk.Tk()
app = Application(master=root)

#Start program
app.mainloop()
