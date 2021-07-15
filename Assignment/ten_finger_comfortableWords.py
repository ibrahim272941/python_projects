left= {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'}
right= {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'}

text = input('pls enter a text\t:')
text_1=set(text)
left_bool = bool(text_1 -left)
right_bool = bool(text_1 - right)

if left_bool and right_bool:
    print(f'{text} is comfortable words')
else:
    print('{} is uncomfortable'.format(text))