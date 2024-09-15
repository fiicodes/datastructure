
class Solution:
    def floorSqrt(self, n):
        # Your code here
        s = 1
        e = max(n // 2, 1)

        ans = -1
        while s <= e:
            mid = (s + e) // 2
            if mid * mid == n:
                return mid
            else:
                if mid * mid < n:
                    ans = mid
                    s = mid + 1
                else:
                    e = mid - 1
        return ans
