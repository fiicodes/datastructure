class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        depth = maxdepth = 0
        for i in s:
            if i == '(':
                stack.append(i)
            elif i ==')':
                depth = len(stack)
                maxdepth = depth if depth > maxdepth else maxdepth
                stack.pop()
        return maxdepth


