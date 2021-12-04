from art import logo
from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

machine_on_flag = True

while machine_on_flag:
    print(logo)
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}): ").lower()
    if user_choice == "off":
        print("Switched off!")
        machine_on_flag = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(menu_item):
            money_machine.make_payment(menu_item.cost)
            coffee_maker.make_coffee(menu_item)
