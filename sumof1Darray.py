class Solution:
    def runningSum(self, nums: list[int]) :
        sum=0
        num1=[]
        for i in  range (0,len(nums)):
            sum+=nums[i]
            num1.append(sum)


        return num1


o=Solution()
print((o.runningSum([1,2,3])))

