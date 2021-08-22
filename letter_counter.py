def counter(word):
    new_dict={}
    for i in word:
        if i not in new_dict:
            new_dict[i] = 0
        new_dict[i]+=1
    return new_dict
