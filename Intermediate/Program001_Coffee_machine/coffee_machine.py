import sys
sys.path.insert(0, "python/")
from python import dictionaries
from python import functions
from python import errors


def switches(loop: bool):
    global choice_loop
    global machine_on
    if loop:
        machine_on = True
        choice_loop = True
    else:
        machine_on = False
        choice_loop = False


def ask_to_continue(question_type: str):
    global prompt
    if question_type != list(dictionaries.CASES.keys())[0]:
        question = input(f"{dictionaries.CASES[question_type]}. Would you like to start over? Type Y or N: ").upper()
        if question == "Y":
            loop = True
            prompt = functions.start_machine(dictionaries.MENU)
        elif question == "N":
            loop = False
        else:
            functions.clear_console()
            print(errors.error(1))
            loop = True
            prompt = functions.start_machine(dictionaries.MENU)
    else:
        functions.clear_console()
        print(errors.error(1))
        loop = True
        prompt = functions.start_machine(dictionaries.MENU)
    switches(loop)


choice_loop = True
machine_on = True
prompt = functions.start_machine(dictionaries.MENU)
while machine_on:
    while choice_loop:
        if prompt in dictionaries.MAINTENANCE:
            if dictionaries.MAINTENANCE[prompt]:
                report = functions.report()
                print(report)
                prompt = functions.start_machine(dictionaries.MENU)
            else:
                switches(False)
        elif prompt in list(dictionaries.MENU.keys()):
            choice_loop = False
            task = prompt
            not_sufficient = functions.resources_sufficient(prompt)
            if not_sufficient:
                choice_loop = True
                print(f"Machine does not have sufficient amount of {not_sufficient}.")
                prompt = functions.start_machine(dictionaries.MENU)
        else:
            functions.clear_console()
            print(errors.error(1))
            prompt = functions.start_machine(dictionaries.MENU)
    if machine_on:
        cost = dictionaries.MENU[task]["cost"]
        change = {}
        for i in dictionaries.MONEY:
            change[i] = {
                "amount": int(input(f"How many {i}?: "))
            }
        money = functions.calculate_money(change)
        if money < cost:
            ask_to_continue(list(dictionaries.CASES.keys())[1])
        else:
            prepare_coffee = functions.prepare_coffee(task, change)
            message = prepare_coffee
            if message:
                print(f"Here's your {task}!")
                ask_to_continue(list(dictionaries.CASES.keys())[2])
            else:
                ask_to_continue(list(dictionaries.CASES.keys())[3])


functions.machine_off()

