class Solution:
    def maxProduct(self, nums: list[int]) -> int:


        currentmax,currentmin=1,1
        res=nums[0]
        for n in nums:
            vals = (n, n * currentmax, n * currentmin)
            currentmax, currentmin = max(vals), min(vals)

            res = max(res, currentmax)

        return res