class Course:
    #static attribute or class attribute
    taxrate = 9

    @staticmethod
    def gettaxrate():
        return Course.taxrate

    def __init__(self, title, fee, duration=24):
        #object attributes
        self.title = title
        self.fee = fee
        self.duration = duration

    @property
    def netfee(self):
        return self.fee + self.fee * Course.taxrate // 100

    def getnetfee(self):
        return self.fee + self.fee * Course.taxrate // 100

    def getduration(self):
        return self.duration

    def gettitle(self):
        return self.title

    def show(self):
        print(f"Title    : {self.title}")
        print(f"Duration : {self.duration}")
        print(f"Fee      : {self.fee}")

print(Course.gettaxrate())
c1 = Course('GenAI', 10000)
c1.show()
print(c1.getnetfee())
print(c1.netfee)  # use property