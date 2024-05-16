import tkinter as tk


root = tk.Tk()

root.geometry("800x500")
root.title("My First GUI")

textbox = tk.Text(root, height=3, font=("Arial", 18))
textbox.pack(padx=30)

button = tk.Button(root, text="Click Me!", font=("Arial", 14))    # button and text
button.pack(padx=10, pady=10)

root.mainloop()
