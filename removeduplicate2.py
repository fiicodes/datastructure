class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for element in nums:
            if i < 2 or nums[i - 2] != element:
                nums[i] = element
                i += 1
        return i
