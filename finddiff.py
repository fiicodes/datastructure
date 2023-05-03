class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1=set(nums1)
        set2=set(nums2)
        dif1=list(set1-set2)
        dif2=list(set2-set1)
        return [dif1,dif2]

ob=Solution()
print(ob.findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))
