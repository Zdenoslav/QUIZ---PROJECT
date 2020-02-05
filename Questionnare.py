from tkinter import *

class Questionnaire(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.grid()
        self.create_prog_select()
        self.create_team_xp_quest()
        self.create_probs()
        self.create_comments()
        self.entry_name()
        self.quit()

    def create_prog_select(self):

        lblProg = Label(self, text='Degree Programme:', font=('MS', 8, 'bold'))
        lblProg.grid(row=0, column=0, columnspan=2, sticky=NE)

        #listbox
        self.listProg = Listbox(self, height=3)
        self.listProg.grid(row=0, column=2, columnspan=2, sticky=NE)

        #scrollbar
        scroll = Scrollbar(self, command=self.listProg.yview)
        self.listProg.configure(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=4, sticky=W)

        #items for listbox
        for item in ["CS", "CS with", "CSE", "IS", "JOINTS", ""]:
            self.listProg.insert(END, item)

        self.listProg.selection_set(END)

    def create_team_xp_quest(self):

        lblStrAgr = Label(self, text='Team Experience:', font=('MS', 8, 'bold'))
        lblStrAgr.grid(row=4, column=0, columnspan=2)
            # create widgets to ask Team Experience Questions
        lblStrAgr = Label(self, text= '1.Our team worked together effectively', font=('MS', 8,'bold'))
        lblStrAgr.grid(row=5, column= 0, columnspan=4)

        lblStrAgr = Label(self, text= '2.Our team produced good quality products', font=('MS', 8,'bold'))
        lblStrAgr.grid(row=6, column= 0, columnspan=4)

        lblStrAgr = Label(self, text= '3.I enjoyed working in our team', font=('MS', 8,'bold'))
        lblStrAgr.grid(row=7, column= 0, columnspan=4)

        lblStrAgr = Label(self, text = 'Strongly \n Agree', font=('MS', 8,'bold'))
        lblStrAgr.grid(row=3, column= 4, rowspan=2)

        lblStrAgr = Label(self, text = 'Partly \n Agree', font=('MS', 8,'bold'))
        lblStrAgr.grid(row=3, column= 5, rowspan=2)

        lblStrAgr = Label(self, text = 'Partly \n Disagree', font=('MS', 8,'bold'))
        lblStrAgr.grid(row=3, column= 6, rowspan=2)

        lblStrAgr = Label(self, text = 'Strongly \n Disagree', font=('MS', 8,'bold'))
        lblStrAgr.grid(row=3, column= 7, rowspan=2)


    #RadioButtons
        self.varQ1 = IntVar()

        R1Q1 = Radiobutton(self, variable=self.varQ1, value=4)
        R1Q1.grid(row=5, column=4)

        R2Q1 = Radiobutton(self, variable= self.varQ1, value=3)
        R2Q1.grid(row=5, column= 5)

        R3Q1 = Radiobutton(self, variable= self.varQ1, value=2)
        R3Q1.grid(row=5, column= 6)

        R4Q1 = Radiobutton(self, variable= self.varQ1, value=1)
        R4Q1.grid(row=5, column= 7)

        #row 6
        R1Q1 = Radiobutton(self, variable=self.varQ1, value=4)
        R1Q1.grid(row=6, column=4)

        R2Q1 = Radiobutton(self, variable= self.varQ1, value=3)
        R2Q1.grid(row=6, column= 5)

        R3Q1 = Radiobutton(self, variable= self.varQ1, value=2)
        R3Q1.grid(row=6, column= 6)

        R4Q1 = Radiobutton(self, variable= self.varQ1, value=1)
        R4Q1.grid(row=6, column= 7)

        #row7
        R1Q1 = Radiobutton(self, variable=self.varQ1, value=4)
        R1Q1.grid(row=7, column=4)

        R2Q1 = Radiobutton(self, variable= self.varQ1, value=3)
        R2Q1.grid(row=7, column= 5)

        R3Q1 = Radiobutton(self, variable= self.varQ1, value=2)
        R3Q1.grid(row=7, column= 6)

        R4Q1 = Radiobutton(self, variable= self.varQ1, value=1)
        R4Q1.grid(row=7, column= 7)

    def create_probs(self):
        #create widgets to show Problems experienced

        lblProb1 = Label(self, text='Problems:', font=('MS', 8, 'bold'))
        lblProb1.grid(row=8, column=0)

        lblProb2 = Label(self, text='Our team often experienced the ' + 'following problems(choose all that apply):')
        lblProb2.grid(row=8, column=1, columnspan=6, sticky=W)

        #checkbutton
        self.varCB1 = IntVar()
        CB1 = Checkbutton(self, text=" Poor Communication", variable=self.varCB1)
        CB1.grid(row=9, column=0, columnspan=4, sticky=W)

        self.varCB1 = IntVar()
        CB1 = Checkbutton(self, text=" Lack of Direction", variable=self.varCB1)
        CB1.grid(row=10, column=0, columnspan=4, sticky=W)

        self.varCB1 = IntVar()
        CB1 = Checkbutton(self, text=" Disagreements Amongst Team", variable=self.varCB1)
        CB1.grid(row=11, column=0, columnspan=4, sticky=W)

        self.varCB1 = IntVar()
        CB1 = Checkbutton(self, text=" Members Missing Meetings", variable=self.varCB1)
        CB1.grid(row=9, column=5, columnspan=4, sticky=W)

        self.varCB1 = IntVar()
        CB1 = Checkbutton(self, text=" Members Not Contributing", variable=self.varCB1)
        CB1.grid(row=10, column=5, columnspan=4, sticky=W)

        self.varCB1 = IntVar()
        CB1 = Checkbutton(self, text=" Members Not Motivated", variable=self.varCB1)
        CB1.grid(row=11, column=5, columnspan=4, sticky=W)

    def create_comments(self):

        Text = Label(self, text="Comments about Teamwork: ", font=('MS', 8,'bold'))
        Text.grid(row=12, column=0, columnspan=2)

        self.txtComment = Text(self, height=3, width=40)

        scroll = Scrollbar(self, command=self.txtComment.yview)
        self.txtComment.configure(yscrollcommand=scroll.set)

        self.txtComment.grid(row=12, column=2, columnspan=5, sticky=E)
        scroll.grid(row=12, column=7, sticky=W)

    def entry_name(self):

        self.entName = Entry(self)
        self.entName.grid(row=15, column=3, columnspan=2, sticky=E)

    def quit(self):
        global root
        root.quit()


#main
root = Tk()
root.title("Teamwork Questionnaire")
root.geometry("1000x500")
app = Questionnaire(root)
root.mainloop()
