#User function Template for python3


class Solution:
    def sumOfDivisors(self, N):
        sum=0
    	#code here
        for i in range(1,N+1):
            sum+=(N//i)*i
        return sum



#