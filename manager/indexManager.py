from db.neon_connect import conn
import re
from manager.DashboardManager import DashboardManager

global id_manager
global name_manager
global badge_manager

def manager():


    def starter():
        print('Welcome manager! Do you have an account? (Y/N)')
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
    print(" ")
    print("---- SIGN UP ----")
    print(" ")
    def prompter():

        global name
        name = input('Please type your full name: ')
        print(" ")
        Verifier()

    def is_correct_badge(badge_number):
        pattern = r'^\d{4}$'
        if re.match(pattern, badge_number):
            return badge_number
        else:
            return None
    def Verifier():
        badge_number = input('Please type your badge number: ')
        print(" ")

        if is_correct_badge(badge_number):
            password = input('Please type your password: ')
            print(' ')

            Register(name, badge_number, password)
            login()

        else:

            print('Your badge number does not match the pattern of a real badge number. Please try again!')
            print(' ')
            Verifier()


    def Register(name, badge_number, password):

        try:
            cur = conn.cursor()
            cur.execute('INSERT INTO manager (name, badge_number, password) VALUES (%s, %s, %s)',
                        (name, badge_number, password))
            conn.commit()
            print('The manager was registered in our database successfully!')
        except Exception as err:
            print(f'Something went wrong, {err}')

            Register(name, badge_number, password)

    prompter()

def login():
    print(" ")
    print("---- LOGIN ----")
    print(" ")
    def prompter():

        Verifier()

    def is_correct_badge(badge_number):
        pattern = r'^\d{4}$'
        if re.match(pattern, badge_number):
            return badge_number
        else:
            return None
    def Verifier():

        badge_number = input('Please type your badge number: ')
        print(" ")

        if is_correct_badge(badge_number):
            password = input('Please type your password: ')
            print(" ")
            Select(badge_number, password)

        else:
            print('Your badge number does not match the pattern of a real badge number. Please try again!')
            print(" ")
            Verifier()

    def Select( badge_number, password):


        try:

            cur = conn.cursor()
            cur.execute('SELECT * FROM manager WHERE badge_number = %s AND password = %s',
                        (badge_number, password))
            res = cur.fetchone()

            id_manager = res[0]
            name_manager = res[1]
            badge_manager = res[2]


            print('Login successful!')
            DashboardManager.funcaosimples(id_manager,name_manager, badge_manager)
        except:
            print("The information you provided was incorrect. Please try again!")
            login()


    prompter()

