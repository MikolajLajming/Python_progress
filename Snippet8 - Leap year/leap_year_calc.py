year = int(input("Which year do you want to check? "))

modulo_4 = year % 4
modulo_100 = year % 100
modulo_400 = year % 400
yes = "Leap year."
no = "Not leap year."

if modulo_4 == 0:
    if modulo_100 == 0:
        if modulo_400 == 0:
            print(yes)
        else:
            print(no)
    else:
        print(yes)
else:
    print(no)
