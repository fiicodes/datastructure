def fib(n):
        res=[]
        fibno=[0]*(n+1)
        fibno[0]=0
        fibno[1]=1
        for i in range(2,n+1):
            fibno[i]=fibno[i-1]+fibno[i-2]
            res.append(fibno[i])
        return res




print(fib(9))

