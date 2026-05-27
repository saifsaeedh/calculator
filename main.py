import operations

print("==CALCULATOR V1.2==")
print("[INFO] Initializing Calculator")
print()

print("This is a basic calculator that can take two values and do one of the following operations")
print()

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")
print()

print("Which of these operations do you want to do?")
op = input("Enter Here: ")
print(f"[DEBUG] op = {op}")
print()

print("What is the first value?")
num1 = float(input("Enter here: "))
print(f"[DEBUG] num1 = {num1}")
print()


while True:
    print("What is the second value? ")
    num2 = float(input("Enter here: "))
    if num2 == 0:
        print("[ERROR] Cannot divide a number by ZERO, try again")
        print()
    else:
        print(f"[DEBUG] num2= {num2}")
        print()
        break

if op == "1":
    result = operations.add(num1, num2)

elif op == "2":
    result = operations.subtract(num1, num2)

elif op == "3":
    result = operations.multiply(num1, num2)

elif op == "4":
    result = operations.divide(num1, num2)

print(f"[DEBUG] Result = {result}")
print(f"Result: {result}")