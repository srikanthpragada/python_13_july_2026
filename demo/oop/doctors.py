from abc import ABC, abstractmethod

# Abstract class
class Doctor(ABC):
    def __init__(self, name, mobile, dept):
        self.name = name
        self.mobile = mobile
        self.dept = dept

    def getdept(self):
        return self.dept

    def getmobile(self):
        return self.mobile

    # Abstract method
    @abstractmethod
    def getsalary(self):
        pass

class ResidentDoctor(Doctor):
    def __init__(self, name, mobile, dept, salary):
        super().__init__(name, mobile, dept)
        self.salary = salary

    def getsalary(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, mobile, dept, visits, charge):
        super().__init__(name, mobile, dept)
        self.visits = visits
        self.charge = charge

    def getsalary(self):
        return self.visits * self.charge


c = Consultant("Dr. Gary", "39399433", "ortho", 10, 1000)
r = ResidentDoctor("Dr. Kim", "399239232", "cardio", 300000)

print(c.getmobile())
print(c.getsalary())

print(r.getmobile())
print(r.getsalary())