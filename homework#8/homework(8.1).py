text = str(input("enter text :"))
filter_text = "".join(char.lower() for char in text if char.isalpha())
lenght=len(filter_text)
is_palindrom = True
for i in range(lenght//2):
    if filter_text[i]!= filter_text[lenght-1-i]:
        is_palindrom = False
        break

if is_palindrom == True:
    print("is palindrome")
else:
    print("is not palindrome")
    