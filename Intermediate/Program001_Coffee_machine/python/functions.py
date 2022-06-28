import dictionaries
import os
import math


def clear_console():
    """Clears the console"""
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def resources_sufficient(product: str):
    output = False
    ingredients = []
    for i in dictionaries.MENU[product]["ingredients"]:
        if dictionaries.MENU[product]["ingredients"][i] > dictionaries.RESOURCES[i][0]:
            ingredients.append(i)
    if ingredients:
        output = neatify_list(ingredients)
    return output


def start_machine(menu: dict):
    menu_items = []
    not_enough_resources = []
    for i in menu:
        menu_items.append(i)
        for x in dictionaries.MENU[i]["ingredients"]:
            if dictionaries.MENU[i]["ingredients"][x] > dictionaries.RESOURCES[x][0]:
                not_enough_resources.append(i)
    items = [x for x in menu_items if x not in not_enough_resources]
    if not items:
        print("no menu available")
        return False
    print(f'Available menu is:\n{neatify_list(items)}')
    prompt = input(f'What would you like?: ').lower()
    return prompt


def report():
    maintenance_report = "Current state of resources:\n"
    for i in dictionaries.RESOURCES:
        maintenance_report += f"{i.title()}: {dictionaries.RESOURCES[i][0]}{dictionaries.RESOURCES[i][1]}\n"
    money = calculate_money(dictionaries.MONEY)
    coins_in_machine = list_coins(dictionaries.MONEY)
    maintenance_report += f"Money: ${'{:.2f}'.format(money)}: {coins_in_machine}.\n"
    return maintenance_report


def calculate_money(dictionary: dict):
    money = 0
    for i in dictionary:
        money += dictionary[i]["amount"] * dictionaries.MONEY[i]["value"]
    return money


def prepare_coffee(product: str, money: dict):
    print("Preparing your coffee...")
    cost = dictionaries.MENU[product]["cost"]
    change = calculate_money(money)
    if change > cost:
        enough_change = return_change(money, cost)
        if not enough_change:
            return False
        print(calculate_change(enough_change))
        use_ingredients(product)
        return True
    modify_machine_money(money, False)
    use_ingredients(product)
    return True


def return_change(money: dict, cost: float):
    change = 0
    memory = {}
    for i in money:
        change += money[i]["amount"] * dictionaries.MONEY[i]["value"]
    modify_machine_money(money, False)
    change = round((change - cost), 2)
    for i in list(money.keys()):
        if dictionaries.MONEY[i]["amount"] != 0 and change >= dictionaries.MONEY[i]["value"]:
            temp_memory = math.floor(change / dictionaries.MONEY[i]["value"])
            change = round((change - temp_memory * dictionaries.MONEY[i]["value"]), 2)
            if temp_memory <= dictionaries.MONEY[i]["amount"]:
                memory[i] = {
                    "amount": temp_memory
                }
                dictionaries.MONEY[i]["amount"] -= temp_memory
    if not memory:
        modify_machine_money(money, True)
        return False
    return memory


def neatify_list(my_list: list):
    items_but_last = []
    if my_list[0] != my_list[-1]:
        for i in my_list[:-1]:
            items_but_last.append(i)
        output = f"{', '.join(items_but_last)} and {my_list[-1]}"
    else:
        output = my_list[0]
    return output


def use_ingredients(product):
    for i in dictionaries.MENU[product]["ingredients"]:
        dictionaries.RESOURCES[i][0] -= dictionaries.MENU[product]["ingredients"][i]


def modify_machine_money(money: dict, remove: bool):
    for i in money:
        amount = money[i]["amount"]
        if remove:
            amount *= -1
        dictionaries.MONEY[i]["amount"] += amount


def calculate_change(rest: dict):
    coins_returned = list_coins(rest)
    amount_returned = calculate_money(rest)
    message = f"${amount_returned} returned: {coins_returned}"
    return message


def list_coins(coins_dict: dict):
    coins = []
    for i in coins_dict:
        coins.append(f'{coins_dict[i]["amount"]} {i}')
    return neatify_list(coins)


def machine_off(no_resources: bool):
    clear_console()
    if no_resources:
        print("Machine out of resources!")
    print("Bye!")