# def outer():
#     x="python"
#     def inner():
#         print(x)
#     return inner

# fn=outer()
# fn()
# print(fn.__closure__)
# def outer():
#     x=[1,2,3]
#     print(hex(id(x)))
#     def inner():
#         y=x
#         print(hex(id(y)))
#     return inner
# fn=outer()
# fn()
# print(fn.__closure__)
# def outer():
#     count=0
    
#     def inner():
#         nonlocal count
#         count+=1
#         return count
#     return inner
# fn=outer()
# print(fn())
# print(fn.__closure__)

# print((hex(id(1))))
#applicatn of closure here we can simplify class using closure
# class Average:
#     def __init__(self):
#         self.total=0
#         self.count=0
#     def add(self,num):
        
#         self.total+=num
#         self.count+=1
#         return self.total/self.count
# a=Average()
# b=Average()
# print(a.add(10))
# print(b.add(30))
# def average():
#     total=0
#     count=0
    
#     def inner(n):
#         nonlocal total,count
#         total+=n
#         count+=1
#         return total/count
#     return inner
# a=average()
# b=average()
# print(a(10))
# print(b(20))
# print(a(20))
# print(b(30))
from itertools import count
from time import perf_counter
# def outer():
#     start=perf_counter()
#     def poll():
#         return perf_counter()-start
#     return poll
# o=outer()
# print(o())
counters=dict()
def outer(fn):
    count=0
    def inner(*args,**kwargs):
        nonlocal count
        count+=1
        counters[fn.__name__]=count
        
        return fn(*args,**kwargs)
    return inner
def add(x,y):
    return x+y
def mult(x,y):
    return x*y
def fac(x):
    f=1
    for i in range(2,x):
        f*=i
    return f

mult=outer(mult)
fac=outer(fac)
print(mult(9,2))

print(fac(4))
print(counters)
print(fac.__closure__)
