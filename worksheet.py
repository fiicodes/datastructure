def sumofarray(nums):
   for i in range(1,len(nums)):
    nums[i]+=nums[i-1]
   return nums
print(sumofarray([1,2,3,4]))