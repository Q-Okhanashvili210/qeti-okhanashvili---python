import random
n = int(input("enter your number :"))

if n < 0 and n > 30:
    exit(0)
max_number = 0
for i in range(n):
    your_numbers = random.randint(0, 1000)
    if max_number < your_numbers:
        max_number = your_numbers
print("maximum number is :" ,max_number )
