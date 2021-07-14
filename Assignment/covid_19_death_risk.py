
###### User dan bilgi alarak olusturulan risk analizi #########

age = (input('Are you a cigarette addict older than 75 years old?: ').title())
chronic = (input('Do you have a severe chronic disease?: ').title())

immune = (input('Is your immune system too weak?:').title())

if age == 'Yes' or chronic == 'Yes' or immune == 'Yes' :

     print(True , 'You are in Risk Group')

else :
    print(False , 'You are not in Risk Group')


   