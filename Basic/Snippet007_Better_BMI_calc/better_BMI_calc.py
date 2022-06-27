height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = weight / height ** 2
BMI_rounded = round(BMI)

if BMI < 18.5:
    print(f"Your BMI is {BMI_rounded}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI_rounded}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI_rounded}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI_rounded}, you are obese.")
else:
    print(f"Your BMI is {BMI_rounded}, you are clinically obese.")
