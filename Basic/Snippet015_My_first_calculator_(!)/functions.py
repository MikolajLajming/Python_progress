import os


def add(additive1, additive2):
    """Adds two numbers"""
    return additive1 + additive2


def subtract(subtract1, subtract2):
    """Subtracts two numbers"""
    return subtract1 - subtract2


def multiply(multiplier1, multiplier2):
    """Multiplies two numbers"""
    return multiplier1 * multiplier2


def divide(factor1, factor2):
    """Divides two numbers"""
    return factor1 / factor2


def clear_console():
    """Clears the console"""
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
