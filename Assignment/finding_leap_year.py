year = int(input('Pls enter a 4 digit year: '))

print((year%400==0 and f'{year} is leap year') or (year % 4 ==0 and year % 100!=0 and f'{year} is leap year') or (year %100 ==0 and f'{year} is not leap year') or f'{year} is not leap year')