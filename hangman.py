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
        chosen_letter = ask_for_guess()

        if chosen_letter in secret_word:
            mark_guessed_letters(chosen_letter, secret_word, masked_word)
        else:
            attempts += 1
            print("There's no {} in whe word, you have {} attempts remaining".format(chosen_letter, 6 - attempts))

        print(masked_word)

        hanged = attempts == 6
        guessed = "_" not in masked_word

    show_end_message(guessed)


def show_welcome_message():
    print("###########################################")
    print("##      Welcome to the Hangman Game      ##")
    print("###########################################")


def show_end_message(guessed):
    print("###########################################")
    if guessed:
        print("##              YOU WIN!                 ##")
    else:
        print("##              GAME OVER                ##")
    print("###########################################")


def pick_secret_word():
    words_file = open("words.txt")
    secret_words = [word.strip().upper() for word in words_file]
    words_file.close()

    return secret_words[random.randrange(0, len(secret_words))]


def create_word_mask(secret_word):
    return ["_"] * len(secret_word)


def ask_for_guess():
    chosen_letter = input("Choose a letter: ")
    return chosen_letter.strip().upper()


def mark_guessed_letters(chosen_letter, secret_word, masked_word):
    index = 0
    for letter in secret_word:
        if letter.upper() == chosen_letter:
            masked_word[index] = letter
        index += 1


if __name__ == "__main__":
    play()
