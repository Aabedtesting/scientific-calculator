import tkinter as tk
from tkinter import ttk
import math

# --- Functions ---
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = str(screen.get())
            result = eval(expression)
            screen.delete(0, tk.END)
            screen.insert(0, result)
        except Exception:
            screen.delete(0, tk.END)
            screen.insert(0, "Error")
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

def sci_click(func):
    try:
        expression = screen.get()
        value = float(eval(expression))
        result = None

        if func == "sin":
            result = math.sin(math.radians(value))
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "tan":
            result = math.tan(math.radians(value))
        elif func == "log":
            result = math.log10(value)
        elif func == "ln":
            result = math.log(value)
        elif func == "sqrt":
            result = math.sqrt(value)
        elif func == "exp":
            result = math.exp(value)
        elif func == "pi":
            result = math.pi
        elif func == "e":
            result = math.e

        screen.delete(0, tk.END)
        screen.insert(0, result)
    except Exception:
        screen.delete(0, tk.END)
        screen.insert(0, "Error")

# --- Main Window ---
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")

tab_control = ttk.Notebook(root)
basic_tab = ttk.Frame(tab_control)
sci_tab = ttk.Frame(tab_control)

tab_control.add(basic_tab, text="Basic")
tab_control.add(sci_tab, text="Scientific")
tab_control.pack(expand=1, fill="both")

# --- Display ---
screen = tk.Entry(basic_tab, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify="right")
screen.pack(fill=tk.X, padx=10, pady=10)

# --- Basic Buttons ---
basic_buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

for row in basic_buttons:
    frame = tk.Frame(basic_tab)
    frame.pack(expand=True, fill="both")
    for text in row:
        button = tk.Button(frame, text=text, font="Arial 18", relief=tk.GROOVE)
        button.pack(side=tk.LEFT, expand=True, fill="both")
        button.bind("<Button-1>", click)

# --- Scientific Buttons ---
sci_screen = screen  # reuse the same display
sci_buttons = [
    ["sin", "cos", "tan"],
    ["log", "ln", "sqrt"],
    ["exp", "pi", "e"]
]

for row in sci_buttons:
    frame = tk.Frame(sci_tab)
    frame.pack(expand=True, fill="both")
    for text in row:
        button = tk.Button(frame, text=text, font="Arial 18", relief=tk.GROOVE",
                           command=lambda t=text: sci_click(t))
        button.pack(side=tk.LEFT, expand=True, fill="both")

root.mainloop()
