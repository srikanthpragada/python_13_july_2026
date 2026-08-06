class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(10,20)
print(getattr(p1, 'x'))
print(hasattr(p1, 'width'))

setattr(p1, 'depth', 5)
print(getattr(p1, 'depth'))
delattr(p1, 'depth')
print(hasattr(p1, 'depth'))
print(getattr(p1, 'width', 2))

print(p1.__dict__)

