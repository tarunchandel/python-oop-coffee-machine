class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""

        self.process_coins()
        change = round(self.money_received - cost, 2)
        # print(f"Cost: {cost}. Change = {change}")
        if change >= 0:
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost

        else:
            print(f"Sorry that's not enough money.")
            self.profit += self.money_received
            self.make_payment(-change)

        self.money_received = 0
