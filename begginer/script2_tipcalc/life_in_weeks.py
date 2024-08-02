def calculate_life_in_weeks(age):
    years = 90 - int(age)
    weeks = years * 52
    return weeks

def main():
    age = int(input("How old are you in years (e.g., 18): "))
    weeks_remaining = calculate_life_in_weeks(age)
    print(f"You have {weeks_remaining} weeks remaining ultil you are 90 years old")

if __name__ == "__main__":
    main()
