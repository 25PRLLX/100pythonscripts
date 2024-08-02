def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

def main():
    try:
        height = float(input("Please, enter your height in meters e.g 1.70: "))
        weight = float(input("Please, enter your weight in kilograms  e.g 72: "))

        bmi = calculate_bmi(height, weight)
        print(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")
    except ValueError:
        print("Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()