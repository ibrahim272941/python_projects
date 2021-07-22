prime = int(input('pls enter a number\t:'))
sign = False

if prime > 0:
    for i in range(2 , int(prime/2)+1):
        if prime % i == 0 :
            sign = True
            break
    if sign:
        print('{} is not prime number'.format(prime)) 
    else:
        print('{} is prime number'.format(prime))  
       
else :
    print('Please enter a number greater than 0')