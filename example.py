class Solution:
    def check_fib(self, arr):
        for i in range(2, len(arr)):
            if arr[i] != arr[i - 1] + arr[i - 2]:
                return False

        return True


ob = Solution()
print(ob.check_fib([0, 1, 1, 2, 3, 5, 8, 13, 21, 34]))
