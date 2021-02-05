#Nested Condition
height = float(input("Please enter your height: "))
age = int(input("Enter your age: "))
if height > 120:
    if age < 12 :
        bill = 5
        print("You can Play, and payment $5")
    elif age <= 18:
        bill = 7
        print("You can Play, and payment $7")
    else:
        bill = 12
        print("You can Play, and payment $12")
    want_photo = input("Do you want a photo taken? Y or N \n").capitalize()
    if want_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry can't play due to your height")