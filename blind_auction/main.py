from os import system
from art import logo
#HINT: You can call clear() to clear the output in the console.

bidder = {}
print(logo)
flag = True
def highest_bidder():
  highest_bid = 0
  for x,y in bidder.items():
    if y > highest_bid:
      highest_bid = y
      winner = x
  print(f"The winner is {winner} with the bid ${highest_bid}")

while flag:
  name = input('What is your name?:')
  bid = int(input('What is your Bid: $'))
  bidder[name]=bid
  choice = input('Are There any other bidders! type \'Yes\' or \'No\':').lower()
  if choice not in ['yes','no']:
    print('enter a correct option')
    continue
  elif choice == 'yes':
    system('cls')
    continue
  else:
    flag = False
    highest_bidder()

