n = int(input("enter number:"))
if n < 0 and n > 1000:
    exit(0)

for i in range(1, n+1):
    if n%i == 0:
        print(i, end=", ")