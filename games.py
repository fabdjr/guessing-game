import number_guessing
import hangman

def select_game():
    print("###########################################")
    print("##       What do you want to play?       ##")
    print("###########################################")
    print("##   (1) Number Guessing  (2) Hangman    ##")
    print("###########################################")

    game = int(input("Select your game: "))

    if game == 1:
        number_guessing.play()
    elif game == 2:
        hangman.play()

if __name__ == "__main__":
    play()