from functions import make_file_into_list
import tkinter as tk
from tkinter import ttk

def display_results():
    # Create Tkinter window
    window = tk.Tk()
    window.title("TXT Results")

    # Create Treeview widget
    tree = ttk.Treeview(window)
    tree["columns"] = ("Result", "Value", "Conversion", "Amount")
    tree.heading("#0", text="Index")
    for i in tree["columns"]:
        tree.heading(i, text=i)
    # tree.heading("Result", text="Result")
    # tree.heading("Value", text="Value")
    # tree.heading("Conversion", text="Conversion")

    # Read CSV file
    reader = make_file_into_list()
    reader.pop(0)
    for index, row in enumerate(reader):
        tree.insert("", tk.END, text=index, values=row)

    # Pack the Treeview widget
    tree.pack()

    # Start the Tkinter event loop
    window.mainloop()


# Call the function to display the results
display_results()
