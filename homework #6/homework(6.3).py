n = int(input("enter number: "))

if n < 0 or n >= 10000:
   print("invalid number. try again")
else:
    n = n
    reversd_number = 0
    sum_digits = 0
    
while n>0:
    last_num = n%10
    reversd_number = reversd_number*10 +last_num
    sum_digits += last_num

print(f'reserved number : {reversd_number}')
print(f'sum of digits: {sum_digits}')
 