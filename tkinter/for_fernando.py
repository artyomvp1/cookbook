import random
from tkinter import *


root = Tk()
root.geometry("300x200")
root.title(" WORKOUT ")


def plan():
    push1 = "\n:::TODAY IS A PUSH WORKOUT:::\n---\nBench press 3x10\nOverhead press 3x12\nTricep pushdown 3x12\nLeg press 3x10\n"
    push2 = "\n:::TODAY IS A PUSH WORKOUT:::\n---\nIncline bench press 3x10\nDumbbell shoulder press 3x12\nTricep pushdown 3x12\nSquats 3x10\n"
    pull1 = "\n:::TODAY IS A PULL WORKOUT:::\n---\nPull down 3x12\nBarbell row 3x12\nFace pull 3x12\nBicep Curl 3x10\n"
    pull2 = "\n:::TODAY IS A PULL WORKOUT:::\n---\nLateral raise 3x12\nDumbbell row 3x12\nPull ups 3x12\nHammer Curl 3x10\n"
    rest = "\nTODAY YOU TAKE A REST MR. FERNANDO!\n"
    sequence = [push1, push2, pull1, pull2, rest]
    result = random.choice(sequence)
    output.insert(1.0, result)
    print('Done')


def clear():
    output.delete(1.0, END)


button = Button(root, height=2, width=4, text='Go!', command=lambda: [clear(), plan()])
button.pack()

output = Text(root, height=100, width=100, bg="light cyan")
output.pack()

mainloop()
