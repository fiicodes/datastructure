# def lowercasedec(function):
#     def wrapper():
#         fun=function()
#         lower_string=fun.lower()
#         return lower_string
#     return wrapper

# @lowercasedec
# def printstring():
#     return "FITHAASHRAF"
# print(printstring())

def fib(n):
    p=0
    q=1
    while(p<n):
        yield p
        p,q=q,p+q
x=fib(9)

for i in x:
    print(i)

