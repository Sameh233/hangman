import random
from hangman_words import word_list
import hangman_art

lives = 6

stages = hangman_art.stages
logo = hangman_art.logo
chosen_word = random.choice(word_list)
print(logo)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    
    print(f"**************************** {lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    display = ""

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

   
            print(f"*********************** THE WORD WAS {chosen_word} GAME OVER **********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    print(stages[lives])
