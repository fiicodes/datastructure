class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashset={}
        for i in nums:
            if i not in hashset:
                hashset[i]=1
            else:
                hashset[i]+=1
        return max(hashset,key=hashset.get)
            