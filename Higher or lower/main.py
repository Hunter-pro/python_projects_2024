from art import logo,vs
from random import choice
from game_data import data
from replit import clear


print(logo)

account_a = choice(data)
account_b = choice(data)

score = 0
end_of_game = False
while not end_of_game:
  
  print(f"compare A:{account_a['name']},{account_a['description']},from {account_a['country']}")
  
  print(vs)
  print(f"against B:{account_b['name']},{account_b['description']},from {account_b['country']}")
  user_choice = input('Who has more followers? Type "A" or "B"').lower()
  if account_a['follower_count'] > account_b['follower_count']:
    correct_ans = 'a'
  else:
    correct_ans = 'b'
  if user_choice == correct_ans:
    score +=1
    data.remove(account_a)
    account_a = account_b
    account_b = choice(data)
    clear()
    print(f"You're right! Current score: {score}.")
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    end_of_game = True
  
  
 