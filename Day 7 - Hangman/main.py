import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
blank = "_"
lives = 6
guessed_letters = []

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = [blank] * len(chosen_word)

print(logo)
while blank in display and lives != 0:
    print(stages[lives])
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
    else:
        guessed_letters.append(guess)
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display[index] = letter
        else:
            print(f"The letter {guess} is not in the word.")
            lives -= 1

    print(f"{' '.join(display)}")

if lives == 0:
    print(stages[lives])
    print("You Lose.")
else:
    print("You Win!")
