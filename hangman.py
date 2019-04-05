def play():
    print("###########################################")
    print("##      Welcome to the Hangman Game      ##")
    print("###########################################")

    secret_word = "banana"
    masked_word = ["_", "_", "_", "_", "_", "_"]

    hanged = False
    guessed = False

    while(not hanged and not guessed):
        print(masked_word)
        chosen_letter = input("Choose a letter: ")
        chosen_letter = chosen_letter.strip()
        index = 0

        for letter in secret_word:
            if letter.upper() == chosen_letter.upper():
                masked_word[index] = letter.upper()

            index = index + 1

    print("###########################################")
    print("##              Game end!                ##")
    print("###########################################")


if __name__ == "__main__":
    play()
