#importing required modules 
import random
import hangman_art
from hangman_words import word_list
from  os import system

#choosing a random word from word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#var that used to end the game
end_of_game = False
#no of lifes each player has ie wrong guess user can make
lives = 6

print(hangman_art.logo)


#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    system('cls')

    if guess in display:
      print(f'You have alreay guessed {guess},try again')
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        
        print(f'You have guessed {guess},which is not in the word, you lose a life')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"{chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])