# Position-only arguments
def wish(user, message, /):
    print(message, user)

wish("Scott", "Hello")
#wish(message = 'Hi', user = 'Dave')




