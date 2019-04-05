def play():
    print("###########################################")
    print("##      Welcome to the Hangman Game      ##")
    print("###########################################")

    secret_word = "banana"
    hanged = False
    guessed = False

    while(not hanged and not guessed):
        letter = input("Choose a letter: ")
        print("Playing...")

    print("###########################################")
    print("##              Game end!                ##")
    print("###########################################")


if __name__ == "__main__":
    play()
