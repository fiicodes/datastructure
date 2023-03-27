class Solution:
    def   twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r=0,len(numbers)-1
        while(l<=r):
            current_sum=numbers[l]+numbers[r]
            if current_sum>target:
                r-=1
            elif current_sum<target:
                l+=1
            else:
                return(l,r)
o=Solution()
print(o.twoSum(numbers =[2,7,11,15], target = 9))


