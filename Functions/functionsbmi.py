def calculate_BMI():
    weight = int(input("Enter your weight in kilograms"))
    height = float(input("Enter your height in metres"))
    BMI = weight/height **2
    print(f"Your BMI is{BMI}")
calculate_BMI()