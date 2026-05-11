import tkinter as tk

def click(button_value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(button_value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry. insert(0, "Error")

root = tk.Tk()
root.title("calculator")

entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
           ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
           ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
           ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text == "C":
        action = clear
    elif text == "=":
        action = calculate
    else:
        action = lambda x=text: click(x)

    tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),command=action). grid(row=row, column=col)

root.mainloop()

