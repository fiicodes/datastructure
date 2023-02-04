class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low,high=0,len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1

        return -1

