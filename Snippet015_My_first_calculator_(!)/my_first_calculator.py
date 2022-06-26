import functions
from errors import error
from art import logo


def calculator(is_failed, failure_no):
    functions.clear_console()
    print(logo)

    if is_failed:
        print(error(failure_no))

    memory = False
    carry_on = True
    first_number = float(input("What's the first number?: "))

    while carry_on:
        if memory:
            print(memory)
            memory = False
        else:
            for i in functions.operations:
                print(i)

        operation = str(input("Select an operation: "))
        second_number = float(input("What's the next number?: "))

        if operation == "/" and second_number == 0:
            calculator(True, 1)
        elif operation not in functions.operations:
            calculator(True, 2)
        else:
            result = 0
            for action in functions.operations:
                if operation == action:
                    function = functions.operations[action]
                    result = function(first_number, second_number)
                    print(f"{first_number} {operation} {second_number} = {result}")
                    memory = result
            question1 = str(input(f"Continue with the result {result}? Type Y for yes or N for no: ")).upper()
            if question1 == "Y":
                first_number = memory
            elif question1 == "N":
                memory = False
                question2 = str(input("Would you like to continue? Type Y for yes or N for no: ")).upper()
                if question2 == "Y":
                    calculator(False, 0)
                elif question2 == "N":
                    carry_on = False
                    functions.clear_console()
                    print("Bye!")
                else:
                    calculator(True, 2)
            else:
                calculator(True, 2)


calculator(False, 0)
