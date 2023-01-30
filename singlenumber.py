class Solution:
    def singleNumber(self, nums: list[int]) -> int:
       
        for i in nums:
            if nums.count(i)==1:
                return i
        return i


S=Solution()
print(S.singleNumber([4,1,2,1,2]))


