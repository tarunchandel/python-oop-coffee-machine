from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myCoffeeMaker = CoffeeMaker()
myMenu = Menu()
myMoneyMachine = MoneyMachine()

machine_on_flag = True
while machine_on_flag:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        print("Switched off!")
        machine_on_flag = False
    elif user_choice == "report":
        myCoffeeMaker.report()
        myMoneyMachine.report()
    else:
        myMenuItem = myMenu.find_drink(user_choice)
        if myCoffeeMaker.is_resource_sufficient(myMenuItem):
            myMoneyMachine.make_payment(myMenuItem.cost)
            myCoffeeMaker.make_coffee(myMenuItem)