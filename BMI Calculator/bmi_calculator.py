# BMI Calculator

height = input("Enter your height in m: ")
weight = input("Enter youw weight in kg: ")

BMI = float(weight) / float(height)**2

if BMI < 18.5:
    print(f"Your BMI is {float(BMI):.1f}. You are Underweight!")
elif BMI >= 18.5 and BMI <= 24.9:
    print(f"Your BMI is {float(BMI):.1f}. You are in Normal Weight category!")
elif BMI >= 25 and BMI <= 29.9:
    print(f"Your BMI is {float(BMI):.1f}. You are in Overweight category!")
else: 
    print(f"Your BMI is {float(BMI):.1f}. You are in Obese category!") 