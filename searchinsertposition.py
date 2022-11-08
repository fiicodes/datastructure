class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low,high=0,len(nums)
        while(low<=high):

            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:

                low=mid+1

            else:
                high=mid-1
        return low
ob=Solution()
print(ob.searchInsert([1,3,5,7],4))

