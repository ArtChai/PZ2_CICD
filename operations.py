def calculate(a, b, operation):
    """
    функция выполняет сложение, вычитание или умножение двух чисел
    
    возможные операции: сложение (+), вычитание (-) и умножение (*)
    """
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
