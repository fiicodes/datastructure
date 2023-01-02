class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        totalsum=sum(nums)
        leftsum=0
        for i in  range (len(nums)):
            rightsum=totalsum-nums[i]-leftsum
            if leftsum==rightsum:
                return i

            leftsum+=nums[i]
        return -1

S=Solution()
print(S.pivotIndex([1,7,3,6,5,6]))