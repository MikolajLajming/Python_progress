import random

# >>>>>>> For testing purposes <<<<<<<
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

throw = random.randint(0, 1)

if throw == 0:
    print("Tails")
else:
    print("Heads")
