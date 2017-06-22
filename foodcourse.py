start = '''
Hi! My name is Foodie! My purpose is to help you
decide where to go for dinner!!
'''


print(start)


print("Choose your lifestyle, are you 'wealthy' or 'poor'?")
user_input = input()
if user_input == "wealthy":
    print("Would you like to eat at 'Cheescake Factory' or 'Black Angus Steakhouse'?")
    user_input = input()
    if user_input == "Cheescake Factory" or user_input == "cheesecake factory":
        print("Would you like to eat 'Guacamole Salad' or 'Everything Pizza'?")
        user_input = input()
        if user_input == "Guacamole Salad":
            print("Yay! You are going to live ten years longer now!")
        elif user_input == "Everything Pizza":
            print("shame on you! That's a lot more calories!")
    elif user_input == "Black Angus Steakhouse" or user_input == "black angus steakhouse":
        print("Would you like to eat 'steak'or 'cobb salad'?")
        user_input = input()
        if user_input == "steak":
            print(":/ now you will never be able to fit in that dress.")
        elif user_input == "cobb salad":
            print("Good choice!You look fit!")
elif user_input == "poor":
    print("Would you like to eat at 'McDonald's' or 'In-n-Out'?")
    user_input = input()
    if user_input == "McDonald's" or user_input == "mcdonalds":
        print("Would you like to eat 'Big Mac' or 'House Salad'")
        user_input = input()
        if user_input == "Big Mac" or user_input == "big mac":
            print("You have gained 10 Pounds!")
            user_input = input()
        elif user_input == "House Salad":
            print("Yay!You have chosen the healthier choice!!")
    elif user_input == "In-n-Out" or user_input == "in-n-out":
        print("Would you like to eat 'protein style' or 'cheeseburger'? ")
        user_input = input()
        if user_input == "protein style":
            print("Good Job! One step closer to you bikini body (:")
        elif user_input == "cheeseburger":
            print("Boohoo... I am disappointed in you.")
