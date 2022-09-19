from itertools import count


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1
        return l

    
                
             
       

obj=Solution()
print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
          

             


    #          class Solution:
    # def removeDuplicates(self, nums: list[int]) -> int:
    #     listforcheck=[]
    #     count=0
    #     underscore=0
    #     for i in ((nums)):
             
    #        if i not in listforcheck:
    #             count+=1
                
    #             listforcheck.append(i)
    #        else:
    #             underscore+=1
    #     for i in range(underscore):
    #          listforcheck.append("_")
    #     print(count,listforcheck)