def play():
    print("###########################################")
    print("##      Welcome to the Hangman Game      ##")
    print("###########################################")

    secret_word = "banana"
    masked_word = ["_", "_", "_", "_", "_", "_"]
    attempts = 0

    hanged = False
    guessed = False

    print(masked_word)

    while(not hanged and not guessed):


        chosen_letter = input("Choose a letter: ")
        chosen_letter = chosen_letter.strip()

        index = 0
        if chosen_letter.upper() in secret_word.upper():
            for letter in secret_word:
                if letter.upper() == chosen_letter.upper():
                    masked_word[index] = letter.upper()
                index += 1
        else:
            attempts += 1

        print(masked_word)

        hanged = attempts == 6
        guessed = "_" not in masked_word

    print("###########################################")
    if guessed:
        print("##              YOU WIN!                 ##")
    else:
        print("##              GAME OVER                ##")
    print("###########################################")


if __name__ == "__main__":
    play()
