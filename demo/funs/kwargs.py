def show(**details):
    for k, w in details.items():
        print(k, w)


show(a=10, b=20, c=30)
show(name='Python', version='3.14')
