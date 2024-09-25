n =int(input("enter number: "))
if n < 0 or n >20 :
    exit(0)
    m = 1
    a = 0
    b = 1     
    while m <= n +1 :
        print( a, end= " ")
        temp = a
        a = b
        b = temp + b
    
    m=m+1