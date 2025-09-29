### Data ###
from warnings import catch_warnings

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients:
            if ingredients[ingredient] > self.resources.get(ingredient,0):
                print(f"Sorry, there is not enough {ingredient}")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Insert coins:")
        try:
            large_dollars = int(input("How many Large Dollars?: "))
            half_dollars = int(input("How many Half Dollars?: "))
            quarters = int(input("How many Quarters?: "))
            nickles = int(input("How many Nickles?: "))
        except ValueError:
            print("Please enter correct values.")
            return 0.00
        total = large_dollars + half_dollars * 0.5 + quarters * 0.25 + nickles * 0.05
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        else:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change:.2f}.") #format .2f = 0.00
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient in order_ingredients:
            self.resources[ingredient] -= order_ingredients[ingredient]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    def report(self):
        for ingredient, amount in self.resources.items():
            print(f"{ingredient}: {amount}")
### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)
while True:
    user_input = input("What would you like? (small/medium/large/off/report): ")

    if user_input == "off":
        break
    elif user_input == "report":
        machine.report()
    elif user_input == "small":
        recipe = recipes[user_input]
        ingredients = recipe["ingredients"]
        cost = recipe["cost"]
        if machine.check_resources(ingredients):
            coins_in = machine.process_coins()
            if machine.transaction_result(coins_in, cost):
                machine.make_sandwich(user_input, ingredients)
    elif user_input == "medium":
        recipe = recipes[user_input]
        ingredients = recipe["ingredients"]
        cost = recipe["cost"]
        if machine.check_resources(ingredients):
            coins_in = machine.process_coins()
            if machine.transaction_result(coins_in, cost):
                machine.make_sandwich(user_input, ingredients)
    elif user_input == "large":
        recipe = recipes[user_input]
        ingredients = recipe["ingredients"]
        cost = recipe["cost"]
        if machine.check_resources(ingredients):
            coins_in = machine.process_coins()
            if machine.transaction_result(coins_in, cost):
                machine.make_sandwich(user_input, ingredients)