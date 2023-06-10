class Solution:
    def can_construct(nums, index, maxSum, mid):
        n = len(nums)
        remaining_sum = maxSum - mid

        total_sum = 0
        for i in range(n):
            if i < index:
                total_sum += 1
            elif i > index:
                value = min(mid, remaining_sum // (n - index))
                total_sum += value
                remaining_sum -= value

        return total_sum <= maxSum

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        low = 1
        high = maxSum

        while low <= high:
            mid = (low + high) // 2

            if self.can_construct(self.nums, index, maxSum, mid):
                low = mid + 1
            else:
                high = mid - 1

        return high


