class Solution:
    def maxDepth(self, s: str) -> int:
        curr = 0
        res = 0
        for c in s:
            if c == "(":
                curr += 1
            elif c == ")":
                curr -= 1
            res = max(res, curr)
        return res

