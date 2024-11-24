import tkinter as tk
from tkinter import messagebox
import re

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.current_expression = ""
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display Screen
        display = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10)

        # Adjust row and column weights
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        if button_text == "C":
            self.current_expression = ""
            self.result_var.set("")
        elif button_text == "=":
            try:
                # Check for invalid expressions (like consecutive operators)
                if re.search(r"[+\-*/]{2,}", self.current_expression):  # two or more consecutive operators
                    raise SyntaxError("Invalid expression")
                
                # Evaluate the expression
                result = eval(self.current_expression)
                # Convert to int if the result is a whole number (no decimal)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.result_var.set(result)
                self.current_expression = str(result)
            except (SyntaxError, ZeroDivisionError, NameError) as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.current_expression = ""
                self.result_var.set("")
        else:
            # Update the current expression
            self.current_expression += button_text
            self.result_var.set(self.current_expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
