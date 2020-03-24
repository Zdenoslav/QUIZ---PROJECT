from tkinter import *

root = Tk()
root.title("Amending Questions")
root.geometry('650x300')

title = Label(root, text="Confirm Quiz Questions", font=("MS", 25, "bold")).grid(row=0, column=3)

Label3 = Label(root, text="Questions", font=("MS", 18, "bold")).grid(row=2, column=0)
Label4 = Label(root, text="Question 1 content ").grid(row=3, column=0)
Label5 = Label(root, text="Question 2 content ").grid(row=4, column=0)
Label6 = Label(root, text="Question 3 content ").grid(row=5, column=0)
Label7 = Label(root, text="Question 4 content ").grid(row=6, column=0)
Label8 = Label(root, text="Question 5 content ").grid(row=7, column=0)


Label2 = Button(root, text="Back to change quiz type").grid(row=1, column=0)

buttom1 = Button(root, text="Edit").grid(row=3, column=2)
buttom2 = Button(root, text="Edit").grid(row=4, column=2)
buttom3 = Button(root, text="Edit").grid(row=5, column=2)
buttom4 = Button(root, text="Edit").grid(row=6, column=2)
buttom5 = Button(root, text="Edit").grid(row=7, column=2)

# def click_add():

buttom6 = Button(root, text="Add").grid(row=8, column=2)

# def click_remove():

buttom7 = Button(root, text="Remove").grid(row=8, column=3)

# def click_confirm():
buttom8 = Button(root, text="Confirm & Start", font=("MS", 15, "bold")).grid(row=10, column=4)


root.mainloop()