print("==CALCULATOR V1==")
print()

print("This is a basic calculator that can take two values and do one of the following operations")
print()

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print()

print("Which of these operations do you want to do?")
op = input(str("Enter Here: "))
print()

print("What is the first value?")
num1 = int(input("Enter here: "))
print()
print("What is the second value? ")
num2 = int(input("Enter here: "))
print()

if op == "1":
    result = num1 + num2

elif op == "2":
    result = num1 - num2

elif op == "3":
    result = num1 * num2

elif op == "4":
    result = num1 / num2


print(f"Result: {result}")