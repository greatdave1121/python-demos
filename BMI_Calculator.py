def BMI_Calculator(name, weight_kg, height_m):
    BMI = weight_kg/(height_m**2)
    print(f"{name}, your BMI is: {BMI:.2f}")

    if  BMI < 25:
        return "Not overweight."
    else:
        return "You're overweight."


print("This is the BMI Calculator\n")

print("What is your name?")
name = input()

print("What is your weight in Kilograms(Kg)?")
weight_kg = float(input())

print("What is your height in meters(M)?")
height_m = float(input())

print("\n")

print("Calculating BMI........\n\n")

BMI = BMI_Calculator(name, weight_kg, height_m)
print(BMI)


