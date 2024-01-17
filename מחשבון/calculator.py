import tkinter as tk

def on_click(character):
    current = entry.get()
    if character == "." and "." in current:
        return
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(character))

def on_clear():
    entry.delete(0, tk.END)

def on_operation(operator):
    global first_number
    global operation
    try:
        first_number = float(entry.get())
        operation = operator
        entry.delete(0, tk.END)
    except ValueError:
        pass

def on_equal():
    try:
        second_number = float(entry.get())
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            result = first_number / second_number
        entry.delete(0, tk.END)
        if result.is_integer():
            result = int(result)
        entry.insert(tk.END, str(result))
    except (ValueError, ZeroDivisionError):
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("👨🏻‍💻 מחשבון")

entry = tk.Entry(window, width=12, font=('Verdana', 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_color = "#333333"
operation_color = "#4CAF50"
clear_color = "#f44336"

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('C', 4, 0), ('.', 4, 1), ('0', 4, 2),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3),
    ('/', 3, 3), ('=', 4, 3)
]

for text, row, col in buttons:
    btn_color = button_color if text not in "+-*/=" else operation_color
    btn_color = clear_color if text == 'C' else btn_color
    button = tk.Button(window, text=text, padx=20, pady=10, font=('Verdana', 14), bg=btn_color, fg='white', relief="ridge", border=6, command=lambda t=text: on_click(t) if t.isnumeric() or t == '.' else on_clear() if t == 'C' else on_operation(t) if t in "+-*/" else on_equal())
    button.grid(row=row, column=col, padx=1, pady=1)

first_number = None
operation = None

window.mainloop()
