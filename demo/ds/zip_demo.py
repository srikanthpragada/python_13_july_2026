langs  = ['Python', 'Java', 'C#' , 'JavaScript']
vers = [3.14, 25, 14]

for t in zip(langs, vers):
    print(t)

for t in zip("abc", (1,2,3)):
    print(t)
