# from textwrap import wrap


# from functools import wraps
# from time import timezone
def timed(fn):
    from time import perf_counter
    from functools import wraps
    @wraps(fn)
    def inner(*args,**kwaargs):
        start=perf_counter()
        result=fn(*args,**kwaargs)
        end=perf_counter()
        elapsed=end-start
        argument=[str(a) for a in args]
        keyargument=['{0}={1}'.format(k,v) for (k,v) in kwaargs.items() ]
        all_arg=argument+keyargument
        str_args=",".join(all_arg)
        print("{0}{1} took{2:.6f}s to run ".format(fn.__name__,str_args,elapsed))
        return result
    return inner
# #using loop
# @timed
# def loop_fib(n):
#     f1=0
#     f2=1
    
#     for i in range(1,n):
       
#         f3=f1+f2
       
  
    
       
#         f1=f2
#         f2=f3
       
#     print(f3)
       
# (loop_fib(9))


# # fibnocci using  recursion
# class fibno:
#     def __init__(self):
#         self.cache={1:1,2:1}
        
#     def fib(self,n):
#         if n not in self.cache:
#              print("{0} calculating".format(n))


           
#              self.cache[n]=self.fib(n-1)+self.fib(n-2)
      
#         return self.cache[n]
   

# o=fibno()
# print(o.fib(10))
# print(o.fib(9))

# # [0,1,1,2,3]


#fib using closure
def memoiz(fn):
    cachec={1:1,2:1}
    def inner(n):
        
        if  n not in cachec:
            print("calculating{}".format(n))
            # cachec[n]=inner(n-1)+inner(n-2)
            cachec[n]=fn(n)
            print(cachec)
        return cachec[n]
    return inner
# f=fib()
# print(f(9))
# print(f(7))
# print(f(5))
# print(f(6))


#application of dec logger
@memoiz
def fac(n):
    from functools import reduce
    from operator import mul
    return reduce(mul,range(1,n+1))
print(fac(6))

# def logged(fn):
#     from datetime import datetime,timezone
#     from functools import wraps
#     def inner(*args,**kwaargs):
#         login=datetime.now(timezone.utc)
#         result=fn(*args,**kwaargs)
#         print('{0} called {1}'.format(login,fn.__name__))
#         return result
#     return inner
# @logged
# def fun():
#     pass
# def fun1():
#     pass
# fun()
# fun1()
