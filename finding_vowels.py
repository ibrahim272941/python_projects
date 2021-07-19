
word = input('Input your sentence\t:').lower()
# word = 'ich fahre mit dem Auto'
word = ''.join(word)

vowels = ['a','e','u','ü','ä','ö','i','o']

new_list = {}

for i in word:
    if i in  vowels:
        new_list[i]=word.count(i)
print(new_list)