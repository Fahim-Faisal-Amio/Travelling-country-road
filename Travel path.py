name = input("Please type your name: ")
print("Welcome", name, "to this journey!")

answer = input(
    "You are on a country road, it has come to a dead end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a mansion, you can enter or avoid? Type enter to enter the mansion and avoid to avoid the mansion: ")

    if answer == "enter":
        print("You entered and were bit by a snake.")
    elif answer == "avoid":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Invalid option. You lost.')

elif answer == "right":
    answer = input(
        "You come to a market, do you want to proceed it or head back (proceed/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "proceed":
        answer = input(
            "You entered the market and met a stranger. Do you want to talk to him (yes/no)? ")

        if answer == "yes":
            print("You talked to the stanger and he gave you gold. You WIN!")
        elif answer == "no":
            print("You ignored the stranger and you lost.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying",  name)
