# def lower_dec(function):
#     def wrapper():
#         fun = function()
#         low = fun.lower()
#         return low

#     return wrapper


# @lower_dec
# def hello():
#     return "PRINT HII"


# print(hello())
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
