from ..manageManagerAccount import

def funcaosimples(id,name, badge):

    print(f'Welcome `{name}, this is your dashboard, here you can make these things: ')
    print('''

    1 - Add an Employee;'

    '2 - Update the Employee data;'

    '3 - Delete the Employee;
    
    4 - Update your data;
    
    5 - Delete your account.

    ''')

    def starter():

        res = input(': ')

        if int(res) == 1:
            add()

        elif int(res) == 2:
            update()

        elif int(res) == 3:
            delete()

        elif int(res) == 4:



        else:
            print('''
            Something went wrong, please type an existent option: 
            ''')
            starter()

    starter()











