def lower_dec(function):
    def wrapper():
        fun = function()
        lower = fun.lower()
        return lower
