class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftsum = rightsum = 0
        count = 0
        sum_total = sum(nums)
        for i in range(len(nums) - 1):
            leftsum += nums[i]
            rightsum = sum_total - leftsum
            if leftsum >= rightsum:
                count += 1

        return count

