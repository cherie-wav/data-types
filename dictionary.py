inventory = [
    {
    'name1' : 'egg roll', 'price1': 24, 'description': 'a deep fried side savory roll with cabbage and meat wrapped in a wheat flour skin',
    'name2' : 'milk tea', 'price2': 12, 'description2': 'a creamy beverage made by combining fresh jasmine tea with milk and sweetened with syrup',
    'name3' : 'popcorn chicken', 'price3': 14, 'description3': 'a snack made of small, bite sized pieces of chicken that are sesoned, breaded, and deep fried till crunchy',
    }
]
def run_shop():
    wallet = 200
    cart = []
    total_cost = 0
    while True:
        print (f"we have: {inventory[0]['name1']}, {inventory[0]['name2']}, {inventory[0]['name3']}")
        print (f"cost: ${inventory[0]['price1']}, ${inventory[0]['price2']}, ${inventory[0]['price3']}")
        print (f"account balance: ${wallet}")
        desc = input("would you like to view the description of an item? ").lower()
        if desc == 'yes':
            bum = input("which item would you like to view? if you want to go back, type 'nevermind'")
            if bum == 'egg roll':
                print (f"{inventory['description']}")
                run_shop()
            elif bum == 'milk tea':
                print (f'{inventory['description2']}')
                run_shop()
            elif bum == 'popcorn chicken':
                print (f"{inventory['description3']}")
                run_shop()
            elif bum == 'nevermind':
                choice = input("what do you wanna buy ")
                if choice == 'egg roll':
                    item_price = inventory[0]['price1']
                    if item_price >= wallet:
                        print("yo you cant afford this get outta here")
                        break
                    elif item_price <= wallet:
                        total_cost += 24
                        wallet -= item_price
                        cart.append(choice)
                        print (f"you spent ${item_price}")
                        print (f"account balance: ${wallet}")
                        print (f"you have successfully bought one {choice}")
                        cont = input("would you like to keep shopping? Yes or No: ")
                        if cont == 'No' or cont == 'no':
                            print (f"thanks for shopping yo; you spent ${total_cost} and bought {cart}")
                            break
                elif choice == 'milk tea':
                    item_price = inventory[0]['price2']
                    if item_price >= wallet:
                        print("yo you cant afford this get outta here")
                        break
                    elif item_price <= wallet:
                        total_cost += 12
                        wallet -= item_price
                        cart.append(choice)
                        print (f"you spent ${item_price}")
                        print (f"account balance: ${wallet}")
                        print (f"you have successfully bought one {choice}")
                        cont = input("would you like to keep shopping? Yes or No: ")
                        if cont == 'No' or cont == 'no':
                            print (f"thanks for shopping yo; you spent ${total_cost} and bought {cart}")
                            break
                elif choice == 'popcorn chicken':
                    item_price = inventory[0]['price3']
                    if item_price >= wallet:
                        print("yo you cant afford this get outta here")
                        break
                    elif item_price <= wallet:
                        total_cost += 14
                        wallet -= item_price
                        cart.append(choice)
                        print (f"you spent ${item_price}")
                        print (f"account balance: ${wallet}")
                        print (f"you have successfully bought one {choice}")
                        cont = input("would you like to keep shopping? Yes or No: ")
                        if cont == 'No' or cont == 'no':
                            print (f"thanks for shopping yo; you spent ${total_cost} and bought {cart}")
                            break
        if desc == 'no':
            run_shop()
run_shop()