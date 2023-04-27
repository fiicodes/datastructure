class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        stack=[]
        #if closed==open==n
        #if open<n
        #if closed<open
        def backtrack(openN,closedN):
            if openN==closedN==n:
                res.append("".join(stack))
                return
            if openN<n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN<openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        return res


