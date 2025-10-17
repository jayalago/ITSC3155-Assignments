class Cashier:
    def __init__(self):
        pass

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
                print(f"Here is ${change:.2f}.")  # format .2f = 0.00
            return True
