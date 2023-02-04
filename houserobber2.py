class Solution:
    def rob(self, nums: list[int]) -> int:
        #here it is same as the house rob 1 except the first and last element are adjacent to each other.So we will call the functn in 2 parts  and find the maximum .Suppose the array has only 1 elementso we find the max of 3 condition.
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))


    def helper(self,nums):
            rob1,rob2=0,0
            for i in nums:
                temp=max(rob1+i,rob2)
                rob1=rob2
                rob2=temp
            return rob2


