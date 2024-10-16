text_word = input("please enter your text word: ")
new_word=" "
for i in text_word:
    if i not in "aeiou " :
        new_word += i
        
print(new_word, end ="")