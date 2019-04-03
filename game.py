print("####################################")
print("##  Welcome to the Guessing Game  ##")
print("####################################")

secret_number = 42
round = 1
rounds_limit = 3

while(round <= rounds_limit):
    print("Round", round, "from", rounds_limit)

    guessing_number_str = input("Take a good guess: ")
    print("You choose: ", guessing_number_str)

    # typecast is required as long as input() returns a str
    guessing_number = int(guessing_number_str)

    guessing_is_correct = guessing_number == secret_number
    guessing_is_higher = guessing_number > secret_number
    guessing_is_lower = guessing_number < secret_number

    if guessing_is_correct:
        print("WOW! You guessed it!")
    else:
        if(guessing_is_higher):
            print("OPS! Not this time: your guessing is HIGHER than the secret number.")
        elif(guessing_is_lower): # this line doesn't make any logic sense, just for syntax demonstration
            print("OPS! Not this time: your guessing is LOWER than the secret number.")

    round = round + 1

    print("####################################")

print("Game end!")