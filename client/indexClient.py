from db.neon_connect import conn
import re

def client():

    def starter():
        print('Welcome client! Do you have an account? (Y/N)')
        response = input(' ')

        try:
            if response.lower() == 'n':
                signup()

            elif response.lower() == 'y':
                login()
        except Exception as err:
            print(' ')
            print('Something went wrong, please try again: ', err)
            starter()

    starter()


def signup():

    def prompter():

        print(" ")
        print("--- SIGN UP ----")
        print(" ")

        global name
        name = input('Please type your full name: ')
        print(' ')
        Verifier()

    def is_correct_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return email
        else:
            print(' ')

    def Verifier():

        email = input('Please type your email: ')

        if is_correct_email(email):
            print(' ')
            birthdate = input('Please type your birthdate (mm/dd/yyyy): ')
            print(' ')
            password = input('Please type your password: ')
            print(' ')

            Register(name, email, password, birthdate)
            login()

        else:
            print('Your email does not match the pattern of a real email. Please try again!')
            print(' ')
            Verifier()


    def Register(name, email, password, birthdate):

        try:
            cur = conn.cursor()
            cur.execute('INSERT INTO client (name, email, password, birthdate) VALUES (%s, %s, %s, %s)',
                        (name, email, password, birthdate))
            conn.commit()
            print('The client was registered in our database successfully!')
        except Exception as err:
            print(' ')
            print(f'Something went wrong, {err}')
            print(' ')

    prompter()


def login():

    def prompter():

        print(" ")
        print("--- LOGIN ----")
        print(" ")

        Verifier()

    def is_correct_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return email
        else:
            print(' ')

    def Verifier():

        email = input('Please type your email: ')
        print(' ')

        if is_correct_email(email):
            password = input('Please type your password: ')
            print(' ')
            Select(email, password)

        else:
            print('The information provided does not exist in our database, please try again!')
            print('')
            Verifier()

    def Select( email, password):

        try:
            cur = conn.cursor()
            cur.execute('SELECT * FROM client WHERE email = %s AND password = %s',
                        (email, password))
            res = cur.fetchone()
            global id_user
            global name_user
            global email_user

            id_user = res[0]
            name_user = res[1]
            email_user = res[2]

            print('Login successful!')
        except Exception as err:

            print("The information you provided was incorrect. Please try again!")
            print(' ')
            login()

    prompter()

