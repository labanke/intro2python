#enable user to enter input
weight = input("Enter your weight")
height = input("Enter your height")


weight = float(weight)
height = float(height)

#calculate bmi
bmi = weight/height**2
print("BMI is", bmi)

if bmi <= 18.0:
    print("You are underweight")
elif bmi <= 29.0:
    print("Normal weight")
elif bmi <= 34.0:
    print("Overweight")
else:
    print("You are obese")