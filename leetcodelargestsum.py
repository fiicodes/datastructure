class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
       maxsum=-1
       for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            if sum>maxsum:
                maxsum=sum
       return maxsum
o=Solution()
print(o.maxSubArray([-3, -2, -2, -3]))