# Task 1: Guess the Number
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to Guess the Number!")
print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too Low! Try Again.")

    elif guess > secret_number:
        print("Too High! Try Again.")

    else:
        print("Congratulations! You guessed the correct number.")
        break

# Task 2: Word Scramble

import random

# List of words
words = ['python', 'javascript', 'java', 'automation',
         'pytest', 'guvi', 'selenium']

# Select a random word
word = random.choice(words)

# Scramble the word
scrambled = ''.join(random.sample(word, len(word)))

print("Welcome to Word Scramble!")
print("Unscramble the following word:")
print(scrambled)

while True:
    guess = input("Enter your guess: ").lower()

    if guess == word:
        print("Congratulations! Correct Answer.")
        break
    else:
        print("Wrong Answer. Try Again.")