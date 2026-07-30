def hello(user):
    print('Hello', user)

def goodbye(user):
    print("Good Bye", user)

def msg(user, task):
    task(user)

msg('Bill', hello)
msg('Bill', goodbye)
#msg('Tom', abs)