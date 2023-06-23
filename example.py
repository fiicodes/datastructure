def lower_case_dec(function):
    def wrapper():
        fun=function()
        lower_case=fun.lower()
        return lower_case
    return wrapper

@lower_case_dec
def myname():
    return "HELLO FITHA!!"
print(myname())
