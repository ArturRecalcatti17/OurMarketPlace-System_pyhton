
from db.neon_connect import conn
import re

def employee():

    def starter():
        print('Welcome employee! Please login for full access!!')
        print(' ')
    login()


def login():



    def prompter():

        print(" ")
        print("--- LOGIN ----")
        print(" ")

        def is_correct_email(email):
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if re.match(pattern, email):
                return email
            else:
                return None
        def is_correct_badge_number(number):
            pattern = r'^\d{4}$'
            if re.match(pattern, number):
                return number
            else:
                return None

        def VerifierNumber():

            global badgeNumber
            badgeNumber = input('Please type the number from your Badge: ')
            print(' ')
            if is_correct_badge_number(badgeNumber):
                VerifierEmail()

            else:
                print('Your badge number does not match the pattern of a real badge number. Please try again!')
                print('')
                VerifierNumber()

        def VerifierEmail():

            email = input('Please type your email: ')
            print(' ')
            if is_correct_email(email):
                password = input('Please type your password: ')
                print(' ')
                Select(badgeNumber, email, password)

            else:
                print('Your email does not match the pattern of a real email. Please try again!')
                print('')
                VerifierEmail()

        VerifierNumber()
    def Select(badgeNumber, email, password):

        try:
            cur = conn.cursor()
            cur.execute('SELECT * FROM employee WHERE badge_number = %s AND email = %s AND password = %s',
                        (badgeNumber, email, password))
            res = cur.fetchone()
            global id_employee
            global name_employee
            global email_employee

            id_employee = res[0]
            name_employee = res[1]
            email_employee = res[3]

            print('Login successful!')
        except Exception as err:
            print("The information you provided was incorrect. Please try again!")
            login()

    prompter()



