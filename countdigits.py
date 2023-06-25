class Solution:
    def evenlyDivides (self, N):
        c=0
        N=str(N)
        for i in N:
            if i!='0':
                N=int(N)
                i=int(i)
                if N%i==0:
                    c+=1
        return c


