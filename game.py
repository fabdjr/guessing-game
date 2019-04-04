import random

secret_number = random.randrange(1, 101)

print("####################################")
print("##  Welcome to the Guessing Game  ##")
print("####################################")
print("## (1) Easy  (2) Medium  (3) Hard ##")
print("####################################")

level_str = input("Select your level: ")
level = int(level_str)

if level == 1:
    rounds_limit = 20
elif level == 2:
    rounds_limit = 10
else:
    rounds_limit = 5

for current_round in range(1, rounds_limit + 1):
    print("####################################")
    print("Round {} from {}".format(current_round, rounds_limit))

    guessing_number_str = input("Take a good guess (between 1 and 100): ")
    print("Your guess: ", guessing_number_str)

    # typecast is required as long as input() returns a str
    guessing_number = int(guessing_number_str)

    if guessing_number < 1 or guessing_number > 100:
        print("Your guess should be between 1 and 100!")
        continue

    guessing_is_correct = guessing_number == secret_number
    guessing_is_higher = guessing_number > secret_number
    guessing_is_lower = guessing_number < secret_number

    if guessing_is_correct:
        print("WOW! You guessed it!")
        break
    else:
        if guessing_is_higher:
            print("OPS! Not this time: your guessing is HIGHER than the secret number.")
        elif guessing_is_lower:  # this line doesn't make any logic sense, just for syntax demonstration
            print("OPS! Not this time: your guessing is LOWER than the secret number.")


print("####################################")
print("##           Game end!            ##")
print("####################################")