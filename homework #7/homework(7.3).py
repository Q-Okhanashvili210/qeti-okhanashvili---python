text = input("please enter your word: ")

lenght = len(text)

if lenght == 0:
    print("invalid word, try again!")
else:
  first_symbol = text[0]
  last_symbol = text[-1]

if lenght % 2 == 0:
    mid_symbol =text[lenght//2-1 :lenght//2+1]
else:
    mid_symbol=text[lenght//2]

i = 0
while i < 5:
    print(first_symbol,  mid_symbol, last_symbol)
    i += 1 
  