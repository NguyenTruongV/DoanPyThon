import tkinter as tk
import math

# Tạo cửa sổ chính
app = tk.Tk()
app.title("Calculator")
app.geometry("350x500")

# Biến toàn cục cho biểu thức đầu vào
expression = ""

# Chức năng cập nhật biểu thức trong hộp nhập
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Hàm đánh giá biểu thức
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except Exception as e:
        equation.set("Error")
        expression = ""

# Chức năng xóa ô nhập
def clear():
    global expression
    expression = ""
    equation.set("")

# Hàm tính căn bậc hai
def sqrt():
    global expression
    try:
        result = str(math.sqrt(eval(expression)))
        equation.set(result)
        expression = result
    except Exception:
        equation.set("Error")
        expression = ""

# Hàm tính bình phương
def square():
    global expression
    try:
        result = str(eval(expression) ** 2)
        equation.set(result)
        expression = result
    except Exception:
        equation.set("Error")
        expression = ""

# Hàm tính giai thừa
def factorial():
    global expression
    try:
        result = str(math.factorial(int(eval(expression))))
        equation.set(result)
        expression = result
    except Exception:
        equation.set("Error")
        expression = ""


# Chức năng chuyển đổi dấu hiệu
def toggle_sign():
    global expression
    try:
        result = str(-1 * eval(expression))
        equation.set(result)
        expression = result
    except Exception:
        equation.set("Error")
        expression = ""

# Hàm chèn số π
def insert_pi():
    global expression
    expression += str(math.pi)
    equation.set(expression)

# Chức năng chèn e
def insert_e():
    global expression
    expression += str(math.e)
    equation.set(expression)


# Ô nhập máy tính
equation = tk.StringVar()
entry = tk.Entry(app, textvariable=equation, font=("Arial", 18), bd=10, insertwidth=4, width=18, borderwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/', '√',
    '4', '5', '6', '*', 'x²',
    '1', '2', '3', '-', '±',
    '%', '0', 'e', '+', 
    'π', '=', 'X'
]

# Button commands
commands = {
    '√': sqrt,
    'x²': square,
    '±': toggle_sign,
    'π': insert_pi,
    'e': insert_e,
    '%': lambda: press("/100")
}

# Create buttons 
row_val = 1
col_val = 0
for button in buttons:
    if button in commands:
        tk.Button(app, text=button, padx=20, pady=20, font=("Arial", 14),
                  command=commands[button]).grid(row=row_val, column=col_val)
    elif button == "=":
        tk.Button(app, text=button, padx=20, pady=20, font=("Arial", 14), bg="lightgreen",
                  command=equalpress).grid(row=row_val, column=col_val)
    elif button == "X":
        tk.Button(app, text=button, padx=20, pady=20, font=("Arial", 14), bg="red",
                  command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(app, text=button, padx=20, pady=20, font=("Arial", 14),
                  command=lambda b=button: press(b)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

app.mainloop()