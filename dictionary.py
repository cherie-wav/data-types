inventory = [
    {
    'name' : 'egg roll', 'price': 8, 'description': 'a deep fried side savory roll with cabbage and meat wrapped in a wheat flour skin',
    },
    {'name' : 'milk tea', 'price': 12, 'description': 'a creamy beverage made by combining fresh jasmine tea with milk and sweetened with syrup',
    },
    {'name' : 'popcorn chicken', 'price': 14, 'description': 'a snack made of small, bite sized pieces of chicken that are sesoned, breaded, and deep fried till crunchy',
    },
    {'name' : 'fried chicken burger', 'price': 21, 'description': 'a thick chunk of fried chicken in between two toasted buns with a lettuce and a drizzle of house made mayonaise',
    },
    {'name' : 'matcha crepe cake', 'price': 16, 'description': 'a slice of numerous layers of crepes stacked on top of each other with butter cream between each layer and a thick dusting of matcha powder on top',
    },
    {'name' : 'crossing bridge noodles', 'price': 25, 'description':'a steaming bowl of pork bone broth, and a large tray of noodles, thin beef strips, cabbage, a quail egg, and various other toppings',
    },
    {'name' : 'strawberry lemonade',  'price': 6, 'description':'a refreshing, sweet and tart beverage made of lemon juice, water, honey, and pureed strawberries'
    },
    {'name' : 'honey lemon iced tea', 'price': 10, 'description': 'a refreshing, cold beverage that combines a brewed tea base, caramelized lemon slices and sweet honey'
     },
    {'name' : 'lemon cream puffs', 'price': 15, 'description': 'light airy pastries made from hollow choux dough and stuffed with a bright citrusy cream filling'
    },
    {'name' : 'lemon froyo bowl', 'price': 20, 'description': 'lemon flavored frozen yogurt topped with dried strawberries, oreo crumble, and a caramel drizzle'
    }
]
def run_shop():
    wallet = 200
    cart = []
    total_cost = 0
    while True:
        for item in inventory:
            print(f"{item['name']}, ${item['price']}")
        print(f"account balance: {wallet}")
        desc = input("would you like to view the description of an item? ").lower()
        if desc == 'yes':
            bum = input("which item would you like to view? if you want to go back, type 'nevermind'")
            if bum != 'nevermind':
                    found_desc = False
            for item in inventory:
                if item['name'] == bum:
                    print(f"{item['description']}")
                    found_desc = True
                    break
            if not found_desc:
                print("we dont got that get outta here")
        if desc == 'no':
            pass
            choice = input("what do you wanna buy ").lower()
            chosen_thing = None
            for item in inventory:
                if item['name'] == choice:
                    chosen_thing = item
                    break
            if chosen_thing is None:
                print("we don't sell that get outta here")
                continue
            item_price = chosen_thing['price']
            if item_price >= wallet:
                print("yo you cant afford this get outta here")
                continue
            elif item_price <= wallet:
                total_cost += item_price
                wallet -= item_price
                cart.append(chosen_thing['name'])
                print (f"you spent ${item_price}")
                print (f"account balance: ${wallet}")
                print (f"you have successfully bought one {choice}")
            cont = input("would you like to keep shopping? Yes or No: ")
            if cont == 'No' or cont == 'no':
                print (f"thanks for shopping yo; you spent ${total_cost} and bought {cart}")
                break
run_shop()