hoursA = input("How many hours does employee A work?: ")
hoursB = input("How many hours does employee B work?: ")

class Employee:

    def __init__(self, name, age, gender, experience, salary, otsalary, hours):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__experience = experience
        self.__salary = salary
        self.__otsalary = otsalary
        self.__hours = hours

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getGender(self):
        return self.__gender

    def getExperience(self):
        return self.__experience

    def getSalary(self):
        return self.__salary

    def getOtsalary(self):
        return self.__otsalary

    def getHours(self):
        return self.__hours

    def getPaycheckA(self):
        if int(hoursA) <= 40:
            return int(self.__hours) * self.__salary
        if int(hoursA) > 40:
            return ((int((self.__hours)) - 35) * self.__otsalary) + (int(self.__salary) * 35)

    def getPaycheckB(self):
        if int(hoursB) <= 40:
            return int(self.__hours) * self.__salary
        if int(hoursB) > 40:
            return ((int((self.__hours)) - 35) * self.__otsalary) + (int(self.__salary) * 35)

def Main():
    aEmployee = Employee("John", "21", "Male", "3 Years", 20, 35, hoursA)
    bEmployee = Employee("Jack", "35", "Male", "10 Years", 20, 35, hoursB)
    print("Name: " + aEmployee.getName())
    print("Age: " + aEmployee.getAge())
    print("Gender: " + aEmployee.getGender())
    print("Years of Experience: " + aEmployee.getExperience())
    print("Salary ($/Hour): " + str(aEmployee.getSalary()))
    print("OT Salary ($/Hour): " + str(aEmployee.getOtsalary()))
    print("Hours Worked: " + aEmployee.getHours())
    print("Paycheck Amount ($): " + str(aEmployee.getPaycheckA()))
    print()
    print("Name: " + bEmployee.getName())
    print("Age: " + bEmployee.getAge())
    print("Gender: " + bEmployee.getGender())
    print("Years of Experience: " + bEmployee.getExperience())
    print("Salary ($/Hour): " + str(bEmployee.getSalary()))
    print("OT Salary ($/Hour): " + str(bEmployee.getOtsalary()))
    print("Hours Worked: " + bEmployee.getHours())
    print("Paycheck Amount ($): " + str(bEmployee.getPaycheckB()))

Main()



