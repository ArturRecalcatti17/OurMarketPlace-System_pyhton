from db.neon_connect import conn

def update(id, name, badge):
    print("Would you rather update the name, badge or both?")
    response = input(': ')
    def starter():
        try:
            if response.lower() == 'name':
                update_name()
            elif response.lower() == 'badge':
                update_badge()
            elif respones.lower() =='both':
                update_both()
        except Exception as err:
            print('Something went wrong, please try again: ', err)
        starter()

    def update_name():

        try:
            cur = conn.cursor()
            cur.execute('UPDATE employee(name) SET name = %s WHERE id = %s;',
                            (name, id))
            conn.commit()
            print("The employee's name was successfully updated " )
        except Exception as err:
            print(f'Something went wrong, {err}')
    update_name()

    def update_badge():
        try:
            cur = conn.cursor()
            cur.execute('UPDATE employee(badge_number) set badge_number = %s where id = %s;',
            (badge,id))
            conn.commit()
            print("The employee's badge was successfully updated ")
        except Exception as err:
            print(f'Something went wrong, {err}')
    update_badge()

update(id, name, badge, email, birthdate, password)


