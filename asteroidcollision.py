class Solution:
    def collision(arr):
        stack = []
        for a in arr:
            while stack and stack[-1] > 0 > a:
                if stack[-1] > abs(a):
                    stack.pop()
                    continue
                elif stack[-1] == abs(a):
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack
