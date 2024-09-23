import random

players_number = int(input("enter players number: "))

for i in range(players_number):
    
    first_number = random.randint(1,6)
    second_number = random.randint(1,6)
    print(first_number, second_number)
  