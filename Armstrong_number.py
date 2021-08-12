num = (input('pls enter a number\t:'))

digit = str(num)
summ = 0
if num.isdigit():
    for i in digit :
        num_1 = int(i) ** len(digit)
        summ +=num_1
        num = int(num)
    if num == summ :
            print(f'{num} is Amrstrong number !!!!')
    else:
            print(f'{num} is not Armstrong number')
elif num.isalpha():
    print(' It is an invalid entry. Dont use non-numeric, float, or negative values!')
elif float(num) < 0:
     print(' It is an invalid entry. Dont use non-numeric, float, or negative values!')
else:
    print('It is an invalid entry. Dont use non-numeric, float, or negative values!')


