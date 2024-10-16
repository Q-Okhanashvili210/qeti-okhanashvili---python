text = input("please enter your text: ")

for i in range(len(text)):
    if text[i] == " " or text[i] == "e":
        continue
    if i%2 == 0:
        print(text[i])
    