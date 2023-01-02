
class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1,rob2=0,0
        #[rob1,rob2,i,n+1...]
        for i in nums:
            temp=max(rob1+i,rob2)
            rob1=rob2
            rob2=temp
        return rob2
o=Solution()
print(o.rob([2,7,9,3,1]))