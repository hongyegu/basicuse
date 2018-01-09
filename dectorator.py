from functools import wraps

#在类中定义装饰器
class A:
    def dectorator1(self,func):
        @wraps(func)
        def newfunc(*wraps,**kwargs):
            print('loging1')
            return func(*wraps,**kwargs)
        return newfunc

    @classmethod
    def dectorator2(self,func):
        @wraps(func)
        def newfunc(*wraps,**kwargs):
            print('loging2')
            return func(*wraps,**kwargs)
        return newfunc
a = A()

@a.dectorator1
def test1():
    pass

@A.dectorator2
def test2():
        pass

import types
#把装饰器定义成类
class DectorClass:

    def __init__(self,func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            print(self)
            print(instance)
            return types.MethodType(self,instance)

@DectorClass
def add(x,y):
    return x + y

#这个地方还是不太懂
class Spam:

    @DectorClass
    def bar(self,x):
        print(self, x)


def main():
    test1()
    test2()
    print(add(2,3))
    print(add.ncalls)
    # 这个地方还是不太懂
    s = Spam()
    print(21)
    s.bar(1)


if __name__ == '__main__':
    main()