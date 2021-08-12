words = ["eat", "tea", "tan", "ate", "nat", "bat"]

dict ={}

for i in words:
    sortedWord = ''.join(sorted(i)) 
    if sortedWord in  dict:
        dict[sortedWord].append(i)
    else :
        dict[sortedWord] = [i]

print(list(dict.values()))


