import random
guess_number = random.randint(0, 100)
user_attemp = 10

for i in range(user_attemp):
    user_guess = int(input (f"Attempt {i + 1}: Enter your guess: "))
    
    if user_guess == guess_number:
            print("You are winner!")
                  
    elif user_guess > guess_number:
            print("High")
    else:
            print("Low")
                 
    print("computer is winner" "number is: ", guess_number )
