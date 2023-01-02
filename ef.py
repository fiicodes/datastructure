class Solution:
    def find(self, nums: list[int]) -> int:
        res=nums[0]
        l,r=0,len(nums)-1
        while(l<r):
            if nums[l]<=nums[r]:
                res=min(res,nums[l])
                break
            mid=(l+r)//2
            res=min(res,nums[mid])
            if nums[l]<=nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return res


ob=Solution()
print(ob.find([4,5,6,7,0,1,2]))