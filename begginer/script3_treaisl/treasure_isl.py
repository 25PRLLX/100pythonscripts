print("Welcome to Treasure Island.\n Your mission is to find the treasure.\n")
left_right = input("You are at a cross road. Where do you want to go?\n Type 'Left' or 'Right' ").lower()

if left_right == "left":
    lake = input("You have come to a lake. There is an island in the middle of the lake\n Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if lake == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which colour do you choose?").lower()
        if door == "yellow":
            print("You win!")
        elif door == "red":
            print("Burned by fire. Game Over.")
        elif door == "lue":
            print("Eaten by beasts. Game Over.")
        else:
            print("You choose a door that doesn't exist. Game Over")
    else:
        print("Attacked by an angry trout. Game Over.")
else:
    print("You fell in to a hole. Game Over.")

