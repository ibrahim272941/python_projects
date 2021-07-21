import random
rnumber = random.randint(1,10)
print(rnumber)

count = 0
while True:
    guessNumber = int(input('Aklimdan 1\'den 10\'a kadar bir sayi tuttum tahmin et bakalim '))
    if guessNumber ==rnumber:
        print('Bravo bildin!!! {} aklimdaki sayiydi'.format(rnumber))
        count +=1
        break
    elif guessNumber > rnumber:
        count +=1
        print('Senin sayin biraz fazla daha kücük bir sayi tusla')

    elif guessNumber < rnumber:
        count +=1
        print('Senin sayin biraz kücük daha büyük bir sayi tusla')

