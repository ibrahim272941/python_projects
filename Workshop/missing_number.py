# num_list = [2, 3, 1, 5, 6, 4, 9, 8, 10]
# a =sorted(num_list)
# missing_number = a[-1] * (a[-1] + a[0]) / 2 - sum(a)
# print(a , 'missing number: ', missing_number)


num_list = list(range(11))
num_list.sort()
print(list(reversed(num_list[1:11])))


grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]


print(grocer[1][1][1::2 ])


# text = "My two favorite flowers are tulip and rose, two favorite colors are blue and green."

flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
colors = ["red", ("blue", ["yellow", "green"]), "pink"]

print("My two favorite flowers are {} and {}, two favorite colors are {} and {}." 
.format((flowers[0][2]) , (flowers[0][1][1]) , (colors[1][0]) , (colors[1][1][1])))



# I am 40 years old.
#     I have two children.
#         Data Science is my IT domain.

sentence = "I am 40 years old. I have two children. Data Science is my IT domain."

print("I am 40 years old.\n{}I have two children.\n{}{}Data Science is my IT domain.".format("\t" , "\t" , "\t"))
