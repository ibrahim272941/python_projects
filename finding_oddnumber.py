user = int(input('enter a number'))
user_1 = int(input('enter a number'))


new_list=[]
while user<user_1:
    if user%2!=0:
        new_list.append(user)
    user+=1
print(new_list)