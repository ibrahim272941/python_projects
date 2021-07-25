user_asking = int(input('pls input a number: '))
if user_asking == 1:
    fib_list =[1]
elif user_asking !=1:
    fib_list =[1,1]
    for i in fib_list:
        while len(fib_list)<user_asking:
            i = fib_list[-1] + fib_list[-2]
            fib_list.append(i)
print(fib_list)