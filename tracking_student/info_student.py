print("""
            ############################################
            ------WELCOME TO STUDENT REGISTER MODUL-----
            ############################################
                """)
print("""
        1-New Register
        2-Display Student Info
        3-Display All Record
        4-Exit""")
student_dict = {}

while True:
    user = input('Which module do you want to access ? ')
    if user == '1':
        number = input('pls enter a student number : ')
        name = input('pls enter a student name : ')
        surname = input('pls enter a student surname : ')
        grade = int(input('pls enter a student grade : '))
        dict_1={number: 
        {'name': name, 'surname':surname , 'grade': grade}}
        student_dict.update(dict_1)
    elif user == '2':
        number = input('pls enter student number : ')
        print(student_dict[number])
    elif user == '3':
        print(student_dict)
    elif user == '4':
        break
   

       
            
        


