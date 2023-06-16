class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0
        for n in nums:
            #check if n is the starting of sequence
            if (n-1) in numSet:

                length=0
                while (length+n) in numSet:
                    length+=1
                longest=max(length,longest)
        return longest


