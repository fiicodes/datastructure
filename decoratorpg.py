def lowercase_decorator(function):
    def wrapper():
        fun=function()
        lowercase=fun.lower()
        return lowercase
    return wrapper

def split_decorator(function):
    def wrapper():
        fun=function()
        splitword=fun.split()
        return splitword
    return wrapper
@split_decorator
@lowercase_decorator
def hello():
    return 'Hello World'
print(hello())
# def unique(numlist):
#     li=[]
#     for i in numlist:
#         if i not in li:
#          li.append(i)

#         else:
#          print("not unique")
# d=unique([1,2,3,2,4,5])
# print(d)

