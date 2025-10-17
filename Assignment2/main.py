import data
from cashier import Cashier
from sandwich_maker import SandwichMaker

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    ###  write the rest of the codes ###
    while True:
        user_input = input("What would you like? (small/medium/large/off/report): ")

        if user_input == "off":
            break
        elif user_input == "report":
            for ingredient, amount in resources.items():
                print(f"{ingredient}: {amount}")
        elif user_input == "small":
            recipe = recipes[user_input]
            ingredients = recipe["ingredients"]
            cost = recipe["cost"]
            if sandwich_maker_instance.check_resources(ingredients):
                coins_in = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_in, cost):
                    sandwich_maker_instance.make_sandwich(user_input, ingredients)
        elif user_input == "medium":
            recipe = recipes[user_input]
            ingredients = recipe["ingredients"]
            cost = recipe["cost"]
            if sandwich_maker_instance.check_resources(ingredients):
                coins_in = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_in, cost):
                    sandwich_maker_instance.make_sandwich(user_input, ingredients)
        elif user_input == "large":
            recipe = recipes[user_input]
            ingredients = recipe["ingredients"]
            cost = recipe["cost"]
            if sandwich_maker_instance.check_resources(ingredients):
                coins_in = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_in, cost):
                    sandwich_maker_instance.make_sandwich(user_input, ingredients)

if __name__=="__main__":
    main()
