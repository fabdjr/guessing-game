print("####################################")
print("##  Welcome to the Guessing Game  ##")
print("####################################")

secret_number = 42

guessing_number_str = input("Take a good guess: ")
print("You choose: ", guessing_number_str)

# typecast is required as long as input() returns a str
guessing_number = int(guessing_number_str)

if secret_number == guessing_number:
    print("WOW! You guessed it!")
else:
    print("OPS! Not this time!")
