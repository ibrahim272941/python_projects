numbers = int((input('pls enter a number')))
div_range = list(range(1 ,numbers +1))
div_list = []
for i in div_range:
    if numbers % i ==0:
        div_list.append(i)
print(div_list)