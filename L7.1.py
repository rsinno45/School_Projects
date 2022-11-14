class Person:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def setName(self, name):
        self.__name = name

    def setPhone(self, phone):
        self.__phone = phone

    def getName(self):
        return self.__name

    def getPhone(self):
        return self.__phone

    def whoAmI(self):
        print("I am a person")

class Customer(Person):
    def __init__(self, name, phone, CustomerNumber):
        Person.__init__(self, name, phone)
        self.__CustomerNumber = CustomerNumber

    def whoAmI(self):
        print("I am a customer")

def display(object):
    if isinstance(object, Customer):
        object.whoAmI()
    elif isinstance(object, Person):
        object.whoAmI()

def main():
    person = Person("Rakan", "8153209887")
    customer = Customer("Natasha", "7089687834", "129")
    display(person)
    display(customer)

main()



