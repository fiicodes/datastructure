class Solution:
    def findMin(self, nums: list[int]) -> int:
        res=nums[0]
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]<=nums[r]:
                res=min(res,nums[l])
                break
            m=(l+r)//2
            res=min(res,nums[m])
            if nums[m]>=nums[l]:
                l=m+1
            else:


                r=m-1
        return res

ob=Solution()
print(ob.findMin([4,5,6,7,0,1,2],))


##Another method

class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        l = 0
        h = len(nums) - 1
        if nums[l] <= nums[h]:
            return nums[l]
        while (l <= h):
            mid = (l + h) // 2
            if mid > 0:
                if nums[mid] < nums[mid - 1]:
                    return nums[mid]
            if mid < len(nums) - 1:
                if nums[mid] > nums[mid + 1]:
                    return nums[mid + 1]
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                h = mid - 1

