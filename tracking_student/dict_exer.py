# dict_by_dict = {'animal':'dog',
# 			'planet': 'Neptun',
# 			'number': 40,
# 			'pi':3.14,
# 			'is_good': True}

# for i in dict_by_dict:
#     print(i)



def main():
    print("""
            **********************
            --------WELCOME-------
            **********************
    
    """)

    while True:
        print(""" 
                  1- New Register
                  2- Show the Register 
                  3- Exit""")
        order = input('What do want to access')
        
        students_main = {'100':{'name':'Ibrahim','surname':'Coban','grade':'95'}}
        students ={}
        if order == '1':
            register(students)
            students_main.update(students)
        elif order =='2':
            display(students_main)
        elif order == '3':
            break        
                  

def register(students):
    number =input('pls enter student number')
    name = input('pls enter student name')
    surname = input('pls enter student surname')
    grade = input('pls enter student grade')
    students['number']=number
    students['name']=name
    students['surname']=surname
    students['grade']=grade  
      

def display(students_main):
    number = input('student number')
    print(students_main[number])


main()
