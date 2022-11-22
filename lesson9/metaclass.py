class CustomMeta(type):
    def __new__(cls, name, bases, dct):
        meths = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        new_meths = dict(('method_' + name, value) if callable(value) else (name, value) for name, value in meths)
        new_meths['class_name'] = name.lower()
        return type.__new__(cls, name, bases, new_meths)

if __name__ == "__main__":
    class Proba(metaclass=CustomMeta):

        def __init__(self):
            self.atr = 'ATR'
            print('init')

        def method1(self):
            print('Method1')

        def method2(self):
            print('Method2')

    a = Proba()
    print(a.__dict__)
    print(dir(a))
    print(a.class_name)
    a.method_method1()
    a.method_method2()
    print(a.__dict__)
