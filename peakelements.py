class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        while (l <= h):
            mid = (l + h) // 2
            if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                h = mid - 1
            else:
                return mid








