# "Your BMI is 18, you are underweight."
# "Your BMI is 22, you have a normal weight."
# "Your BMI is 28, you are slightly overweight."
# "Your BMI is 33, you are obese."
# "Your BMI is 40, you are clinically obese."
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi  = round(weight / height ** 2)
bmi_int = int(bmi)
if bmi_int < 18.5:
    print(f"Your BMI is {bmi_int}, you are underweight.")
elif bmi_int < 25:
    print(f"Your BMI is {bmi_int}, you have a normal weight.")
elif bmi_int < 30:
    print(f"Your BMI is {bmi_int}, you are slightly overweight.")
elif bmi_int > 35:
    print(f"Your BMI is {bmi_int}, you are obese.")
else:
    print(f"Your BMI is {bmi_int}, you are clinically obese.")
