import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)

for guess in range(1, top_of_range + 1):
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        result = "You were above the number!" if user_guess > random_number else "You were below the number!"

        if user_guess == random_number:
            print("You got it")
            print("You got it in", guess, "guess")
            break
        else:
            print(result)
    else:
        print("Please type a number next time.")
