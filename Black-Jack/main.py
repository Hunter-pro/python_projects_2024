#Number Guessing Game Objectives:
logo ="""
   _____                       _   _                                  _              
  / ____|                     | | | |                                | |             
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ ___ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \'__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |  
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_| 

"""



# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint

hard_guess_limit = 5
easy_guess_limit = 10

rand_number = randint(1,100)
attempts = 1
print(logo)
print('Welcome to number guessing game!')
print("I'am thinking of number between 1 and 100")
difficulty = input("Choose the difficuly.Type easy or hard:")
if difficulty == 'easy':
  attempts = easy_guess_limit
elif difficulty == 'hard':
  attempts = hard_guess_limit
else:
  print('you have entered the wrong input,try again')

while attempts:
  print(f'You have {attempts} remaining for guessing the number')
  guess_number = int(input('Make a guess:'))
  if guess_number > rand_number:
    print('Too high')
    attempts -= 1
  elif guess_number < rand_number:
    print('Too low')
    attempts -= 1
  elif guess_number == rand_number:
    print('you have got the correct number')
    attempts = 0
