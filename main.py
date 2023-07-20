import random

print("Welcome to the Number Guessing Game!")
print("You have to guess a number between 0 and an upper limit.")
print("You have 5 attempts to guess the correct number. Good luck!\n")

top_of_range = input("Type the upper limit of the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = [] 

for guess in range(1, 6):  # Limit the user to 5 guesses
    user_guess = input("Attempt {}/5 - Make a guess: ".format(guess))

    if user_guess.isdigit():
        user_guess = int(user_guess)
        result = "You were above the number!" if user_guess > random_number else "You were below the number!"

        if user_guess == random_number:
            print("Congratulations! You guessed it!")
            print("You guessed it in", guess, "attempt(s).")
            break
        else:
            print(result)
            guesses.append(user_guess)  
    else:
        print("Please type a number next time.")

if random_number not in guesses:
    print("You lost! The number was", random_number)
