import random

def play():
    print("###########################################")
    print("##      Welcome to the Hangman Game      ##")
    print("###########################################")

    words_file = open("words.txt", "r")
    secret_words = [word.strip().upper() for word in words_file]
    words_file.close()

    secret_word = secret_words[random.randrange(0, len(secret_words))]
    masked_word = ["_"] * len(secret_word)
    attempts = 0

    hanged = False
    guessed = False

    print(masked_word)

    while not hanged and not guessed:
        chosen_letter = input("Choose a letter: ")
        chosen_letter = chosen_letter.strip().upper()

        index = 0
        if chosen_letter in secret_word:
            for letter in secret_word:
                if letter.upper() == chosen_letter:
                    masked_word[index] = letter
                index += 1
        else:
            attempts += 1
            print("There's no {} in whe word, you have {} attempts remaining".format(chosen_letter, 6 - attempts))

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
