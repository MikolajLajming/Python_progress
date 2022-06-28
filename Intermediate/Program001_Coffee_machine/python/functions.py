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
    ingredients = [
        i for i in dictionaries.MENU[product]["ingredients"]
        if dictionaries.MENU[product]["ingredients"][i] > dictionaries.RESOURCES[i][0]
    ]
    if ingredients:
        output = neatify_list(ingredients)
    return output


def start_machine(menu: dict):
    menu_items = [i for i in menu]
    not_enough_resources = [
        i for i in menu_items for x in dictionaries.MENU[i]["ingredients"]
        if dictionaries.MENU[i]["ingredients"][x] > dictionaries.RESOURCES[x][0]
    ]
    items = [x for x in menu_items if x not in not_enough_resources]
    if not items:
        print("no menu available")
        return False
    print(f'Available menu is:\n{neatify_list(items)}')
    prompt = input(f'What would you like?: ').lower()
    return prompt


def report():
    maintenance_report = "\n".join(list([
        "Current state of resources:\n",
        "\n".join(f"{i.title()}: "
                  f"{dictionaries.RESOURCES[i][0]}{dictionaries.RESOURCES[i][1]}" for i in dictionaries.RESOURCES),
        f"Money: ${'{:.2f}'.format(calculate_money(dictionaries.MONEY))}: {list_coins(dictionaries.MONEY)}.\n"
    ]))
    return maintenance_report


def calculate_money(dictionary: dict):
    money = sum([dictionary[i]["amount"] * dictionaries.MONEY[i]["value"] for i in dictionary])
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
    change = sum([money[i]["amount"] * dictionaries.MONEY[i]["value"] for i in money])
    memory = {}
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
    if my_list[0] != my_list[-1]:
        items_but_last = [i for i in my_list[:-1]]
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
    amount_returned = '{:.2f}'.format(calculate_money(rest))
    message = f"${amount_returned} returned: {list_coins(rest)}"
    return message


def list_coins(coins_dict: dict):
    coins = []
    for i in coins_dict:
        if coins_dict[i]["amount"] == 1 and i == "pennies":
            coins.append(f'{coins_dict[i]["amount"]} penny')
        elif coins_dict[i]["amount"] == 1:
            coins.append(f'{coins_dict[i]["amount"]} {i[:-1]}')
        else:
            coins.append(f'{coins_dict[i]["amount"]} {i}')
    return neatify_list(coins)


def machine_off(no_resources: bool):
    clear_console()
    if no_resources:
        print("Machine out of resources!")
    print("Bye!")
