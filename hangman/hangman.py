import random

def play_hangman():
    word_list = ["python", "programming", "computer", "science", "code"]
    word = random.choice(word_list)
    word = word.upper()
    word_letters = set(word)
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    used_letters = set()
    word_guessed = set()
    word_display = "_"*len(word)
    word_display = list(word_display)
    tries = 6
    hangman = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
    ]
    print("Welcome to Hangman!")
    print(hangman[0])
    print("\n")
    print("The word contains", len(word), "letters.")
    print("\n")
    print("You have", tries, "tries to guess the word.")
    print("\n")
    print(" ".join(word_display))
    print("\n")
    while tries > 0:
        guess = input("Guess a letter or the word: ")

        if len(guess) == 1 and guess.isalpha():
            if guess in used_letters:
                print("You have already used that letter. Try again.")
            elif guess in word_letters:
                used_letters.add(guess)
                for i in range(len(word)):
                    if guess == word[i]:
                        word_display[i] = guess
                        word_guessed.add(guess)
                if word_guessed == word_letters:
                    print("Congratulations! You guessed the word:", word)
                    break
                print(" ".join(word_display))
            else:
                tries -= 1
                used_letters.add(guess)
                print(hangman[6 - tries])
        else:
            if guess == word:
                print("Congratulations! You guessed the word:", word)
                break
            else:
                print("Sorry, that's not the correct word. The hangman has been hanged.")
                break

if __name__ == '__main__':
    play_hangman()
