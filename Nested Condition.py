height = float(input("Please enter your height: "))
age = int(input("Enter your age: "))
if height > 120:
    if age < 12 :
        print("You can Play, and payment $5")
    elif age <= 18:
        print("You can Play, and payment $7")
    else:
        print("You can Play, and payment $12")
else:
    print("Sorry can't play due to your height")