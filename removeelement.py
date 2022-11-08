class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count=0
        n=len(nums)

        for i in range(0,n):
            if nums[i]!=val:
                nums[count]=nums[i]
                count+=1
        return (count,nums)






if __name__=='__main__':
    ob=Solution()
    print(ob.removeElement([0,1,2,2,3,0,4,2],2))




# [[3,2,2,3],]