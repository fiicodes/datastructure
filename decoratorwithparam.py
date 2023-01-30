def  my_func():
    print("hhj")

def outer(rep):
    def timed(fn):
        from time import perf_counter
        
        def inner(*args,**kwaargs):
            total_elapsed=0
            for i in range(rep):
                start=perf_counter()
                result=fn(*args,**kwaargs)
                end=perf_counter()
                total_elapsed=end-start
            avg_elapsed=total_elapsed/rep
            print(avg_elapsed)
            return result
        return inner
    return timed
my=outer(10)(my_func)
print(my())

