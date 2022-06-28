MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

MAINTENANCE = {
    "report": True,
    "off": False,
}

MONEY = {
    "quarters": {
        "value": 0.25,
        "amount": 25,
    },
    "dimes": {
        "value": 0.10,
        "amount": 25,
    },
    "nickles": {
        "value": 0.05,
        "amount": 25,
    },
    "pennies": {
        "value": 0.01,
        "amount": 25,
    }

}

RESOURCES = {
    "water": [300, "ml"],
    "milk": [200, "ml"],
    "coffee": [100, "g"],
}

CASES = {
    "error": "ERROR",
    "money": "That's not enough. Money returned",
    # "not_sufficient": "",
    "coffee_served": "Enjoy!",
    "not_enough_change": "Sorry, the machine could not return change. All coins (if provided) returned"
}

LOOPS = {
    "loop_machine": True,
    "machine_off": False,
}
