import random
rnumber = random.randint(1,20)
print()

count = 0
while True:
    guessNumber = int(input('I thought of a number from 1 to 20, guess what : '))
    if guessNumber ==rnumber:
        print('Congrats you guessed right !! {} was the number in my mind'.format(rnumber).center(50))
        count +=1
        break
    elif guessNumber > rnumber:
        count +=1
        print('Your number is a little too much, enter a smaller number :')

    elif guessNumber < rnumber:
        count +=1
        print('Your number is a little smaller, enter a bigger number :')

