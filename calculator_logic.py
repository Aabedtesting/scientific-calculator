import math

def evaluate_basic(expression: str):
    try:
        return eval(expression)
    except Exception:
        return "Error"

def evaluate_scientific(func: str, value):
    try:
        value = float(value)

        if func == "sin":
            return math.sin(math.radians(value))
        elif func == "cos":
            return math.cos(math.radians(value))
        elif func == "tan":
            return math.tan(math.radians(value))
        elif func == "log":
            return math.log10(value)
        elif func == "ln":
            return math.log(value)
        elif func == "sqrt":
            return math.sqrt(value)
        elif func == "exp":
            return math.exp(value)
        elif func == "pi":
            return math.pi
        elif func == "e":
            return math.e

        return "Error"
    except Exception:
        return "Error"
