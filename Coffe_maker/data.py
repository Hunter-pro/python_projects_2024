MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# 4. Check resources sufficient?
def check_resource(u_input):
    for key,val in MENU[u_input]['ingredients'].items():
        if resources[key] < val:
            print(f"Sorry there is not enough {key}")
            return False
    return True

# 6. Check transaction successful?
def check_transcation(u_money):
    if u_money >= MENU[user_input]["cost"]:
        return True
    else:
        return False    

money = 0.0
while True:
    # TODO 1.Prompt user by asking “ What would you like?
    user_input = input("what would you like? (expresso/latte/cappuccino):")
    # 2. Turn off the coffee machine by entering “ off” to the prompt.
    if user_input == 'off':
        break
    elif user_input == 'report':
        # 3. Print report.
        for key,val in resources.items():
            print(f"{key}: {val}")
        print(f'Money: ${money}')
    elif check_resource(user_input):
        # 5. Process coins.
        print('Please insert the coins')
        quaters = int(input('How many quaters? :'))
        dimes = int(input("how many dimes? :"))
        nickel = int(input("how many nickel? :"))
        penny = int(input("how many pennies? :"))
        user_money = (quaters * 0.25) + (dimes * 0.10) + (nickel * 0.05) + (penny * 0.01)
        if check_transcation(user_money):
            cost = MENU[user_input]['cost']
            money += cost    
            for key,val in MENU[user_input]['ingredients'].items():
                resources[key] -= val
            if user_money > cost:
                print( f"Your change is ${user_money - cost %0.2 }🪙")
            # 7. Make Coffee.
            print(f'Here is your {user_input}.Enjoy!💕')
            continue
        else:
            print('Sorry that\'s not enough money.Money refunded')
            continue
    elif user_input not in ['expresso','latte','cappuccino']:
        print('wrong input try again.')
        continue


        

        





