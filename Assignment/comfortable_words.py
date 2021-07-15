left_hand= ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
right_hand = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']

enter_text = input('pls enter a text\t:')
val_left = 1
val_right = 1

for i in enter_text :
    if i in left_hand:
        val_left = 11
    if i in right_hand:
         val_right = 11
if val_right == 11 and val_left ==  11 :
    print(True , f'{enter_text} is a Comfortable text')              
        
elif val_right == 11 and val_left == 1:
    print(False , f'You used only your Right Hand\n{enter_text} is not a Comfortable text') 

elif val_right == 1 and val_left == 11 :
    print(False , f'You used only your Left Hand\n{enter_text} is not a Comfortable text')
else:
    print('Pls enter only Letter')   









