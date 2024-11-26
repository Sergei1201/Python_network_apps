# Create a greeting
# Create you word list
# Randomly choose a word from the list
# Ask the user to guess a letter
# Replace letters in a secret word with _ sign
# If the guess word equals the letter in the secret word, replace _ with the letter
# Make the program take the input from the user and convert it to lowercase
# Check if the letter is in the word

import random
import time

# Greeting
first_name = input('Enter you first name: ')
last_name = input('Enter you last name: ')


def greeting(first_name, last_name):
    return f'{first_name} {last_name}, welcome to the game!'


print(greeting(first_name, last_name))
time.sleep(2)

# Create a word list
word_list = ['apple', 'pear', 'banana', 'apricot', 'grapes']
secret_word = random.choice(word_list)

# Get user input
user_guess = input('Enter a letter: ').lower()
word_display = []

# For each letter in the secret word replace a letter with _ sign
for letter in secret_word:
    word_display += '_'
print(word_display)

# For each letter in the secret word replace a letter _ with user_guess letter if it matches that of the secret word's letter
for position in range(len(secret_word)):
    letter = secret_word[position]
    if letter == user_guess:
        word_display[position] = secret_word[position]

print(word_display)

print(secret_word)
