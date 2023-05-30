class Solution:
    def prime(self,n):
        if n<2:
            return False
        else:
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        largeprime=0
        for i in range(len(nums)):
            if self.prime(nums[i][i]):
                largeprime=max(largeprime,nums[i][i])
            if self.prime(nums[i][len(nums)-i-1]):
                largeprime=max(largeprime,nums[i][len(nums)-i-1])
        return largeprime

        