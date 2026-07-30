def hello():
    print('Hello')

h = hello

h()
hello()

print(id(h))
print(id(hello))
