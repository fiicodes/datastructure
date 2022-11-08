class Solution:
    def containsDuplicate(self, nums: list[int]) :
        dic=dict()

        for i in range(0,len(nums)):
           if nums[i] in  dic:
              return True

           dic[i]=(nums[i])
        return False

















o=Solution()
print(o.containsDuplicate([3,39]))

