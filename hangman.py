def play():
    print("###########################################")
    print("##      Welcome to the Hangman Game      ##")
    print("###########################################")

    secret_word = "banana"
    hanged = False
    guessed = False

    while(not hanged and not guessed):
        chosen_letter = input("Choose a letter: ")
        index = 0

        for letter in secret_word:
            if letter == chosen_letter:
                print("Found letter '{}' at {}".format(chosen_letter, index))

            index = index + 1

    print("###########################################")
    print("##              Game end!                ##")
    print("###########################################")


if __name__ == "__main__":
    play()
