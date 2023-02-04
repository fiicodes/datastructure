class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        count=Counter(nums)
        nums=sorted(list(set(nums)))
        e1,e2=0,0
        for i in range(len(nums)):
            currearn=nums[i]*count[nums[i]]
        #[1,2,3] here 1 is e1,2 is e2,3 is currearn

            if i>0 and nums[i]==nums[i-1]+1:#cant use curend and e2
                temp=e2

                e2=max(currearn+e1,e2)
                e1=temp
            else:
                temp=e2
                e2=currearn+e2
                e1=temp
        return e2












