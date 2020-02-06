from tkinter import *
from Response import Response

class DisplayResults(Frame):# GUI Setup

    def __init__(self, master):
        # Initialise Questionnaire Class
        Frame.__init__(self, master)
        self.pack()

    def ret_resp(self):

        countAll = 0
        sumQ1CSE = 0.0
        sumP5Joints = 0

        import shelve
        db=shelve.open('responsedb')
        respNo = len(db)

        for i in range (1, respNo):
            Ans = db.get((str(i)))

        countAll +=1
        sumQ1All += Ans.q1
        sumQ2All += Ans.q2
        sumQ3All += Ans.q3
        sumP1All += Ans.pr1
        sumP2All += Ans.pr2
        sumP3All += Ans.pr3
        sumP4All += Ans.pr4
        sumP5All += Ans.pr5
        sumP6All += Ans.pr6

        if Ans.prog == "CS":
            countCS +=1
            sumQ1CS += Ans.q1



    # Main
root= Tk()
root.title("Display Results")
app = DisplayResults(root)
root.mainloop()
