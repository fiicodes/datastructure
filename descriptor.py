class Descriptor:
    def __get__(self, instance, owner):
        print("Getting attribute")
        return instance._value

    def __set__(self, instance, value):
        print("Setting attribute")
        instance._value = value

    def __delete__(self, instance):
        print("Deleting attribute")
        del instance._value


class MyClass:
    descriptor_attr = Descriptor()

    def __init__(self, value):
        self._value = value


obj = MyClass(10)
print(obj.descriptor_attr)  # Getting attribute
obj.descriptor_attr = 20  # Setting attribute
print(obj.descriptor_attr)  # Getting attribute
del obj.descriptor_attr  # Deleting attribute
