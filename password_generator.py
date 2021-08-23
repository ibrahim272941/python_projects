import random



upper=''.join([chr(random.randint(65,90)) for i in range(3)])
lower =''.join([chr(random.randint(97,122)) for i in range(3)])
number =''.join([chr(random.randint(48,57)) for i in range(3)])
chars =chr(random.randint(33,47))+chr(random.randint(58,64))
pasword=upper+lower+number+chars


def shuffle_it(string):
    pass_list=list(string)
    random.shuffle(pass_list)
    return ''.join(pass_list)

passw=shuffle_it(pasword)