from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

root = Tk()
root.title("Expense Tracker")

# function to submit the expense details
def submit_expense():
    values = [date_entry.get(), name_entry.get(), title_entry.get(), expense_entry.get()]
    Etable.insert('', 'end', values=values)

# function to view all the saved expenses
def view_expenses():
    # code to retrieve data from database and display in treeview widget
    pass

# create the UI elements
date_label = Label(root, text="Date", font=('Arial', 14))
date_label.grid(row=0, column=0, padx=5, pady=5)
date_entry = DateEntry(root, font=('Arial', 14))
date_entry.grid(row=0, column=1, padx=5, pady=5)

name_label = Label(root, text="Name", font=('Arial', 14))
name_label.grid(row=1, column=0, padx=5, pady=5)
name_entry = Entry(root, font=('Arial', 14))
name_entry.grid(row=1, column=1, padx=5, pady=5)

title_label = Label(root, text="Title", font=('Arial', 14))
title_label.grid(row=2, column=0, padx=5, pady=5)
title_entry = Entry(root, font=('Arial', 14))
title_entry.grid(row=2, column=1, padx=5, pady=5)

expense_label = Label(root, text="Expense", font=('Arial', 14))
expense_label.grid(row=3, column=0, padx=5, pady=5)
expense_entry = Entry(root, font=('Arial', 14))
expense_entry.grid(row=3, column=1, padx=5, pady=5)

submit_button = Button(root, text="Submit", font=('Arial', 14), command=submit_expense)
submit_button.grid(row=4, column=0, padx=5, pady=5)

view_button = Button(root, text="View Expenses", font=('Arial', 14), command=view_expenses)
view_button.grid(row=4, column=1, padx=5, pady=5)

# create a treeview widget to display all saved expenses
Elist = ['Date', 'Name', 'Title', 'Expense']
Etable = ttk.Treeview(root, columns=Elist, show='headings', height=7)
for c in Elist:
    Etable.heading(c, text=c.title())
Etable.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

root.mainloop()
