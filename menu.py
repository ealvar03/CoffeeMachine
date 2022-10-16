import products


def show_menu():
    """
    It presents the different options that the user might select.
    :return: It will return the user's selection.
    """
    selection = input("What would you like? (☕️ espresso - ☕️ latte - ☕️ ️capuccino - 📈 report - "
                      "❌ off): ").lower()
    return selection


user_selection = show_menu()
new_money_value = {'money': 0}
products.resources.update(new_money_value)


def report():
    """
    This function will show on screen the different sources and their amount.
    """

    water = products.resources['water']
    milk = products.resources['milk']
    coffee = products.resources['coffee']
    money = products.resources['money']
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def switch_off():
    """
    This function will end code execution.
    """
    exit()


def check_option():
    """
    This function will check the user's selection, and it will execute the corresponding function according
    to the option selected.
    """
    if user_selection == 'report':
        report()
    elif user_selection == 'espresso' or user_selection == 'latte' or user_selection == 'capuccino':
        check_coffee_resources()
        is_enough_money()
    else:
        switch_off()


def check_coffee_resources():
    """
    This function will check if the remaining resources are enough to place the selection the user made based on
    the ingredients needed in the dictionary 'resources' and the remaining items within the coffee machine.
    """
    water = products.resources['water']
    milk = products.resources['milk']
    coffee = products.resources['coffee']
    espresso_items = products.MENU['espresso'].get('ingredients')
    latte_items = products.MENU['latte'].get('ingredients')
    cappuccino_items = products.MENU['cappuccino'].get('ingredients')

    if water > espresso_items['water'] or water > latte_items['water'] or water > cappuccino_items['water']:
        if user_selection == 'espresso':
            products.resources['water'] -= espresso_items['water']
        if user_selection == 'latte':
            products.resources['water'] -= latte_items['water']
        if user_selection == 'cappuccino':
            products.resources['water'] -= cappuccino_items['water']
    else:
        print("Sorry, there is not enough water")
    if milk > latte_items['milk'] or milk > cappuccino_items['milk']:
        if user_selection == 'latte':
            products.resources['milk'] -= latte_items['milk']
        if user_selection == 'cappuccino':
            products.resources['milk'] -= cappuccino_items['milk']
    else:
        print("Sorry, there is not enough milk")
    if coffee > espresso_items['coffee'] or coffee > latte_items['coffee'] or coffee > cappuccino_items['coffee']:
        if user_selection == 'espresso':
            products.resources['coffee'] -= espresso_items['coffee']
        if user_selection == 'latte':
            products.resources['coffee'] -= latte_items['coffee']
        if user_selection == 'cappuccino':
            products.resources['coffee'] -= cappuccino_items['coffee']
    else:
        print("Sorry, there is not enough coffee")


def insert_coins():
    """
    It asks the user the amount of the different coins that will insert and based on that it will calculate the total.
    :return: This function will return the total money that the user inserted.
    """
    print("Please, insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def is_enough_money():
    """
    This function is going to check if the amount of money the user inserted is enough to buy the hot beverage selected
    by the user. It is going to iterate through the nested dictionary to get the value that corresponds to the key
    'cost' from the initial dictionary depending on the user_selection key. After it has been selected the proper
    value of the product selected by the user, it is going to calculate if the user inserted enough money or not, or if
    the machine needs to give to the user some money back in change.
    """
    user_money = insert_coins()
    price = 0
    for product, info in products.MENU.items():
        for feature, value in info.items():
            if feature == 'cost':
                if user_selection == product:
                    price = value

    if user_money < price:
        print("Sorry, that's not enough money. Money refunded.")
    elif user_money > price:
        change = round((user_money - price), 2)
        products.resources['money'] += round((user_money - price), 2)
        print(f"Here is ${change} in change.\nHere is your ☕️ {user_selection}. Enjoy!")
    else:
        products.resources['money'] += round(user_money, 2)
        print(f"Here is your ☕️ {user_selection}. Enjoy!")
