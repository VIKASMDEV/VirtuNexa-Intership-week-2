import tkinter as tk
from tkinter import messagebox

# Arithmetic functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Calculator with Result Button")

        self.entry1 = tk.Entry(root, width=10)
        self.entry2 = tk.Entry(root, width=10)
        self.entry1.grid(row=0, column=0, padx=10, pady=10)
        self.entry2.grid(row=0, column=2, padx=10, pady=10)

        self.selected_operator = tk.StringVar()

        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.grid(row=1, column=1, pady=10)

        # Operation buttons
        tk.Button(root, text="+", width=5, command=lambda: self.set_operator("+")).grid(row=2, column=0)
        tk.Button(root, text="-", width=5, command=lambda: self.set_operator("-")).grid(row=2, column=1)
        tk.Button(root, text="*", width=5, command=lambda: self.set_operator("*")).grid(row=2, column=2)
        tk.Button(root, text="/", width=5, command=lambda: self.set_operator("/")).grid(row=2, column=3)

        # Result button
        tk.Button(root, text="Result", width=20, command=self.calculate_result).grid(row=3, column=0, columnspan=4, pady=10)

    def set_operator(self, op):
        self.selected_operator.set(op)
        self.result_label.config(text=f"Selected: {op}")

    def calculate_result(self):
        try:
            op = self.selected_operator.get()
            if not op:
                messagebox.showwarning("Warning", "Please select an operation first.")
                return

            x = float(self.entry1.get())
            y = float(self.entry2.get())
            result = operations[op](x, y)
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
