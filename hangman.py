import random


def play():
    show_welcome_message()

    secret_word = pick_secret_word()
    masked_word = create_word_mask(secret_word)

    attempts = 0
    hanged = False
    guessed = False

    draw_hangman(attempts)
    print(masked_word)

    while not hanged and not guessed:
        chosen_letter = ask_for_guess()

        if chosen_letter in secret_word:
            mark_guessed_letters(chosen_letter, secret_word, masked_word)
        else:
            attempts += 1
            print("There's no {} in whe word, you have {} attempts remaining".format(chosen_letter, 6 - attempts))

        draw_hangman(attempts)
        print(masked_word)

        hanged = attempts == 6
        guessed = "_" not in masked_word

    if guessed:
        show_win_message()
    else:
        show_game_over_message(secret_word)


def show_welcome_message():
    print("###########################################")
    print("##      Welcome to the Hangman Game      ##")
    print("###########################################")


def show_win_message():
    print("         YOU WIN!       ")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def show_game_over_message(secret_word):
    print("        GAME OVER           ")
    print(" The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \        ")
    print("  /                 \       ")
    print("//                   \/\    ")
    print("\|   XXXX     XXXX   | /    ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/      ")
    print("   |\     XXX     /|        ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/        ")
    print("     \_         _/          ")
    print("       \_______/            ")


def draw_hangman(attempts):
    print("  _______     ")
    print(" |/      |    ")

    if (attempts == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (attempts == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (attempts == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (attempts == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (attempts == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (attempts == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (attempts == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (attempts == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


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
