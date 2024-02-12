#calculator
from os import system
from art import logo
def add(n1,n2):
  return n1+n2
  
def subtract(n1,n2):
  return n1-n2
  
def multiply(n1,n2):
  return n1*n2
  
def divide(n1,n2):
  return n1/n2

operations = {'*':multiply,'+':add,'/':divide,'-':subtract}

def calculator():
  print(logo)
  num1 = float(input("what's the first number?: "))
  
  
  for key in operations.keys():
    print(key)
  
  
  flag = True
  while flag:
    operation_symbol = input('Pick an operation from the line above: ')
    num2 = float(input("what's the next number?: "))
    
    answer = operations[operation_symbol](num1,num2)
    
    print(f"{num1}{operation_symbol}{num2} = {answer}")
    
    choice = input(f"Type 'y' to continue calculating with {answer},or type 'n' to start new or 'e' for exit.: ").lower()
    if choice == 'n':
      flag = False
      system('cls')
      calculator()
    elif choice == 'y':
      num1 = answer
    elif choice == 'e':
      flag = False
    else:
      print('wrong choice,pick again')
      continue

calculator()