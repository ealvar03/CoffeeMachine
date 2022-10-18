import products


def show_menu():
    """
    It presents the different options that the user might select.
    """

    customer = True
    while customer:
        user_selection = input("What would you like? (☕️ espresso - ☕️ latte - ☕️ ️cappuccino - 📈 report - "
                               "❌ off): ").lower()
        if user_selection == 'report':
            report()
        elif user_selection == 'espresso' or user_selection == 'latte' or user_selection == 'cappuccino':
            if check_coffee_resources(user_selection):
                if is_enough_money(user_selection):
                    make_coffee(products.MENU[user_selection])
            else:
                check_coffee_resources(user_selection)
        elif user_selection == 'off':
            customer = False


def report():
    """
    This function will show on screen the different sources and their amount.
    """

    water = products.resources['water']
    milk = products.resources['milk']
    coffee = products.resources['coffee']
    money = products.money
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def check_coffee_resources(selection):
    """
    This function will check if the remaining resources are enough to place the selection the user made based on
    the ingredients needed in the dictionary 'resources' and the remaining items within the coffee machine.
    """
    drink = products.MENU[selection]
    for item in drink['ingredients']:
        if drink['ingredients'][item] >= products.resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(beverage):
    """
    It will reduced the ingredients used in the user choice from the resources.
    :param user_choice: input from user drink selection
    :param beverage: dictionary that contains the ingredients and costs of the menu drinks
    """
    for item in beverage['ingredients']:
        products.resources[item] -= beverage['ingredients'][item]


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


def is_enough_money(user_beverage):
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
                if user_beverage == product:
                    price = value

    if user_money < price:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif user_money > price:
        change = round((user_money - price), 2)
        products.money += round(price, 2)
        print(f"Here is ${change} in change.\nHere is your ☕️ {user_beverage}. Enjoy!")
        return True
    else:
        products.money += round(user_money, 2)
        print(f"Here is your ☕️ {user_beverage}. Enjoy!")
        return True
