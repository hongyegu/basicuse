from random import shuffle
from inspect import signature

#__doc__是函数对象众多属性中的的一个 help(fun)

#函数可赋值
def cal(n=10):
    return n * n

def cancallable(func):
    if callable(func):
        print('%s 是可调用的对象' % func.__name__)
#创建可调用的类实例，可以将类当作函数使用
class CanCall:
    def __init__(self,items):
        self._item = list(items) #list函数接受任何可迭代对象
        #对象没有而函数有的属性
        self.__name__ = 'CanCall'
        shuffle(self._item)
    def pick(self):
        try:
            return self._item.pop()
        except IndexError:
            raise LookupError('cant find thats empty')
    def __call__(self, *args, **kwargs):
        return self.pick()
#函数注解
def add(x:int,y:'int>0'=80) ->int:
    """
    :param x:
    :param y:
    :return x+y:
    """
    return x + y
if __name__ == '__main__':
    pingfang = cal
    #老式写法 list(result)
    result = map(pingfang,range(10))
    #python3
    newresult = [pingfang(n) for n in range(10)]
    newresult1 = [pingfang(n) for n in range(10) if n % 2 ]

    #lambda 方法
    #sorted 返回排序后的对象
    la = sorted(newresult,key=lambda item:-1*item)
    print(la)

    #判断对象能否调用
    cancallable(cal)
    print(newresult)
    #任何对象都可以表现的像函数，只要它实现了__call__方法
    cancall = CanCall(newresult)
    # cancall.pick()
    # cancall()
    cancallable(cancall)

    #从这其实可以看出，'万物皆属性'
    print(dir(cancall))
    print(dir(cal))

    #通过函数通过__defaults__保存定位参数和关键字参数的默认值
    print(cal.__defaults__)
    #使用inspect 提取函数前面
    insp =signature(cal)
    print(insp)
    for name,param in insp.parameters.items():
        print('名称：',name,'类型：',param.kind,'值：',param.default)

    #bind方法验证传入参数是否正确,用于绑定实参与形参
    try:
        verifyargs = {'n':20,'m':20}
        bound_args = insp.bind(**verifyargs) #got an unexpected keyword argument 'm'
    except TypeError as e:
        print(e)
    print(add.__annotations__)#函数的注解

    #函数式编程
    from operator import itemgetter,attrgetter
    testlist =[('a','b'),('a','c'),('a', 'e'),('a', 'a')]
    i = list(sorted(testlist,key=itemgetter(1))) #按指定字段排序
    print(i)
    #attrgetter 可以根据名称提取对象的属性，深入嵌套对象，获取指定属性
    #sorted(list,key=attrgetter('coord.lat'))

    #functools.partial
    import functools
    newadd = functools.partial(add,x=10)
    print(newadd())
    