import random
from words_for_hangman import all_words

hangman_pic = ['''
----
|  |
| 
|
|''', '''
----
|  |
|  o
|
|''', '''
----
|  |
|  o
|  |
|''', '''
----
|  |
|  o
| /|
|''', '''
----
|  |
|  o
| /|\\
|''', '''
----
|  |
|  o
| /|\\
| /''', '''
----
|  |
|  o
| /|\\
| / \\''']


def board(missed_letters, correct_letters, word_to_guess):
    print(hangman_pic[len(missed_letters)])
    print()
    print('Missed letters:', end=' ')

    for letter in missed_letters:
        print(letter, end=' ')

    print()

    blanks = '_'*len(word_to_guess)

    for i in range(len(word_to_guess)):
        if word_to_guess[i] in correct_letters:
            blanks = blanks[:i] + word_to_guess[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    while True:
        print('Guess a letter: ')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in already_guessed:
            print('You have already guessed this letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return guess


def play_again():
    print('Do you want to play again?(yes or no)')
    return input().lower().startswith('y')


print('HANGMAN')
missed_letters = ''
correct_letters = ''
word_to_guess = random.choice(all_words)
game_is_done = False

while True:
    board(missed_letters, correct_letters, word_to_guess)
    guess = get_guess(missed_letters + correct_letters)
    if guess in word_to_guess:
        correct_letters = correct_letters + guess
        found_all_letters = True
        for i in range(len(word_to_guess)):
            if word_to_guess[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print('Yes, you won. The secret word is ' + word_to_guess + '.')
            game_is_done = True
    else:
        missed_letters = missed_letters + guess
        if len(missed_letters) == len(hangman_pic) - 1:
            board(missed_letters, correct_letters, word_to_guess)
            print('''You have run out of guesses
After ''' + str(len(missed_letters)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was ' + word_to_guess + '.')
            game_is_done = True
    if game_is_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            word_to_guess = random.choice(all_words)
        else:
            break
