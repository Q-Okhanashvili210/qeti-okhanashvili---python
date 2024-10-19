first_word = input("enter first word:")
second_word = input("enter second word: ")
if len(first_word) !=len(second_word):
    print("No")
else:
    can_crated = True
    letters_count = {}
    for i in range(0,len(first_word)):
        symbol = first_word[i]
        if letters_count.get(symbol):
            letters_count[symbol]= letters_count[symbol]+1
        else:
            letters_count[symbol]=1
    
    for i in range(0,len(second_word)):
        symbol = second_word[i]
        if letters_count.get(symbol) and letters_count.get(symbol) >0 :
            letters_count[symbol]= letters_count[symbol]-1
        else:
            can_crated = False
    
    if can_crated == True:
        print(" yes")
    else:
        print(" No")