import random
import sys

WORDS = ["python", "hangman", "computer", "programming", "keyboard"]
MAX_INCORRECT = 6

def choose_word():
    return random.choice(WORDS)

def play_once():
    # Pick a word and reset state
    word = choose_word()
    guessed = []      # list of guessed letters
    mistakes = 0

    while mistakes < MAX_INCORRECT:
        # Show progress: letters or underscores
        progress = " ".join(c if c in guessed else "_" for c in word)
        print("\nWord:", progress)
        print(f"Mistakes: {mistakes}/{MAX_INCORRECT}")

        guess = input("Enter a letter or guess the whole word: ").strip().lower()
        if not guess:
            continue

        # Single letter guess
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed:
                print("You already guessed that letter.")
                continue
            guessed.append(guess)
            if guess in word:
                print("Good guess!")
            else:
                print("Wrong letter.")
                mistakes += 1
        else:
            # Whole word guess
            if guess == word:
                print("\nYou won! The word was:", word)
                return
            else:
                print("Wrong word.")
                mistakes += 1

        # Check if all letters are guessed
        if all(c in guessed for c in word):
            print("\nYou won! The word was:", word)
            return

    print("\nYou lost! The word was:", word)

def main():
    while True:
        play_once()
        again = input("\nPlay again? (y/N): ").strip().lower()
        if again != "y":
            print("Goodbye.")
            break

if __name__ == "__main__":
    main()
