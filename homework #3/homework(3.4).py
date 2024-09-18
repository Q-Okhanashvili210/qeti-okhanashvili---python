import random

card_color = ("clubs","diamonds", "hearts", "spaders")
card_number=("A","K","Q","J","10","9","8","7","6","5", "4", "3", "2")
random_card_color = random.choice(card_color)
random_card_number = random.choice(card_number)
print(random_card_color, random_card_number)
