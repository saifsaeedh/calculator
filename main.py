import operations

print("==CALCULATOR V2.1==")
print("[INFO] Initializing Calculator")
print()
print("This is a basic calculator that can take two values and do one of the following operations")
print()

def show_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print()

def get_numbers():
    print("What is the first value?")
    a = float(input("Enter here: "))
    print(f"[DEBUG] a = {a}")
    print()
    while True:
        print("What is the second value? ")
        b = float(input("Enter here: "))
        if b == 0:
            print("[ERROR] Cannot divide a number by ZERO, try again")
            print()
        else:
            print(f"[DEBUG] b = {b}")
            print()
            break
    return a, b

while True:
    show_menu()
    print("Choose an option")
    choice = input("Enter here: ")
    if choice == "5":
        print("Goodbye!")
        break
    if choice in ["1", "2", "3", "4"]:
            a, b = get_numbers()
            if choice == "1":
                print(f"Result = {operations.add(a, b)}")

            elif choice == "2":
                print(f"Result = {operations.subtract(a, b)}")

            elif choice == "3":
                print(f"Result = {operations.multiply(a, b)}")

            elif choice == "4":
                print(f"Result = {operations.divide(a, b)}")
    else: 
        print("Invalid choice, try again")
        print()