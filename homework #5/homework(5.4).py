n = int(input("enter number: "))

start = n-1
print( " " * (start), end = "*")
print('')
while start > 0: 
    print(" "* (start -1), end="")
    print("/"*(n-start), end = '')
    print("|", end = "")
    print("\\" * (n-start), end= "")
    print("")
    start = start -1
    
print(" "*(n-1), end="|" )
    