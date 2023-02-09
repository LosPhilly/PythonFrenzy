import random
word_list = ["python", "javascript", "java", "html", "css"]
word = random.choice(word_list)
hidden_word = "*" * len(word)
misses = 0
while misses < 7:
    print(hidden_word)
    guess = input("Enter a letter: ")
    if guess in word:
        print("Correct! You found a letter.")
        new_hidden_word = ""
        for i, letter in enumerate(word):
            if letter == guess:
                new_hidden_word += letter
            else:
                new_hidden_word += hidden_word[i]
        hidden_word = new_hidden_word
    else:
        print("Wrong! The letter is not in the word.")
        misses += 1
    if hidden_word == word:
        print("You won! The word was " + word + ".")
        break
if misses == 7:
    print("You lost! The word was " + word + ".")
