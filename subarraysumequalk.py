class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        presSum = defaultdict(int)
        prefix = 0

        for i in range(len(nums)):
            prefix+=nums[i]

            if prefix==k:
                res+=1
            if prefix - k in presSum:
                res+=presSum[prefix-k]
            presSum[prefix] +=1
        return res
#class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     sum1 = 0
    #     count =0
    #     for i in range(len(nums)):
    #         for j in range(i, len(nums)):
    #             sum1 = sum(nums[i:j+1])
    #             if sum1 == k:
    #                 count+=1
    #     return count
