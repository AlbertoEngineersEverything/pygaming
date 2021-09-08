class MyBaseClass(object):
    def methodOne(self):
        print("MyBaseClass::methodOne()")


class MyChildClass(MyBaseClass):
    def methodOne(self):
        print("MyChildClass::methodOne()")


class Dog(object):
    def makeNoise(self):
        print("Bark!")


class Duck(object):
    def makeNoise(self):
        print("Quick!")


class Foo(object):
    x = 0

    def __init__(self):
        print("Foo constructor")
        self.x = 10

    def printNumber(self):
        print(self.x)


class Bar(Foo):
    def __init__(self):
        super(Bar, self).__init__()
        print("Bar constructor")


def callMethodOne(obj):
    obj.methodOne()


if __name__ == "__main__":

    # instanceOne = MyBaseClass()
    # instanceTwo = MyChildClass()
    #
    # callMethodOne(instanceOne)
    # callMethodOne(instanceTwo)

    # callMethodOne(5)  # Expected error

    animals = [Dog(), Duck()]

    for a in animals:
        a.makeNoise()

    b = Bar()
    b.printNumber()  # This will output with a 0 because Foo object was not initialized.
