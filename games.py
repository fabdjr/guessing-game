import number_guessing
import hangman

print("###########################################")
print("##       What do you want to play?       ##")
print("###########################################")
print("##   (1) Number Guessing  (2) Hangman    ##")
print("###########################################")

game = int(input("Select your game: "))

if game == 1:
    print("Playing Number Guessing...")
elif game == 2:
    print("Playing Hangman...")
