from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
puji_ki_profit = MoneyMachine()

vivek_ki_machine = CoffeeMaker()

menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? {options}").lower()
    if user_choice == "off" :
        is_on = False
    elif user_choice == "report":
        puji_ki_profit.report()
        vivek_ki_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if vivek_ki_machine.is_resource_sufficient(drink) and puji_ki_profit.make_payment(drink.cost):
            vivek_ki_machine.make_coffee(drink)







