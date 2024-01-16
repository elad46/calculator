import tkinter as tk

def on_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def on_clear():
    entry.delete(0, tk.END)

def on_operation(operator):
    global first_number
    global operation
    first_number = int(entry.get())
    operation = operator
    entry.delete(0, tk.END)

def on_equal():
    second_number = int(entry.get())
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))

window = tk.Tk()
window.title("מחשבון")

# תיבת קלט
entry = tk.Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3), ('=', 4, 2),
    ('C', 4, 0),
]
for text, row, col in buttons:
    button = tk.Button(window, text=text, padx=40, pady=20, command=lambda t=text: on_click(t) if t.isnumeric() else on_clear() if t == 'C' else on_operation(t) if t in "+-*/" else on_equal())
    button.grid(row=row, column=col)

first_number = None
operation = None

window.mainloop()