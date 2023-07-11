class Base:

    def __init__(self):
        self.a = "I have rights"
        self.c = "and priviledges"
        self.__b = "more power"


class Derived(Base):

    def __init__(self):
        print(self.a) #accessible
        print(self.c) #accessible
        print(self.__b)

#create an instance of the parent class
obj1 = Base()
print(obj1.a)
print(obj1.c)
