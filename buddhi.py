import random

def choose_word():
    words = ["python", "hangman", "programming", "example", "learning"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6  # You can adjust the number of allowed attempts

    print("hello!")

    while True:
        current_display = display_word(secret_word, guessed_letters)
        print(f"Current word: {current_display}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")

       
        guess = input("Enter a letter: ").lower()


        guessed_letters.append(guess)

        if guess not in secret_word:
            print("Incorrect guess!")
            attempts -= 1

# Run the hangman game
hangman()
