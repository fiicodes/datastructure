# x=[1,2,3]
# y=[4,5,6]
# s=[x+y for x,y in zip(x,y)]
# print(s)
from functools import reduce,partial
# x=reduce(lambda a,b:a+b ,[1,2,3])
# print(x)
# l=[1,2,3,4]
# _max=lambda a,b:a if a>b else b
# # print(_max(10,12))
# def max_seq(seq):
#     res=seq[0]
#     for i in seq[1:]:
#         res=_max(res,i)
#     return res
# print(max_seq(l))
# n=4
# fac=reduce(lambda a,b:a*b,range(1,n+1))
# print(fac)
# def fac(num):
#     fac=reduce(lambda a,b:a*b,range(1,num+1))
#     return fac
# print(fac(5))
# def funcv(a,b,c):
#     print(a,b,c)
# def func1(b,c):
#     return funcv(10,b,c)
# print(func1(20,340))
#scope
# def func_1():
#     x="hello"
#     def iner_func():
#         print(x)
#     iner_func()
# func_1()
#closure
def func(n):
    def func1(x):
        print( x+n)
    return func1
ad1=func(1)
ad2=func(2)
ad3=func(3)
ad1(2)