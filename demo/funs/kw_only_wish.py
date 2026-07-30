# Keyword-only arguments
def wish(*, user, message):
    print(message, user)


wish(message = 'Hi', user = 'Dave')
wish(user = "Scott", message = "Hello")
#wish('Tom', 'Hi')


