class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        res=[]
        i=0
        j=n
        while(i<n):
            res.append(nums[i])
            res.append(nums[j])
            i+=1
            j+=1
        return res


ob=Solution()
print(ob.shuffle(  [2,5,1,3,4,7],n=3))

