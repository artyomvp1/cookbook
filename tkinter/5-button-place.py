import tkinter as tk


root = tk.Tk()

root.geometry("800x500")
root.title("My First GUI")
textbox = tk.Text(root, height=3, font=("Arial", 18))
textbox.pack(padx=30)

# Just place a button in a certain position
button = tk.Button(root, text="TEST")
button.place(x=200, y=200, height=100, width=150)

root.mainloop()
