names = ['Bill Gates', 'Larry Ellison', 'Mark', 'Sam Altman']

def has_space(st):
    return st.find(' ') != -1

for name in filter(has_space, names):
    print(name)
