input_number = int(input("enter number:"))
if input_number < 0 or input_number > 20:
    exit(0)
 
first_num = 0
second_num = 1
for n in range (input_number):
    m = first_num
    first_num = second_num
    second_num += m
print(first_num)