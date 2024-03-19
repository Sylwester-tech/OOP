class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print("Tworzenie klasy:", name)
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    def __init__(self):
        print("Inicjalizacja instancji MyClass")

# Tworzenie instancji klasy MyClass
obj = MyClass()