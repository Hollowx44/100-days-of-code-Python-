import art
from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu = Menu()

while True:
    print(art.logo)
    choice=str(input(f"What would you like? ({menu.get_items()}) :"))
    if choice not in ("report","off"):
        order=menu.find_drink(choice)

    if choice == "off":
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if coffee_maker.is_resource_sufficient(order) == True:
            print(f"Cost of {choice} : ${order.cost}")
            if money_machine.make_payment(order.cost) == True:
                coffee_maker.make_coffee(order)
                

