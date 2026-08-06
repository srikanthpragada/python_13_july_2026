class Counter:
    def __init__(self, value = 1):
        #Object Attributes
        self.value = value
        self.initvalue = value

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

    def getvalue(self):
        return self.value

    def reset(self):
        self.value = self.initvalue

    def __str__(self):
        return f"Value = {self.value}"

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

c = Counter(100)
print(c)  # c.__str__()

c2 = Counter()
print(c == c2) # c.__eq__(c2)

print(c > c2)

# c.inc()
# c.inc()
# print(c.getvalue())
# c.reset()
# print(c.getvalue())
