import calendar

year = int(input('type in the year: '))
month = int(input('type the month year (for eg march is 3): '))

a = calendar.monthrange(year, month)

print(a[1])



