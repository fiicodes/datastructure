class Solution:
    def maxProduct(self, nums: list[int]) -> int:


        currentmax=max_global=nums[0]
        for i in range(1,len(nums)):
            currentmax=max((abs(nums[i]),abs(nums[i]*currentmax)))
            if currentmax > max_global:
                max_global=currentmax
        return max_global

ob=Solution()
l= [-2,3,-4]
print(ob.maxProduct(l))
















