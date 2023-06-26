#enable user to enter input
weight = input("Enter your weight")
height = input("Enter your height")

#convert variables to integer
weight = int(weight)
height = int(height)

#calculate bmi
bmi = weight/height**2
print("BMI is", bmi)

