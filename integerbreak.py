class Solution:
    def integerBreak(self, n: int) -> int:
        # Handle base cases
        if n == 2:
            return 1
        if n == 3:
            return 2

        # Initialize a list to store the maximum product for each number from 2 to n
        dp = [0] * (n + 1)

        # Base cases
        dp[2] = 2
        dp[3] = 3

        # Fill in the dp list iteratively
        for i in range(4, n + 1):
            dp[i] = max(dp[i - 2] * 2, dp[i - 3] * 3)

        return dp[n]

