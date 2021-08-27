from moduleOfCalculator import calculator
calculator()
y = input("Do you want to calculate again?(Y//N): ").lower()
if y == "y":
    calculator()
else:
    print("Thank's for using me.")