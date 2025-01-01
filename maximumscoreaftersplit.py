class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        s = list(s)
        print(s)
        for i in range(0, len(s)):
            for j in range(i + 1, len(s)):
                count_zero = s[0:i + 1].count('0')
                print('c0',count_zero)
                count_one = s[j:].count('1')
                print('c1',count_one )
                res = max(res, count_zero + count_one)
        return res
ob = Solution()
s = "011101"
print(ob.maxScore(s))
