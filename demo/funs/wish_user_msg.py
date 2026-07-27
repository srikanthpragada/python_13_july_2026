def wish(user, message):
    print(message, user)

# Pass by position
wish('Ben', 'Hi')
wish('Tom', 'Good Morning')
#wish('Mark')

# Pass by keyword
wish(message = 'Hi', user = 'Dave')
# Mixed
wish('Jack', message = 'Hello')

