import tkinter as tk
from tkinter import ttk

def create_form():
    root = tk.Tk()
    root.title("Data Entry Form")
    root.geometry("500x400")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text="User Information").grid(column=0, row=0, columnspan=3, sticky=tk.W)

    ttk.Label(frame, text="First Name").grid(column=0, row=1, sticky=tk.W)
    ttk.Entry(frame).grid(column=0, row=2, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Last Name").grid(column=1, row=1, sticky=tk.W)
    ttk.Entry(frame).grid(column=1, row=2, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Title").grid(column=2, row=1, sticky=tk.W)
    ttk.Combobox(frame).grid(column=2, row=2, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Age").grid(column=0, row=3, sticky=tk.W)
    ttk.Spinbox(frame, from_=18, to=100).grid(column=0, row=4, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Nationality").grid(column=1, row=3, sticky=tk.W)
    ttk.Entry(frame).grid(column=1, row=4, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Registration Status").grid(column=0, row=5, columnspan=3, sticky=tk.W)
    ttk.Checkbutton(frame, text="Currently Registered").grid(column=0, row=6, sticky=tk.W)

    ttk.Label(frame, text="# Completed Courses").grid(column=1, row=6, sticky=tk.W)
    ttk.Spinbox(frame, from_=0, to=100).grid(column=1, row=7, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="# Semesters").grid(column=2, row=6, sticky=tk.W)
    ttk.Spinbox(frame, from_=0, to=20).grid(column=2, row=7, sticky=(tk.W, tk.E))

    ttk.Label(frame, text="Terms & Conditions").grid(column=0, row=8, columnspan=3, sticky=tk.W)
    ttk.Checkbutton(frame, text="I accept the terms and conditions.").grid(column=0, row=9, columnspan=3, sticky=tk.W)

    ttk.Button(frame, text="Enter data").grid(column=1, row=10, sticky=tk.E)

    for child in frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_form()