from datetime import date

birth_year = int(input("enter year: "))
birth_month = int(input("enter month: "))
birth_day = int(input("enter day: "))
new_date = date(birth_year, birth_month, birth_day).ctime()
print(date)

