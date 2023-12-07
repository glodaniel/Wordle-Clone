import random
import os

def read_word_list(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def choose_word(word_list):
    return random.choice(word_list)

def display_word(secret_word, guessed_word, guessed_letters):
    displayed_word = ""
    for i in range(len(secret_word)):
        if i < len(guessed_word) and guessed_word[i] == secret_word[i]:
            displayed_word += f"{guessed_word[i]} "
        elif i < len(guessed_word) and guessed_word[i] in secret_word:
            displayed_word += f"{guessed_word[i].upper()} "
        else:
            displayed_word += "_ "

    remaining_letters = [letter.upper() if letter not in guessed_letters else ' ' for letter in 'abcdefghijklmnopqrstuvwxyz']
    print(" ".join(remaining_letters))
    
    return displayed_word


def play_wordle():
    max_attempts = 6

    file_path = "wordList.txt"
    word_list = read_word_list(file_path)
    secret_word = choose_word(word_list)

    print("Welcome to Wordle! You will have six attempts to guess a five-letter word.")
    print("If a letter is uppercase, then it is in the wrong place.")
    print("If a letter is lowercase, then it is correct.")
    print("Ready to play?")
    
    guessed_letters = []  # Initialize the guessed letters list
    print(display_word(secret_word, "", guessed_letters))

    attempts = 0
    while attempts < max_attempts:
        guess = input("Enter your guess: ").lower()

        if len(guess) != len(secret_word) or not guess.isalpha():
            print("Invalid input. Please enter a guess with the correct length.")
            continue

        guessed_letters.extend(guess)
        current_display = display_word(secret_word, guess, guessed_letters)
        print(current_display)

        if guess == secret_word:
            print("Congrats! You guessed the word:", secret_word)
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            feedback = display_word(secret_word, guess, guessed_letters)
            print("Incorrect guess. Attempts remaining:", remaining_attempts)
            print("Feedback:", feedback)

    if attempts == max_attempts:
        print("Sorry, you ran out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    play_wordle()
