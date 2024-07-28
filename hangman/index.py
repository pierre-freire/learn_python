import random
import string
from words import words

def get_valid_word(options):
    word = random.choice(options)
    while '-' in word or ' ' in word:
        word = random.choice(options)
    return word.upper()

def hangman():
    word =  get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have ',lives,' left. You have used these letters: ', ', '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]

        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter not in the word!')
        elif user_letter in used_letters:
            print('You used it before!')
        else:
            print("Invalid character. Please try again!")
    if lives == 0:
        print(f'You died! word was {word}')
    print(f'Congratulations! You succesfully guessed the word {word}')

hangman()