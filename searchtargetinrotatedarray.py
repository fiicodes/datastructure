class Solution:
    def search(self, nums: list[int],target) -> int:

        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            #left sorted
            if nums[l]<=nums[mid]:
                if target<nums[l] or target >nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if target>nums[r] or target <nums[mid]:
                    r=mid-1
                else:
                   l=mid+1
        return -1




ob=Solution()
print(ob.search([4,5,6,7,0,1,2],88))
