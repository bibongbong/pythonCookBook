'''
如果想创建一个新的具有类型检查功能的实例属性，可以通过描述器功能来实现

描述器就是有“绑定行为”的对象属性，
该属性的访问控制被描述器协议（__get__(),__set__(),__delete__()）重写。
如果对象定义了任一个上述方法，那它就是描述器。

我们需要对什么方法进行控制就hook哪个方法，比如需要对赋值时进行类型检查
'''

#Integer就是一个描述器,因为定义了__set__()方法.
class Integer(object):
    def __init__(self, name):
        self.name = name
    def __set__(self, instance, value):#因为我们只需要对"修改属性"这个行为进行hook,所以我们只定义__set__()方法就够了,不用__get__()和__delete__().
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value
 
class Point(object):
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
p = Point(2, 3)
p.x = 9
p.x = 9.9#这句会抛出TypeError: Expected an int错误.这就是描述器的作用.
