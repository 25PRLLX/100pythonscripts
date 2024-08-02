def evaluate_tip(bill, tip):
    if tip == 10:
        total_bill = bill * 1.10
        return total_bill
    elif tip == 12:
        total_bill = bill * 1.12
        return total_bill
    elif tip == 15:
        total_bill = bill * 1.15
        return total_bill
    else:
        print("The tip percentage is not recognized.")
        return None

def main():
    try:
        bill = float(input("What was the total bill?\n"))
        tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
        split = int(input("How many people to split the bill?\n"))

        total_bill = evaluate_tip(bill, tip)
        if total_bill is not None:
            splited_bill = total_bill / split
            print(f"The value each one needs to pay is: ${splited_bill:.2f}.")
        else:
            print("Please enter a valid tip percentage (10, 12, or 15).")
    except ValueError:
        print("Please enter valid numerical values for the bill, tip, and split.")

if __name__ == "__main__":
    main()
