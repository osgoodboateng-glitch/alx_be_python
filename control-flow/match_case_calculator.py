num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Choose the operation(+, -, *, /): ")
match operation:
    case "+":
        print(f"The result is {num1+num2}.")
    case "-":
        print(f"The result is {num1-num2}.")
    case "*":
        print(f"The result is {num1*num2}.")
    case "divide":
            try:
                print(f"The result is {num1/num2}.")
            except ZeroDivisionError:
                print("Cannot divide by zero.")
    case _:
            print("Unknown operation")
