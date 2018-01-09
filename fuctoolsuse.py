from functools import lru_cache,singledispatch,wraps
import time
import numbers

def clock(func):
    wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print('耗时：',end,'参数：',args)
        return result
    return wrapped

@lru_cache()
@clock
def fac(n):
    if n < 2:
        return n
    else:
        return fac(n-2) + fac(n-1)

#单分派
@singledispatch
def show(obj):
    print(obj,' is a obj')

@show.register(str)
def _(text):
    print(text,'this is a string')

@show.register(numbers.Integral)
def _(n):
    print(n,'this is a number')

if __name__ == '__main__':
    print(fac(6))
    show(fac)
    show('guhongye')
    show(1)
