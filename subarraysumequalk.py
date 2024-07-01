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