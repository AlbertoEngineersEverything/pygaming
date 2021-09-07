class MyBaseClass(object):
    def methodOne(self):
        print("MyBaseClass::methodOne()")


class MyChildClass(MyBaseClass):
    def methodOne(self):
        print("MyChildClass::methodOne()")