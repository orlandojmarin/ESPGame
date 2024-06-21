# Write a program that tests your ESP (extrasensory perception). The program
# should randomly select the name of a color from the following list of words:
# Red, Green, Blue, Orange, Yellow
# To select a word, the program can generate a random number. For example, if
# the number is 0, the selected word is Red, if the number is 1, the selected
# word is Green, and so forth.
# Next, the program should ask the user to enter the color that the computer
# has selected. After the user has entered their guess, the program should
# display the name of the randomly selected color. The program should repeat
# this 10 times and then display the number of times the user correctly guessed
# the selected color.

# import random module
import random

# initialize correct guesses variable to 0
correct_guesses = 0

print("The color choices are: Red, Green, Blue, Orange, or Yellow.")

# create a for loop that will generate a random number and ask the user to 
# guess what it is. Repeat 10 times and count how many times the user guesses
# correctly
for count in range(10): 
    
    # generate a random number from 0 to 4
    random_number = random.randint(0, 4)
    
    # each number corresponds with a computer color
    if random_number == 0:
        computer_color = "RED"
    elif random_number == 1:
        computer_color = "GREEN"
    elif random_number == 2:
        computer_color = "BLUE"
    elif random_number == 3:
        computer_color = "ORANGE"
    elif random_number == 4:
        computer_color = "YELLOW"
    
    # ask for user input on what color they think the computer chose
    user_color_guess = input("\nEnter the color that you think the computer selected? ").upper()
    
    # input validation
    while (user_color_guess != "RED" and user_color_guess != "GREEN" and user_color_guess != "BLUE" and user_color_guess != "ORANGE" and user_color_guess != "YELLOW"):
        print("\nThe response you entered is not an available option (Red, Green, Blue, Orange, or Yellow).")
        user_color_guess = input("Enter the color that you think the computer selected? ").upper()
    
    # count the number of correct guesses
    if user_color_guess == computer_color:
        correct_guesses += 1
    
    # keep track of the guess number and correct computer colors
    print(f"\nGuess # {count + 1}: {user_color_guess}")
    print(f"Correct Computer Color: {computer_color}")

# print the results
print("\nThank you for playing!")
print(f"Correct Guesses: {correct_guesses}")


