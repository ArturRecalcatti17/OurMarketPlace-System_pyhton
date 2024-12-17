from client.indexClient import client

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
            print('Something went wrong, please try again: ')
            starter()
            print(' ')