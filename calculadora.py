import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("300x400")
        
        self.equation = tk.StringVar()
        self.create_widgets()
    
    def create_widgets(self):
        display_frame = tk.Frame(self.root)
        display_frame.pack()
        
        entry = tk.Entry(display_frame, textvariable=self.equation, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)
        
        buttons = [
            'C', '(', ')', '÷',
            '7', '8', '9', '×',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '+/-', '0', ',', '='
        ]
        
        button_frame = tk.Frame(self.root)
        button_frame.pack()
        
        row = 1
        col = 0
        
        for button in buttons:
            if button == 'C':
                btn = tk.Button(button_frame, text=button, padx=20, pady=20, font=('Arial', 18), command=self.clear)
            elif button == '=':
                btn = tk.Button(button_frame, text=button, padx=20, pady=20, font=('Arial', 18), command=self.calculate)
            elif button == '+/-':
                btn = tk.Button(button_frame, text=button, padx=20, pady=20, font=('Arial', 18), command=self.negate)
            else:
                btn = tk.Button(button_frame, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: self.add_to_equation(b))
            
            btn.grid(row=row, column=col, sticky="nsew")
            
            col += 1
            if col == 4:
                col = 0
                row += 1
        
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
    
    def add_to_equation(self, value):
        current_equation = self.equation.get()
        if value == '÷':
            value = '/'
        elif value == '×':
            value = '*'
        elif value == ',':
            value = '.'
        self.equation.set(current_equation + value)
    
    def clear(self):
        self.equation.set('')
    
    def negate(self):
        current_equation = self.equation.get()
        if current_equation and current_equation[0] == '-':
            self.equation.set(current_equation[1:])
        else:
            self.equation.set('-' + current_equation)
    
    def calculate(self):
        try:
            result = str(eval(self.equation.get()))
            self.equation.set(result)
        except:
            self.equation.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

