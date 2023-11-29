import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses a word from the list
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # letters user has guessed

    lives = 6

    # game introduction
    print("Welcome to the Hangman game!")
    print()
    print("RULES: Guess the secret word before you run out of lives.")
    print()

    # get user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # " ".join(["a", "b", "cd"]) --> "a b cd"
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        # tell user what current word is (ex. W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        print()

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1 # subtracts a life if wrong
                print("Letter is not in the word.")
                print()

        elif user_letter in used_letters:
            print("You have already guessed that letter. Please try again.")
            print()
        
        else:
            print("Invalid character. Please try again.")
            print()

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print("You lost, sorry. The word was", word)
    else:
        print("You've guessed the word", word, "!")


hangman()