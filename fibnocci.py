class Solution:

    def fib(self, n: int) -> int:
    #     a,b = 0,1
    #     if n == 0:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     else:
    #         for i in range(2,n+1):
    #             a,b = b,a+b
    #         return b
    #dp 
        fibno=[0]*(n+1)
        fibno[0]=0
        fibno[1]=1
        for i in range(2,n+1):
            fibno[i]=fibno[i-1]+fibno[i-2]
        return fibno[n]



ob=Solution()
print(ob.fib(9))