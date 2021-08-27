def calculator():
    try :
        num1 = int(input("Enter a number: \n>"))
        operator = input("Enter a operator(+-/* **): \n>")
        num2 = int(input("Enter another number: \n>"))
        if operator == "+":
            print(f"num1 + num2 = {num1 + num2}")
        elif operator == "-":
            print(f"num1 - num2 = {num1 - num2}")
        elif operator == "/":
            print(f"num1/ num2 = {num1/ num2}")
        elif operator == "*":
            print(f"num1* num2 = {num1* num2}")
        elif operator == "**":
            print(f"num1**num2 = {num1**num2}")
        else:
            print("Invalid mission")
    except Exception as e:
        print(e)