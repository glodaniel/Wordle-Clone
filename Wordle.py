import random
def read_word_list(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words
import os

#reading file
file_name = "wordList.txt"
file_path = os.path.join(os.getcwd(), file_name)
word_list = read_word_list(file_path)

#choosing a word
def choose_word(word_list):
    return random.choice(word_list)

def display_word(secret_word, guessed_word):
    displayed_word = ""
    for i in range(len(secret_word)):
        if i < len(guessed_word) and guessed_word[i] == secret_word[i]:
            displayed_word += guessed_word[i]
        elif i < len(guessed_word) and guessed_word[i] in secret_word:
            displayed_word += '*'
        else:
            displayed_word += '_'
    return displayed_word

def play_wordle():
    max_attempts = 6

    file_path = "wordList.txt"
    word_list = read_word_list(file_path)
    secret_word = choose_word(word_list)

    print("Welcome to Wordle!")
    print("Can you guess the word?")
    print(display_word(secret_word, ""))

    attempts = 0
    while attempts < max_attempts:
        guess = input("Enter your guess: ").lower()

        if len(guess) != len(secret_word) or not guess.isalpha():
            print("Invalid input. Please enter a guess with the correct length.")
            continue

        if guess == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            feedback = display_word(secret_word, guess)
            print("Incorrect guess. Attempts remaining:", remaining_attempts)
            print("Feedback:", feedback)

    if attempts == max_attempts:
        print("Sorry, you ran out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    play_wordle()
