
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
            print('Something went wrong, please try again: ', err)
            starter()

    starter()


def signup():

    def prompter():

        global name
        name = input('Please type your full name: ')
        Verifier()

    def is_correct_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        re.match(pattern, email)
        return email

    def Verifier():

        email = input('Please type your email: ')

        if is_correct_email(email):
            birthdate = input('Please type your birthdate (mm/dd/yyyy): ')
            password = input('Please type your password: ')

            Register(name, email, password, birthdate)

        else:

            print('Your email does not match the pattern of a real email. Please try again!')
            Verifier()


    def Register(name, email, password, birthdate):

        try:
            cur = conn.cursor()
            cur.execute('INSERT INTO client (name, email, password, birthdate) VALUES (%s, %s, %s, %s)',
                        (name, email, password, birthdate))
            conn.commit()
            print('The client was registered in our database successfully!')
        except Exception as err:
            print(f'Something went wrong, {err}')

    prompter()

def login():

    def prompter():

        Verifier()

    def is_correct_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        re.match(pattern, email)
        return email

    def Verifier():

        email = input('Please type your email: ')

        if is_correct_email(email):
            password = input('Please type your password: ')
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
            print(f'Something went wrong, {err}')

    prompter()


client()


