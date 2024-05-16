import tkinter as tk


root = tk.Tk()

root.geometry("800x500")
root.title("My First GUI")

textbox = tk.Text(root, height=3, font=("Arial", 18))  # Creating a textbox for input. Height - height of the textbox
textbox.pack(padx=30)  # resolution

entry = tk.Entry()  # entry
entry.pack()

root.mainloop()
