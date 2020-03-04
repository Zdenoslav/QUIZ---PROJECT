# Part
part_text = StringVar()
part_label = Label(app, text='MULTIPLE CHOICE', font=('bold', 14), pady=20)
part_label.grid(row=1, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=1, column=1)
