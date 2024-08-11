def main():
    input1 = float(input("Enter the first number: "))
    input2 = float(input("Enter the second number: "))
    operator= input("Enter an operation (+, -, *, /,%): ")

    if operator == "+":
        print("The operation performed is addition:")
        result = input1 + input2
    elif operator== "-":
        print("The operation performed is subtraction:")
        result = input1 - input2
    elif operator== "*":
        print("The operation performed is multiplication")
        result = input1 * input2
    elif operator== "/":
        print("The operation performed is Division:")
        if input2 == 0:
            print("Cannot divide by zero!")
            return
        else:
            result = input1 / input2
    elif operator=="%":
        print("The operation performed is modulo")
        if input2==0:
             print("Cannot divide by zero!")
             return
        else:
              result=input1%input2
    else:
        print("Invalid operation!")
        return

    print("Result:", result)

if __name__ == "__main__":
    main()
