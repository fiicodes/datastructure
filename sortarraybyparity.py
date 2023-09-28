class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[count] = nums[count], nums[i]
                count += 1
        return nums
