from employee.indexEmployee import employee
from client.indexClient import client
from manager.indexManager import manager

def Program():

      print('Hello! Welcome to our market system, are you a client, an employee or a manager?')
      response = input(': ')

      def starter():
            if response.lower() == 'client':
                  client()

            elif response.lower() == 'employee':
                  employee()

            elif response.lower() == 'manager':
                  manager()

            else:
                  print(' ')
                  print('Something went wrong, please try again: ')
                  print(' ')
                  Program()


      starter()
Program()

