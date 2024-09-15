enter_num = int(input("enter number:"))

if enter_num <= 0 or enter_num >= 11 :
    print("invalid number! stop")
else:
    if enter_num == 1:
        print("1")
    if enter_num % 2 == 1 and enter_num < 8:
        print(enter_num)
    if enter_num % 2 == 0 and enter_num < 5:
        print("2")
    if enter_num % 2 == 0 and enter_num % 3 == 0 and enter_num > 5:
        print("2" ,"3")
    if enter_num % 9 == 0:
        print("3")
    if enter_num % 5 == 0 and enter_num % 2 == 0:
        print("5","2")
    if enter_num == 8 :
        print("2")
