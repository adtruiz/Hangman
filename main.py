import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
end_of_game = False
lives = 6

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    print('\n' * 100) # Skips 100 lines because clear() does not work.

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess

    if guess not in chosen_word:  # If I put this with above, itll go through each letter (and remove a lot of lives).
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])

