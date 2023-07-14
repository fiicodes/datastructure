class Solution:
    def fact(self, N):
        f = 1
        for i in range(1, N + 1):
            f *= i
        return f


obj = Solution()
print(obj.fact(4))
