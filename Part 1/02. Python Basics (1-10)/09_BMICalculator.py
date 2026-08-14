# BMI Calculator
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Your BMI is", bmi, "which means you are underweight.")
elif 18.5 <= bmi < 24.9:
    print("Your BMI is", bmi, "which means you have a normal weight.")
elif 25 <= bmi < 29.9:
    print("Your BMI is", bmi, "which means you are overweight.")
else:   
    print("Your BMI is", bmi, "which means you are obese.")
    