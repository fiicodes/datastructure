def outer_func(x):
    def inner_func(y):
        return x+y
    return inner_func
closure=outer_func(5)
print(closure(10))