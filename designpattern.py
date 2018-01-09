#经典策略
#使用abc

from abc import ABC,abstractmethod
from collections import namedtuple

#定义具名元祖 Customer

Customer = namedtuple('Customer','name fidelity')

#购物车

class LineItem:
    def __init__(self,product,quantity,price):
        self.price = price
        self.product = product
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

#order 类，promotion 具体折扣子类
class Order:
    def __init__(self,customer,cart,promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self,'__toatal'): #在我们创建一个以"__"两个下划线开始的方法时，这意味着这个方法不能被重写，它只允许在该类的内部中使用。
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    #折扣价
    def due(self):
        if self.promotion is None:
            discount = 0
        elif callable(self.promotion,):
            discount = self.promotion(self)
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = 'total : {:.2f} due: {:.2f}'
        return fmt.format(self.total(),self.due())

#折扣抽象基类
class Promotion(ABC):
    @abstractmethod #继承子类必须实现基类抽象方法
    def discount(self):
        """返回折扣金额"""

#第一个折扣策略
class FidelityPromo(Promotion):
    """积分1000以上的提供5%的折扣"""
    def discount(self,order):
        return order.total() * .05 if order.customer.fidelity >=1000 else 0

#单个商品达到20个以上，第二个折扣策略
class BulkItemPromo(Promotion):
    """提供10%的折扣"""
    def discount(self,order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount
#另一种策略方法，使用函数对象
def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount
def fidelity_promo(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

promtios = [fidelity_promo,bulk_item_promo]

def best_promo(order):
    return max(item(order) for item in promtios)

#使用装饰器改进上面的例子

pro = []

#装饰器在模块导入的时候执行
def promotion(func):
    print('使用装饰器改进')
    pro.append(func)
    return func

@promotion
def bulk_item_promo1(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def fidelity_promo1(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


