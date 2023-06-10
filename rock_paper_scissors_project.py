import random

computer = ['Rock', 'Paper', 'Scissors']

random_pc_choice = len(computer)
pc_choice = random.randint(0, random_pc_choice - 1)

print("Computer chose " + pc_choice)