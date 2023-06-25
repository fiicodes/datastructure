class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        indc=[]
        nums1=[]
        for i  in range(0,len(nums)):
            if nums[i] not in nums1:

                nums1.append(nums[i])
            else:
                indc.append(i)
        print(indc)


ob=Solution()
print(ob.containsNearbyDuplicate([1,2,3,1], k = 3))







