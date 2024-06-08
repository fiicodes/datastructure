class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = nums[0]

        # calculate next prefix and check sebsets prior to r in the same time
        for r in range(1, len(nums)):
            prefixSum += nums[r]

            # check if the are two zeros in a row
            if nums[r] == 0 and (
                    (r > 0 and nums[r - 1] == 0) or
                    (r < len(nums) - 1 and nums[r + 1] == 0)):
                return True

            # check subsets
            s = prefixSum
            l = 0
            while l < r and s >= k:
                if s == 0 or s % k == 0:
                    return True

                s -= nums[l]
                l += 1

        return False
