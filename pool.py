import tkinter
from tkinter import *
import sqlite3 as db
from Response import Response

class Poll(Frame):

    def __init__(self, master):

        Frame.__init__(self, master)
        self.grid()
        self.create_butts()
        self.question()
        self.title()
        self.title2()
        self.radiobuttons()
        self.buttontitle()
        self.answerstitle()
        self.answersfield()
        self.answersdes()
        self.showthepoll()
    #    self.store_response()
        self.quit()

    def title(self):

        lblProg = Label(self, text= 'TRUE AND FALSE', font=('MS', 20, 'bold'))
        lblProg.grid(row=0, rowspan=1, column=3, sticky=N, pady=10, padx=10)

    def title2(self):

        lblProg2 = Label(self, text='MULTIPLE-CHOICE', font=('MS', 20, 'bold'))
        lblProg2.grid(row=5, rowspan=1, column=3, sticky=N, pady=10, padx=10)

#    def question(self):

    def answerstitle(self):

        QuestionText = Label(self, text='ANSWERS', font=('MS', 10, 'bold'))
        QuestionText.grid(row=7, rowspan=1, column=3)

    #Create text-boxes
    def answersfield(self):

        self.txtA = Text(self, height=1, width=25,)

        self.txtA.grid(row=8, column=3,pady=5, padx=5, ipadx=50)

        self.txtB = Text(self, height=1, width=25)

        self.txtB.grid(row=9, column=3,pady=5, padx=5, ipadx=50)

        self.txtC = Text(self, height=1, width=25)

        self.txtC.grid(row=10, column=3,pady=5, padx=5, ipadx=50)

        self.txtD = Text(self, height=1, width=25)

        self.txtD.grid(row=11, column=3,pady=10, padx=5, ipadx=50)


    def answersdes(self):

        AnswerText = Label(self, text='A', font=('MS', 10, 'bold'))
        AnswerText.grid(row=8, rowspan=1, column=1)

        AnswerText = Label(self, text='B', font=('MS', 10, 'bold'))
        AnswerText.grid(row=9, rowspan=1, column=1)

        AnswerText = Label(self, text='C', font=('MS', 10, 'bold'))
        AnswerText.grid(row=10, rowspan=1, column=1)

        AnswerText = Label(self, text='D', font=('MS', 10, 'bold'))
        AnswerText.grid(row=11, rowspan=1, column=1)


    def buttontitle(self):

        lblBut1 = Label(self, text='TRUE', font=('MS', 10, 'bold'))
        lblBut1.grid(row=3, rowspan=1, column=1, pady=10, padx=10, ipadx=50)

        lblBut2 = Label(self, text='FALSE', font=('MS', 10, 'bold'))
        lblBut2.grid(row=3, rowspan=1, column=2, pady=10, padx=10, ipadx=50)

    def radiobuttons(self):

        self.varQ1 = IntVar()

        R1Q1 = Radiobutton(self, variable=self.varQ1, value=4)
        R1Q1.grid(row=4, column= 1, pady=10, padx=10, ipadx=50)

        R1Q2 = Radiobutton(self, variable=self.varQ1, value=4)
        R1Q2.grid(row=4, column= 2, pady=10, padx=10, ipadx=50)

    def create_butts(self):

        butSubmit= Button(self, text='ADD1',font=('MS', 15,'bold'))
        butSubmit['command']=self.store_response
    #    butSubmit['command']=self.clearResponse  #Note: no () after themethod
        butSubmit.grid(row=2, rowspan=1, column=3, columnspan=2,sticky=NW, pady=10, padx=50, ipadx=50)

        butSubmit= Button(self, text='ADD2',font=('MS', 15,'bold'))
        butSubmit['command']=self.store_response        #Note: no () after themethod
        butSubmit.grid(row=6, rowspan=1, column=3, columnspan=2, sticky=NW, pady=10, padx=50, ipadx=50)

    def question(self):

        self.index=StringVar()

        QuestionFieldTF = Text(self,height=2, width=35, variable=self.index)

        QuestionFieldTF.grid(row=2, column=1, columnspan=2,)

        QuestionFieldM = Text(self,height=2, width=35, variable=self.index)

        QuestionFieldM.grid(row=6, column=1, columnspan=2 )


    def store_response(self):

        index = self.question()

        conn = db.connect('poll_quiz.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO QUESTIONS(questions, answers) VALUES (?, ?)",(index))
        cur.close()
        conn.commit()
        conn.close()
        status.set('Data Added Succesfully.')
#    def clearResponse(self):
#        self.QuestionField.delete(1.0,END)
#        print('button is clicked')

    def showthepoll(self):

        butSubmit= Button(self, text='SHOW THE POOL',font=('MS', 15,'bold'))
    #    butSubmit['command']=self.store_response        #Note: no () after themethod
        butSubmit.grid(row=2, rowspan=1, column=4,columnspan=2,  sticky=NW, pady=10, padx=10, ipadx=35)

        butSubmit= Button(self, text='SHOW THE POOL',font=('MS', 15,'bold'))
    #    butSubmit['command']=self.store_response        #Note: no () after themethod
        butSubmit.grid(row=6, rowspan=1, column=4, columnspan=2, sticky=NW, pady=10, padx=10, ipadx=35)


    #create submit function

    def quit(self):
        global root
        root.quit()
    #Creating a database to store the question and answers from staff
conn = db.connect('poll_quiz.db')

c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS QUESTIONS
            (
               questions text,
                answers  text
              )""")

c.close()
conn.commit()
conn.close()


#main
root = Tk()
root.title("Teamwork Questionnaire")
root.geometry("1000x500")
app = Poll(root)
root.mainloop()
