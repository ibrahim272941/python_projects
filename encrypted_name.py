def crypted ():
    name_1 = input('pls enter name : ')
    surname = input('pls enter surname : ')
    sum_name = name_1 + ' ' + surname
    list_1 = sum_name.split()
    encrypted_name = ''
    for i in list_1:
        x = i.replace(i[1:-1] , '*' * (len(i)-2))
        encrypted_name+=x+' '
    return f'Hi {encrypted_name} Welcome to encrypted name function' 

print(crypted())