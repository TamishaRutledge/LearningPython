import random

print("The Guessing Game!") 
# randint function to generate the  
# random number b/w 0 to 21 
number = random.randint(0,21)


# number of attempts to be given  
# to the user to guess the number     
# total of 5 attempts 
attempts = 0

name = input('Hello there, what is your name?\n')
print('Greetings ' + name + ', what number between 1 and 20 am I thinking of?\n')
# A while loop is used to track the guess attempts
while attempts < 5:

    guess = int(input())

    # Comparing the number entered with
    # the number to be guessed
    if guess == number:
        # If the number matches we break
        # out of the loop with break stmt
        print('Congrats! You guessed it!')
        break

    elif guess < number:
        # Checking if the number is too low
        print('Guess is too low, pick something higher than', guess)
    else:
        # Checking if the number is too high
        print('Guess is too high, pick something lower than', guess)

    # Increase the value of chances by 1
    attempts += 1

if not attempts < 5:
    print('Out of chances! The number is', number)
