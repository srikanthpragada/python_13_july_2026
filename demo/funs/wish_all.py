def wish(*users, message = 'Hello'):
    for u in users:
        print(message, u)


wish('Mark', 'Jack',  message  =  'Hi')
wish('Mark', 'Jack', 'Scott')
wish()
