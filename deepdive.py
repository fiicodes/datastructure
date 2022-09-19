


#factorial is example case where we need to mutable as default





# def fact(n,cachev={}):
#     if n <1:
#         return 1
#     elif n in cachev:
#         return cachev[n]
#     else:
#         print("calculating {0}".format(n))
#         outp= n*fact(n-1)
       
#         cachev[n]=outp
#         print(cachev)
      
#         return outp

# print(fact(3))
# print(fact(3))
# print(fact(2))

# print(fact(10))
# print(fact(5))
# print(fact(6))
# print(fact(5))
# print(fact(4))
# print(id(fact(4)))
# print(id(fact(5)))


# print(fact(5))


# def func(a: "somethimg for a",  b :"some value for b"=1)->"return type":
#     """hello documentation"""
#     return a*b
# print(func.__annotations__)
# print(func.__doc__)
# import random


# print(sorted(s,key=lambda e:random.random()))
# def mul_numbers(nums):
#     new_arr = []
#     for i in range(len(nums)):
#         product = 1
#         for j in range(len(nums)):
#             if nums[i] != nums[j]:
#                 product *= nums[j]
#         new_arr.append(product)

#     return new_arr


# arr = [1, 2, 3, 4]
# result = mul_numbers(arr)
# print(result)

# >>> [120, 60, 40, 30, 24]
##function introspection
# def func(a:"mandatory positional paramete",b:"optional positional parameter"=1,c=2,*args:"optional positional parameter",kw1,kw2=100,kw3=200,**kwargs:"optional keyword argument")->"return nothing":
#      """This is a sample function"""
#      i=20
#      j=68
# print(func.__annotations__)
# print(dir(func))
# func.newattri="hjj"
# print(func.__kwdefaults__)
# print(id(func))
# def func_id(f):
#     print(id(f))
#     print(f.__name__)
# func_id(func)
# import inspect
# s=(inspect.signature(func))
# print(s.parameters)
# print(callable(print))