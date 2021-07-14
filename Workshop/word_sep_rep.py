word = input('pls enter a word: ') 
seperator = input('pls enter a sep: ')
word_n = word + seperator
repetition = input('how many times repetition: ')
result = word_n *int(repetition)
result = result .rstrip(seperator)

print(result)