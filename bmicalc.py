#enable user to enter input
weight = input("Enter your weight")
height = input("Enter your height")


weight = float(weight)
height = float(height)

#calculate bmi
bmi = weight/height**2
print("BMI is", bmi)

