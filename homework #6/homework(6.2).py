n = int(input("enter number : "))
if n < 0 or n > 1000:
    print("pkease try again. invalid number ")
else:
 while n != 1 :
        if n % 2 == 0:
            n//2
        else:
            n = n*3 + 1
print(f' -> {n}', end='')
