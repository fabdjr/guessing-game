import random

def play():
    show_welcome_message()

    secret_word = pick_secret_word()
    masked_word = create_word_mask(secret_word)

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


def show_welcome_message():
    print("###########################################")
    print("##      Welcome to the Hangman Game      ##")
    print("###########################################")


def pick_secret_word():
    words_file = open("words.txt")
    secret_words = [word.strip().upper() for word in words_file]
    words_file.close()

    return secret_words[random.randrange(0, len(secret_words))]


def create_word_mask(secret_word):
    return ["_"] * len(secret_word)


if __name__ == "__main__":
    play()
