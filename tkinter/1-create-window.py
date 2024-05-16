import tkinter as tk


root = tk.Tk()

root.geometry("800x500")    # Resolution
root.title("My First GUI")    # Title

label = tk.Label(root,
                 text="Hello",
                 font=("Arial", 22))
label.pack(padx=20, pady=30)  # Location of the label?

root.mainloop()
