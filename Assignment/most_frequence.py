from typing import Counter
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

c = Counter(numbers)
d = c.most_common(1)

print('The most freuqent number is {} and it was {} times repeated'.format(d[0][0] , d[0][1]))



numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

d = numbers.count(3)
e = numbers[1]
print(f'The most freuqent number is {e} and it was {d} times repeated')



