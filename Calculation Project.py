# Calculation Project
def addition(n1, n2):
    return n1 + n2

def division(n1, n2):
    return n1 / n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

calculation = {
    "+" : addition,
    "/" : division,
    "-" : subtraction,
    "*" : multiplication
}

number1 =  int(input("What's the first number? : "))
for symbol in calculation:
    print(symbol)

# 
calculation_continue = True
while calculation_continue:
    operations = input("Pick an Operation :\n")
    number2 =  int(input("What's the next number? : "))
    calculation_function = calculation[operations]
    answer = calculation_function(number1, number2)
    print(f"{number1} {operations} {number2} = {answer}")
    if input("Do you want to continue calclation type 'yes' or 'no'").lower().strip() == "yes":
        number1 = answer
    else:
        calculation_continue = False
        print(f"{number1} {operations} {number2} = {answer}")