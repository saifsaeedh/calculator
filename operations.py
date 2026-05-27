#This module contains all the necessary operations needed for the calculator app.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("[ERROR] Cannot divide a value by 0")
    else:
        return a / b

