def get_secret_word():
    """
    input is validated to obtain only alphabetical characters
    :return: string
    """
    while True:
        secret_word = input("Please enter a word to be guessed ").strip().lower()
        if not secret_word or not secret_word.replace(" ", "").isalpha():
            print("Invalid input. Only enter a word containing alphabetical characters")
        else:
            return secret_word


def display_hangman(num_tries):
    """
    :param num_tries:
    :return: string
    """
    # list of different stages of hangman
    stage = [
        '''
        +------+
        |       |
        |       |
                |
                |
                |
                |
                |
                |
                |
                |
    =============
        ''',
        '''
        +------+
        |       |
        |       |
        0       |
                |
                |
                |
                |
                |
                |
                |
    =============
        ''',
        '''
        +------+
        |       |
        |       |
        0       |
        |       |
        |       |
        |       |
                |
                |
                |
                |
    =============
        ''',
        '''
         +------+
         |      |
         |      |
         0      |
        /|      |
       / |      |
         |      |
                |
                |
                |
                |
    =============
        ''',
        '''
         +------+
         |      |
         |      |
         0      |
        /|\     |
       / | \    |
         |      |
                |
                |
                |
                |
    =============
        ''',
        '''
         +------+
         |      |
         |      |
         0      |
        /|\     |
       / | \    |
         |      |
        /       |
       /        |
                |
                |
    =============
        ''',
        '''
         +------+
         |      |
         |      |
         0      |
        /|\     |
       / | \    |
         |      |
        / \     |
       /   \    |
                |
                |
    =============
        '''

    ]

    return stage[num_tries]


def get_player_guess(guessed_list):
    """
    :param guessed_list:
    :return: character
    """
    while True:
        # to player 2
        try:
            guess = input("Please enter any letter ").strip().lower()
            # if guess in guessed_l or guess is not equal to 1
            if not guess or len(guess) != 1 or not guess.isalpha() or guess in guessed_list:
                print("Invalid input. Please enter a single alphabetic character that hasn't been guessed")
            else:
                return guess
        except EOFError:
            break


def player():
    """
    it displays "Hanged Man
    it displays partially guessed word
    it displays characters guessed so far in sorted order
    :return: no return value
    """
    # get a secret word from player 1
    secret_word = get_secret_word()
    # variable holds guessed characters by player 2
    guessed_letters = []

    # letters in the secret word should be displayed as ‘?’
    guessed_word = []
    # use for loop to discard space between secret words such as 'left arm', 'right arm', 'left leg', 'right leg'
    for char in secret_word:
        if char.isalpha():
            guessed_word.append("?")
        else:
            guessed_word.append(char)
    num_tries = 6
    while num_tries > 0 and "?" in guessed_word:
        # display a hangman
        print(display_hangman(num_tries))
        # display guessed word in '?'
        print(f"The partially guessed secret word {guessed_word}")
        # display guessed letters in sorted order
        print(f"The characters guessed so far in sorted order {sorted(guessed_letters)}")

        # ask Player 2 to guess a letter
        # we'll call a function that does this
        player_2_guess = get_player_guess(guessed_letters)

        # insert a guessed letter to the list
        guessed_letters.append(player_2_guess)

        # check if player 2 guess is in secret word
        if player_2_guess in secret_word:
            # use for loop to build a complete stage of a hangman chosen
            # by player 1 based on player 2 letters chosen.
            # this is done within 7 trials
            for i, character in enumerate(secret_word):
                if character == player_2_guess:
                    guessed_word[i] = player_2_guess
        else:
            num_tries -= 1  # reduces the number of tries a player 2 guesses a letter
            # and exit the loop as the number of tries reaches 0
    # check if there are no more '?' is a guessed word list
    if '?' not in guessed_word:
        print("Congratulations!! Your guess is {}".format(secret_word))
    else:
        print(display_hangman(num_tries))
        print("Sorry! You lost! the secret word is {}".format(secret_word))


def main():
    """
    the function main calls hangman function
    :return:
    """
    player()


if __name__ == '__main__':
    # calls the main function
    main()
